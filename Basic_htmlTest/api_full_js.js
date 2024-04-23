
function convert() {
    // Get input values
    var binary = document.getElementById("binaryInput").value;
    var decimal = parseInt(binary, 2);
    var hex = decimal.toString(16).toUpperCase();
    var octal = decimal.toString(8);
    var excess3 = (parseInt(binary, 2) + 3).toString(2);
    var grayCode = (parseInt(binary, 2) ^ (parseInt(binary, 2) >> 1)).toString(2);

    // Update input boxes
    document.getElementById("decimalInput").value = decimal;
    document.getElementById("hexInput").value = hex;
    document.getElementById("octalInput").value = octal;
    document.getElementById("excess3Input").value = excess3;
    document.getElementById("grayCodeInput").value = grayCode;
}
