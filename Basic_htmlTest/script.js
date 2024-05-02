// JavaScript part for handling Ajax requests
function sendConversionRequest() {
  // Get the values from the input fields
  const form = document.getElementById("conversionForm");
  const formData = new FormData(form);

  // Check which input field has a value
  const data = {};
  formData.forEach((value, key) => {
    if (value) {
      data[key] = value;
    }
  });

  // Send an Ajax request with the data to the server endpoint
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/convertDataTypes", true); // Adjust the endpoint as needed
  xhr.setRequestHeader("Content-Type", "application/json");

  // Handle the server's response
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      const response = JSON.parse(xhr.responseText);

      // Update the input fields with the converted values
      document.getElementById("binaryInput").value = response.binary;
      document.getElementById("decimalInput").value = response.decimal;
      document.getElementById("hexInput").value = response.hex;
      document.getElementById("octalInput").value = response.octal;
      document.getElementById("excess3Input").value = response.excess3;
      document.getElementById("grayCodeInput").value = response.grayCode;
    } else if (xhr.readyState === 4) {
      alert("An error occurred during the conversion.");
    }
  };

  xhr.send(JSON.stringify(data));
}
