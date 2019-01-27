checkNumber = 20
remainderList = list(range(1,2))

while max(remainderList) > 0:
    remainderList = list()
    
    for i in range(1,21):
        if checkNumber % i > 0:
            remainderList.append(1)
        else:
            remainderList.append(0)
        
    checkNumber +=1

print(checkNumber - 1)


        
