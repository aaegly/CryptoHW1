__author__ = 'andrewegly'
"""
Andrew Egly
HW1: 5 ciphers that can be used in command line to encrypt/decrypt txt files

The code for my ciphers is all in CiphersHW1.py. I have the Caesar cipher, Simple substitution,
poly-alphabetic, transposition, and a spinoff of the Caesar cipher that uses numbers instead
of letters in encryption.


Run this program like a regular python program from command line
It'll walk you through each step

Ciphers: caesar, simpleSub, polyAlpha, transpose, number

for adding a path, I recomend just using the txtfile I threw in there, you can
fill it with whatever you want, or use your own.
"""

import string
# -------------------------------------------------
# initialize alphabets for caesar.
alphabet = {}
alphabet["A"] = "D"
alphabet["B"] = "E"
alphabet["C"] = "F"
alphabet["D"] = "G"
alphabet["E"] = "H"
alphabet["F"] = "I"
alphabet["G"] = "J"
alphabet["H"] = "K"
alphabet["I"] = "L"
alphabet["J"] = "M"
alphabet["K"] = "N"
alphabet["L"] = "O"
alphabet["M"] = "P"
alphabet["N"] = "Q"
alphabet["O"] = "R"
alphabet["P"] = "S"
alphabet["Q"] = "T"
alphabet["R"] = "U"
alphabet["S"] = "V"
alphabet["T"] = "W"
alphabet["U"] = "X"
alphabet["V"] = "Y"
alphabet["W"] = "Z"
alphabet["X"] = "A"
alphabet["Y"] = "B"
alphabet["Z"] = "C"

Dalphabet = {}
Dalphabet["D"] = "A"
Dalphabet["E"] = "B"
Dalphabet["F"] = "C"
Dalphabet["G"] = "D"
Dalphabet["H"] = "E"
Dalphabet["I"] = "F"
Dalphabet["J"] = "G"
Dalphabet["K"] = "H"
Dalphabet["L"] = "I"
Dalphabet["M"] = "J"
Dalphabet["N"] = "K"
Dalphabet["O"] = "L"
Dalphabet["P"] = "M"
Dalphabet["Q"] = "N"
Dalphabet["R"] = "O"
Dalphabet["S"] = "P"
Dalphabet["T"] = "Q"
Dalphabet["U"] = "R"
Dalphabet["V"] = "S"
Dalphabet["W"] = "T"
Dalphabet["X"] = "U"
Dalphabet["Y"] = "V"
Dalphabet["Z"] = "W"
Dalphabet["A"] = "X"
Dalphabet["B"] = "Y"
Dalphabet["C"] = "Z"

# -------------------------------------------------
# initialize alphabets for simple sub
Salphabet = {}
Salphabet["A"] = "Q"
Salphabet["B"] = "W"
Salphabet["C"] = "E"
Salphabet["D"] = "R"
Salphabet["E"] = "T"
Salphabet["F"] = "Y"
Salphabet["G"] = "U"
Salphabet["H"] = "I"
Salphabet["I"] = "O"
Salphabet["J"] = "P"
Salphabet["K"] = "A"
Salphabet["L"] = "S"
Salphabet["M"] = "D"
Salphabet["N"] = "F"
Salphabet["O"] = "G"
Salphabet["P"] = "H"
Salphabet["Q"] = "J"
Salphabet["R"] = "K"
Salphabet["S"] = "L"
Salphabet["T"] = "Z"
Salphabet["U"] = "X"
Salphabet["V"] = "C"
Salphabet["W"] = "V"
Salphabet["X"] = "B"
Salphabet["Y"] = "N"
Salphabet["Z"] = "M"

SDalphabet = {}
SDalphabet["Q"] = "A"
SDalphabet["W"] = "B"
SDalphabet["E"] = "C"
SDalphabet["R"] = "D"
SDalphabet["T"] = "E"
SDalphabet["Y"] = "F"
SDalphabet["U"] = "G"
SDalphabet["I"] = "H"
SDalphabet["O"] = "I"
SDalphabet["P"] = "J"
SDalphabet["A"] = "K"
SDalphabet["S"] = "L"
SDalphabet["D"] = "M"
SDalphabet["F"] = "N"
SDalphabet["G"] = "O"
SDalphabet["H"] = "P"
SDalphabet["J"] = "Q"
SDalphabet["K"] = "R"
SDalphabet["L"] = "S"
SDalphabet["Z"] = "T"
SDalphabet["X"] = "U"
SDalphabet["C"] = "V"
SDalphabet["V"] = "W"
SDalphabet["B"] = "X"
SDalphabet["N"] = "Y"
SDalphabet["M"] = "Z"

