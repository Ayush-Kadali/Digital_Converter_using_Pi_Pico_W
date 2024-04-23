# full demo with web control panel
# combines multi core and multi tasking

import utime
from RequestParser import RequestParser
import json
import uasyncio
import _thread
from ResponseBuilder import ResponseBuilder
from WiFiConnection import WiFiConnection
import buzzer
import convert_with_lcd


# connect to WiFi
if not WiFiConnection.start_station_mode(True):
    raise RuntimeError('network connection failed')


async def handle_request(reader, writer):
    try:
        raw_request = await reader.read(2048)

        request = RequestParser(raw_request)

        response_builder = ResponseBuilder()

        # filter out api request
        if request.url_match("/api"):
            action = request.get_action()
            if action == 'play_buzzer':
                datatype = request.data()['datatype']
                number = requent.data()['number']
                buzzer.play_data(datatype , number)
                
            elif action == 'readData':
                # ajax request for data
                response_obj = data
                response_builder.set_body_from_dict(response_obj)

            elif action == 'setData':
                datatype = request.data()['datatype']
                number = requent.data()['number']
                data = to_bin.to_bin(datatype,number)


                status = 'OK'

                response_obj = getdata()
                response_builder.set_body_from_dict(response_obj)
            else:
                # unknown action
                response_builder.set_status(404)

        # try to serve static file
        else:
            response_builder.serve_static_file(request.url, "/api_index.html")

        response_builder.build_response()
        writer.write(response_builder.response)
        await writer.drain()
        await writer.wait_closed()

    except OSError as e:
        print('connection error ' + str(e.errno) + " " + str(e))


async def main():
    print('Setting up webserver...')
    server = uasyncio.start_server(handle_request, "0.0.0.0", 80)
    uasyncio.create_task(server)


def conversion():
#     convert_with_lcd.init()
#     convert_with_lcd.uasync()
    pass
    


# start neopixel scrolling loop on second processor
second_thread = _thread.start_new_thread(conversion, ())

try:
    # start asyncio tasks on first core
    uasyncio.run(main())
finally:
    print("running finally block")
    uasyncio.new_event_loop()