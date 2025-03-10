#!/usr/bin/env python
import sys

#vigenere_encrypt: helper function to encrypt text using the Vigenere cipher
def vigenere_encrypt(text, key):
    encrypted = [] #stores the encrypted characters 
    key_length = len(key) #length of passkey 
    #convert passkey and text into ASCII integer values 
    key_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    #go through each char in the text and apply the Vigenere cipher formula 
    for i in range(len(text_int)):
        value = (text_int[i] + key_int[i % key_length]) % 26 #shift the char by the corresponding char in the passkey 
        encrypted.append(chr(value + 65))  #append the encrypted character to the list by starting w A (ASCII 65)
    #return the encrypted text as a string 
    return ''.join(encrypted)

#vigenere_decrypt: helper function to decrypt text using the Vigenere cipher, same logic as vigenere_encrypt
def vigenere_decrypt(text, key):
    decrypted = []
    key_length = len(key)
    key_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    for i in range(len(text_int)):
        value = (text_int[i] - key_int[i % key_length]) % 26
        decrypted.append(chr(value + 65))  # 'A' = 65 in ASCII
    return ''.join(decrypted)

#main: function to handle commands for the encryption and decryption program
def main():
    #set the passkey variable (none at first)
    passkey = None

    while True:
        #read the command from standard input
        command = sys.stdin.readline().strip()
        #split the input into command and argument
        parts = command.split(' ', 1)
        cmd = parts[0].upper()  # command part
        arg = parts[1] if len(parts) > 1 else ""  # argument part
        
        #if the command is 'QUIT', stop the program
        if cmd == "QUIT":
            break
        #set the passkey for encryption/decryption
        elif cmd == "PASSKEY":
            #if an argument is provided, set the passkey
            if arg:
                passkey = arg.upper()
                print("RESULT Passkey set.") #confirmation to log later
                sys.stdout.flush()  #flush to ensure driver receives output
            else:
                print("ERROR Passkey not provided.") #error to log later 
                sys.stdout.flush()  
        #command to encrypt the given text using the passkey
        elif cmd == "ENCRYPT":
            #make sure that passkey is set 
            if not passkey:
                print("ERROR Password not set.")
                sys.stdout.flush()  
            elif arg:
                #encrypt the provided text using the passkey
                encrypted = vigenere_encrypt(arg.upper(), passkey)
                print(f"RESULT {encrypted}")
                sys.stdout.flush()  
            else:
                print("ERROR Text to encrypt not provided.")
                sys.stdout.flush()  
        #command to decrypt the given text using the passkey
        elif cmd == "DECRYPT":
            #make sure that passkey is set 
            if not passkey:
                print("ERROR Password not set.")
                sys.stdout.flush()  
            elif arg:
                #decrypt the provided text using the passkey
                decrypted = vigenere_decrypt(arg.upper(), passkey)
                print(f"RESULT {decrypted}")
                sys.stdout.flush()  
            else:
                print("ERROR Text to decrypt not provided.")
                sys.stdout.flush()  
        #if command is just Invalid
        else:
            print("ERROR Invalid command.")
            sys.stdout.flush()  

if __name__ == "__main__":
    main()
