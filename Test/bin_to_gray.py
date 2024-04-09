def bin_to_gray(bin_num):
    bin_str = str(bin_num)  # Convert integer to string
    gray_str = ''
    gray_str += bin_str[0]
    for i in range(1, len(bin_str)):
        gray_str += str(int(bin_str[i - 1]) ^ int(bin_str[i]))
    return gray_str
for i in range(5):
    print(bin_to_gray(bin(i)[2:]))