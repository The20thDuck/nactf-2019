import random
import sys
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890./-_=:"

#alphabet = [char for char in characters]
#shuffleAlphabet = alphabet.copy()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '/', '-', '_', '=', ':']
shuffleAlphabet = ['T', 'v', 'm', '9', 'M', 'j', '=', 'S', 'a', 'i', 'w', 'k', 'e', 'C', 'P', 'L', 'X', 'D', 'J', 'c', '8', 'h', 'f', '_', '.', 't', 'I', 'B', 'q', 'R', 'Q', 'Z', 'U', 'n', 'K', 'u', 'l', 'E', '-', '7', '6', 'g', 'N', 'p', '/', 's', 'Y', '3', ':', '4', 'o', 'A', 'x', 'H', 'G', '1', 'b', 'F', 'W', '2', 'z', 'r', 'y', 'd', 'O', 'V', '5', '0']
#random.shuffle(shuffleAlphabet)
#print (alphabet)
#print (shuffleAlphabet)
#link = "https://lh3.googleusercontent.com/m5JvOKXJ0-gTFuxHTojIVO7NEuoYkoKhMFAQfYvH1fDWMmdOW1Zqn8sllR597lL4YayTJwHWY_yz1UNPqw=w10-h10-rw"
'''
import csv
resultFile = open("table.csv",'w')
wr = csv.writer(resultFile)
wr.writerows([alphabet])
wr.writerows([shuffleAlphabet])
'''
if __name__ == "__main__":
    link = sys.argv[1]
    encryptedLink = ""

    for char in link:
        index = alphabet.index(char)
        encryptedLink += shuffleAlphabet[index]

    print (encryptedLink)

    decryptedLink = ""

    for char in link:
        index = shuffleAlphabet.index(char)
        decryptedLink += alphabet[index]

    print (decryptedLink)