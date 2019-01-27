maxPalindrome = 0
palindromeNumber = 0
firstNumber = 0
secondNumber = 0
thirdNumber = 0
fourthNumber = 0
fifthNumber = 0
lastNumber = 0

for a in range(100,1000):
    for b in range(100,1000):

        c = a*b

        #Check if c is a palindrome
        cString = str(c)
        cStringLength = len(cString)

        #cStringLength will always be 5 or 6 for this problem
        if cStringLength == 5:
            
            firstNumber = int(cString[0])
            secondNumber = int(cString[1])
            thirdNumber = int(cString[2])
            fourthNumber = int(cString[3])
            lastNumber = int(cString[4])

            if firstNumber - lastNumber == 0:
                if secondNumber - fourthNumber == 0:
                        palindromeNumber = c

        else:
            firstNumber = int(cString[0])
            secondNumber = int(cString[1])
            thirdNumber = int(cString[2])
            fourthNumber = int(cString[3])
            fifthNumber = int(cString[4])
            lastNumber = int(cString[5])

            if firstNumber - lastNumber == 0:
                if secondNumber - fifthNumber == 0:
                    if thirdNumber - fourthNumber == 0:
                            palindromeNumber = c


        if palindromeNumber > maxPalindrome:
            maxPalindrome = palindromeNumber

print(maxPalindrome)
