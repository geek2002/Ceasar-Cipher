letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryptFile(shift):
    inputFile=open("input.txt","r")
    outputFile=open("output.txt","w")
    lines=inputFile.readlines()
    
    for line in lines:
        newLine=[]
        for x in range(len(line)):
            lowered=False
            letter=line[x:(x+1)]
            newLetter=""
            if letter.isupper():
                    letter=letter.lower()
                    lowered=True
            if letter in letters:
                letterIndex=letters.index(letter)
                newIndex = letterIndex+shift
                if newIndex >= len(letters):
                    newIndex-=26
                newLetter=letters[newIndex]
            else:
                newLetter=letter
            if lowered:
                newLetter=newLetter.upper()
            newLine.append(newLetter)
        line="".join(newLine)
        print(line)
        outputFile.writelines(line)
    menu(1)
def decryptFile(shift):
    inputFile=open("input.txt","r")
    outputFile=open("output.txt","w")
    lines=inputFile.readlines()
    
    for line in lines:
        newLine=[]
        for x in range(len(line)):
            lowered=False
            letter=line[x:(x+1)]
            newLetter=""
            if letter.isupper():
                    letter=letter.lower()
                    lowered=True
            if letter in letters:
                letterIndex=letters.index(letter)
                newIndex = letterIndex-shift
                if newIndex < 0:
                    newIndex+=26
                newLetter=letters[newIndex]
            else:
                newLetter=letter
            if lowered:
                newLetter=newLetter.upper()
            newLine.append(newLetter)
        line="".join(newLine)
        print(line)
        outputFile.writelines(line)
    menu(2)

def menu(code):
    codes=["","Encryption","Decryption"]
    if code > 0:
        print(codes[code] + " Sucessful, output.txt created")
    print("╔═════════════════════════════════════════╗")
    print("║       1:Encrypt                         ║")
    print("║       2:Decrypt                         ║")
    print("║       3:Exit                            ║")
    print("╚═════════════════════════════════════════╝")
    do=input(">> ")
    if do == "1":
        shift = int(input("Enter Shift >> "))
        encryptFile(shift)
    elif do == "2":
        shift = int(input("Enter Shift >> "))
        decryptFile(shift)
    elif do == "3":
        exit()
    else:
        print("Error , Please only use 1,2,3,4 or 5")
        menu()
menu(0)