# -------------------------------------------------
# initialize a third alphabet set for polyalphabetical
Palphabet = {}
Palphabet["A"] = "M"
Palphabet["B"] = "X"
Palphabet["C"] = "H"
Palphabet["D"] = "S"
Palphabet["E"] = "I"
Palphabet["F"] = "R"
Palphabet["G"] = "N"
Palphabet["H"] = "Z"
Palphabet["I"] = "G"
Palphabet["J"] = "A"
Palphabet["K"] = "U"
Palphabet["L"] = "E"
Palphabet["M"] = "B"
Palphabet["N"] = "L"
Palphabet["O"] = "F"
Palphabet["P"] = "P"
Palphabet["Q"] = "Y"
Palphabet["R"] = "W"
Palphabet["S"] = "V"
Palphabet["T"] = "K"
Palphabet["U"] = "D"
Palphabet["V"] = "O"
Palphabet["W"] = "T"
Palphabet["X"] = "Q"
Palphabet["Y"] = "C"
Palphabet["Z"] = "J"

PDalphabet = {}
PDalphabet["M"] = "A"
PDalphabet["X"] = "B"
PDalphabet["H"] = "C"
PDalphabet["S"] = "D"
PDalphabet["I"] = "E"
PDalphabet["R"] = "F"
PDalphabet["N"] = "G"
PDalphabet["Z"] = "H"
PDalphabet["G"] = "I"
PDalphabet["A"] = "J"
PDalphabet["U"] = "K"
PDalphabet["E"] = "L"
PDalphabet["B"] = "M"
PDalphabet["L"] = "N"
PDalphabet["F"] = "O"
PDalphabet["P"] = "P"
PDalphabet["Y"] = "Q"
PDalphabet["W"] = "R"
PDalphabet["V"] = "S"
PDalphabet["K"] = "T"
PDalphabet["D"] = "U"
PDalphabet["O"] = "V"
PDalphabet["T"] = "W"
PDalphabet["Q"] = "X"
PDalphabet["C"] = "Y"
PDalphabet["J"] = "Z"

# -------------------------------------------------
# initialize alphabets for number variation of caesar cipher
Nalphabet = {}
Nalphabet["A"] = "4"
Nalphabet["B"] = "5"
Nalphabet["C"] = "6"
Nalphabet["D"] = "7"
Nalphabet["E"] = "8"
Nalphabet["F"] = "9"
Nalphabet["G"] = "10"
Nalphabet["H"] = "11"
Nalphabet["I"] = "12"
Nalphabet["J"] = "13"
Nalphabet["K"] = "14"
Nalphabet["L"] = "15"
Nalphabet["M"] = "16"
Nalphabet["N"] = "17"
Nalphabet["O"] = "18"
Nalphabet["P"] = "19"
Nalphabet["Q"] = "20"
Nalphabet["R"] = "21"
Nalphabet["S"] = "22"
Nalphabet["T"] = "23"
Nalphabet["U"] = "24"
Nalphabet["V"] = "25"
Nalphabet["W"] = "26"
Nalphabet["X"] = "1"
Nalphabet["Y"] = "2"
Nalphabet["Z"] = "3"

NDalphabet = {}
NDalphabet["4"] = "A"
NDalphabet["5"] = "B"
NDalphabet["6"] = "C"
NDalphabet["7"] = "D"
NDalphabet["8"] = "E"
NDalphabet["9"] = "F"
NDalphabet["10"] = "G"
NDalphabet["11"] = "H"
NDalphabet["12"] = "I"
NDalphabet["13"] = "J"
NDalphabet["14"] = "K"
NDalphabet["15"] = "L"
NDalphabet["16"] = "M"
NDalphabet["17"] = "N"
NDalphabet["18"] = "O"
NDalphabet["19"] = "P"
NDalphabet["20"] = "Q"
NDalphabet["21"] = "R"
NDalphabet["22"] = "S"
NDalphabet["23"] = "T"
NDalphabet["24"] = "U"
NDalphabet["25"] = "V"
NDalphabet["26"] = "W"
NDalphabet["1"] = "X"
NDalphabet["2"] = "Y"
NDalphabet["3"] = "Z"

# -------------------------------------------------
# initializing some global variables
cipher = ""
answer = ''


"""make copy txt file into all caps and removing all non-letters"""
def fileFormat(txtFile):
    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ch = []
    # open the file to read
    openText = open(txtFile, 'r')
    # base case for non-numbers
    for l in openText:
        for c in l:
            # add letters into the list
            if c in key:
                ch.append(c.upper())
            # remove spaces and non-letters
            else:
                pass
            # make list of characters into a single string
    chString = ''.join(ch)
    openText.close()
    return chString


# -------------------------------------------------
"""make a new file for the encrypted/decrypted message"""
def makeFile(codeString):
    fw = open("aHW1testfile", "w+")
    fw.write(codeString)
    fw.close()
    return


# -------------------------------------------------
"""caesar encryption"""
def caesarEncrypt(fileString):
    newString = ""
    for c in fileString:
        newString += alphabet[c]
    makeFile(newString)
    return newString


