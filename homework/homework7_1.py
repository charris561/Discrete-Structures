def reverseString(string):
    #from geeks for geeks: https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
    string = list(string)
    string.reverse()
    return "".join(string)

def decToBinaryConversion(n):
    # decimal to binary conversion
    if (n > 0):
        R = n % 2  
        binaryNumber = str(int(R))
        n = (n - R) / 2

        while (n != 0):
            R = n % 2
            binaryNumber += str(int(R))
            n = (n - R) / 2

        binaryNumber = reverseString(binaryNumber)
    
    else: 
        raise Exception("Input must be larger than 0")

    return binaryNumber


decimalNum = int(input("Please input a decimal number above 0 (Press CTRL + C to exit): "))
print(f"The binary number is: {decToBinaryConversion(decimalNum)}")