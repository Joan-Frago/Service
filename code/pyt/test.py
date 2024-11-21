#!/usr/bin/python3

def writeFile(aFile:str, aContent):
    with open(aFile, "a") as file:
        file.write(str(f"{aContent}\n"))

if __name__ == "__main__":
    iFile = "../../src/test.txt"
    iContent = 0
    while iContent < 100000:
        writeFile(iFile, iContent)
        iContent += 1
