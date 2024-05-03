
import _thread
import uasyncio as asyncio
import json
import time
import convert_with_lcd
import NetworkCredentials
import RequestParser
import ResponseBuilder

# Helper functions for conversions (same as previous code)

def gray_to_decimal(gray):
    binary = gray
    result = binary[0]
    for bit in binary[1:]:
        result = result + str(int(result[-1]) ^ int(bit))
    return int(result, 2)

# Function to handle HTTP requests (same as previous code)
async def handle_request(reader, writer):
    # Read the HTTP request
    request_line = await reader.readline()
    print("Request:", request_line)

    # Read the headers
    headers = {}
    while True:
        line = await reader.readline()
        if not line or line == b"\r\n":
            break
        key, value = line.decode().split(":", 1)
        headers[key.strip()] = value.strip()

    # If POST, read the body content
    if "Content-Length" in headers:
        content_length = int(headers["Content-Length"])
        body = await reader.read(content_length)
        data = json.loads(body)

        # Determine the key with a value to convert from
        conversion_key = list(data.keys())[0]
        value_str = data[conversion_key]
        decimal_value = None
        
        if conversion_key == "binaryInput":
            decimal_value = int(value_str, 2)
        elif conversion_key == "decimalInput":
            decimal_value = int(value_str)
        elif conversion_key == "hexInput":
            decimal_value = int(value_str, 16)
        elif conversion_key == "octalInput":
            decimal_value = int(value_str, 8)
        elif conversion_key == "excess3Input":
            decimal_value = int(value_str, 2) - 3
        elif conversion_key == "grayCodeInput":
            decimal_value = gray_to_decimal(value_str)

        if decimal_value is None:
            response_body = json.dumps({"error": "Invalid input"})
            response_headers = [
                "HTTP/1.1 400 Bad Request",
                "Content-Type: application/json",
                "Content-Length: {}".format(len(response_body)),
            ]
            await writer.write("\r\n".join(response_headers).encode())
            await writer.write("\r\n\r\n".encode())
            await writer.write(response_body.encode())
            await writer.drain()
            await writer.aclose()
            return
        
        # Convert decimal to other formats
        binary = decimal_to_binary(decimal_value)
        decimal = str(decimal_value)
        hex_val = decimal_to_hex(decimal_value)
        octal = decimal_to_octal(decimal_value)
        excess3 = decimal_to_excess3(decimal_value)
        grayCode = decimal_to_gray(decimal_value)

        # Create response
        response_body = json.dumps({
            "binary": binary,
            "decimal": decimal,
            "hex": hex_val,
            "octal": octal,
            "excess3": excess3,
            "grayCode": grayCode
        })

        response_headers = [
            "HTTP/1.1 200 OK",
            "Content-Type: application/json",
            "Content-Length: {}".format(len(response_body))
        ]

        # Send response
        await writer.write("\r\n".join(response_headers).encode())
        await writer.write("\r\n\r\n".encode())
        await writer.write(response_body.encode())
        await writer.drain()
        await writer.aclose()


# Core 0: Start HTTP serverk
async def start_server():
    server = await asyncio.start_server(handle_request, "0.0.0.0", 80)
    async with server:
        await server.serve_forever()

# Launch the server on core 0 with asyncio
def start_http_server():
    asyncio.run(start_server())

# Running the conversion with LCD on core 1
_thread.start_new_thread(convert_with_lcd, ())

# Start HTTP server on core 0
start_http_server()