"""caesar decryption"""
def caesarDecrypt(fileString):
    newString = ""
    for c in fileString:
        newString += Dalphabet[c]
    makeFile(newString)
    return newString


# -------------------------------------------------
"""simple substitution encryption"""
def simpleSubEncrypt(fileString):
    newString = ""
    for c in fileString:
        newString += Salphabet[c]
    makeFile(newString)
    return newString


"""simple substitution decryption"""
def simpleSubDecrypt(fileString):
    newString = ""
    for c in fileString:
        newString += SDalphabet[c]
    makeFile(newString)
    return newString


# -------------------------------------------------
"""polyalphabetical encryption"""
def polyAlphaEncrypt(fileString):
    newString = ""
    # counter to keep track of the alphabet being used
    counter = 0
    for c in fileString:
        if counter == 0:
            newString += alphabet[c]
            counter += 1
        elif counter == 1:
            newString += Salphabet[c]
            counter += 1
        elif counter == 2:
            newString += Palphabet[c]
            counter = 0
    makeFile(newString)
    return newString


"""polyalphabetical decryption"""
def polyAlphaDecrypt(fileString):
    newString = ""
    # counter to keep track of the alphabet being used
    counter = 0
    for c in fileString:
        if counter == 0:
            newString += Dalphabet[c]
            counter += 1
        elif counter == 1:
            newString += SDalphabet[c]
            counter += 1
        elif counter == 2:
            newString += PDalphabet[c]
            counter = 0
    makeFile(newString)
    return newString


# -------------------------------------------------
"""transpose encryption"""
def transposeEncryption(fileString):
    newString = ""
    for c in fileString:
        appendString = c + newString
        newString = appendString
    makeFile(newString)
    return newString


"""transpose decryption"""
def transposeDecryption(fileString):
    newString = ""
    for c in fileString:
        appendString = c + newString
        newString = appendString
    makeFile(newString)
    return newString


# -------------------------------------------------
"""caesar number encryption"""
def numberEncrypt(fileString):
    newString = ""
    for c in fileString:
        newString += " " + Nalphabet[c]
    makeFile(newString)
    return newString


"""caesar number decryption"""
def numberDecrypt(fileString):
    stringList = fileString.split()
    newString = ""
    for c in stringList:
        newString += NDalphabet[c]
    makeFile(newString)
    return newString


# -------------------------------------------------
"""main class for user interface. Calls most of the other functions"""
class readFile():
    # asking for which cipher will be used
    global cipher
    cipher = input("What cipher do you want to use: caesar, simpleSub, polyAlpha, transpose, number: ")

    # choose encrypting or decrypting
    global answer
    answer = input("encrypt of decrypt? (e/d): ")

    # asking for path to the txt file
    txtFile = fileFormat(input("Add path to file you would like to be encrypted/decrypted: "))

    """choosing which cipher is being used based on 'cipher' variable"""
    if cipher == "caesar":
        """Caesar cipher is credited to Julius Caesar (Serious Cryptography, pg 2)
        This cipher encrypts a document by shifting the letters down by 3, which
        nowadays isn't very difficult to decipher"""
        if answer == 'e':
            testString = caesarEncrypt(txtFile)
        else:
            caesarDecrypt(txtFile)
    elif cipher == "simpleSub":
        """Simple substitution cipher is a monoalphabetic cipher that, instead
         of shifting down a few letters, runs a scrambled alphabet with
         the same amount of letters as the regular one, each with a key to the
         original(Basic Cryptanalysis, ch3 sec1)
         This cipher scrambles a document by swapping letters around using the
         specific secondary alphabet used, which can changed from person to person."""
        if answer == 'e':
            testString = simpleSubEncrypt(txtFile)
        else:
            simpleSubDecrypt(txtFile)
    elif cipher == "polyAlpha":
        """The polyalphabetical cipher makes use of multiple alphabets set to
        different shifts in letters, and is also known as the Vigenere cipher,
        after the man who popularized it(Serious Crypography, pg 3)
        This cipher takes three separate alphabets with differents permutations
        and uses this to scramble a document even further than the Caesar cipher."""
        if answer == 'e':
            testString = polyAlphaEncrypt(txtFile)
        else:
            polyAlphaDecrypt(txtFile)
    elif cipher == "transpose":
        """Transposition cipher used to be popular but fell off as people
        became more learned and technology improved(Manual of Cryptography, chapter 3)
        This cipher doesn't change the letters or words, but instead shifts them
        around, making the original text unreadable, but keeping the letters in the
        actual document"""
        if answer == 'e':
            testString = transposeEncryption(txtFile)
        else:
            transposeDecryption(txtFile)
    elif cipher == "number":
        """This cipher was used by an Italian mob boss before he was caught by
        the police, showing that the cipher itself has become somewhat
        obsolete (Serious Cryptography, pg 2)"""
        if answer == 'e':
            testString = numberEncrypt(txtFile)
        else:
            numberDecrypt(txtFile)
