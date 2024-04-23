function convert() {
  // Get the values from the input fields
  const binaryInput = document.getElementById("binaryInput").value;
  const decimalInput = document.getElementById("decimalInput").value;
  const hexInput = document.getElementById("hexInput").value;
  const octalInput = document.getElementById("octalInput").value;
  const excess3Input = document.getElementById("excess3Input").value;
  const grayCodeInput = document.getElementById("grayCodeInput").value;

  // Clear any previous output
  document.getElementById("decimalInput").value = "";
  document.getElementById("binaryInput").value = "";
  document.getElementById("hexInput").value = "";
  document.getElementById("octalInput").value = "";
  document.getElementById("excess3Input").value = "";
  document.getElementById("grayCodeInput").value = "";

  // Check which input field has a value
  let userInput;
  if (binaryInput) {
    userInput = parseInt(binaryInput, 2); // Convert binary to decimal
  } else if (decimalInput) {
    userInput = parseInt(decimalInput);
  } else if (hexInput) {
    userInput = parseInt(hexInput, 16); // Convert hexadecimal to decimal
  } else if (octalInput) {
    userInput = parseInt(octalInput, 8); // Convert octal to decimal
  } else if (excess3Input) {
    userInput = parseInt(excess3Input,2) - 3; // Convert excess-3 to decimal
  } else if (grayCodeInput) {
    // Gray code conversion requires additional logic based on code length
    userInput = convertGrayCode(grayCodeInput);
  }

  // If no valid input is found, show an error message
  if (!userInput) {
    alert("Please enter a valid value in one of the input fields.");
    return;
  }

  // Convert the decimal value to other data types
  const binary = userInput.toString(2);
  const decimal = userInput.toString(10);
  const hex = userInput.toString(16).toUpperCase();
  const octal = userInput.toString(8);
  const excess3 = (userInput + 3).toString(2);
  const grayCode = convertDecimalToGray(userInput); // Convert decimal to Gray code

  // Update the output fields
  document.getElementById("decimalInput").value = decimal;
  document.getElementById("binaryInput").value = binary;
  document.getElementById("hexInput").value = hex;
  document.getElementById("octalInput").value = octal;
  document.getElementById("excess3Input").value = excess3;
  document.getElementById("grayCodeInput").value = grayCode;
}

// Function to convert decimal to Gray code (implementation example)
function convertDecimalToGray(decimal) {
  let grayCode = decimal.toString(2); // Convert to binary first
  grayCode = grayCode.slice(0, -1) + (grayCode[grayCode.length - 1] === "0" ? "0" : "1");
  return grayCode;
}

// Function to convert Gray code to decimal (implementation example)
function convertGrayCode(grayCode) {
  let decimal = 0;
  for (let i = grayCode.length - 1; i >= 0; i--) {
    decimal ^= parseInt(grayCode[i]);
    decimal <<= 1;
  }
  return decimal >> 1; // Remove the leading zero from the shift
}
