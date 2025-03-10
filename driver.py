#!/usr/bin/env python3
import sys
import subprocess

def main(log_file):
    # Start the logger and encryption programs
    logger = subprocess.Popen(["python3", "logger.py", log_file], stdin=subprocess.PIPE, text=True)
    encryptor = subprocess.Popen(["python3", "encryption.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    # Function to log messages
    def log(action, message):
        logger.stdin.write(f"{action} {message}\n")
        logger.stdin.flush()

    log("START", "Driver started.")
    history = []
    key = None  # Passkey storage

    while True:
        print("\nCommands: password, encrypt, decrypt, history, quit")
        command = input("Enter command: ").strip().lower()

        if command == "password":
            key = input("Enter password: ").strip().upper()
            encryptor.stdin.write(f"PASS {key}\n")
            encryptor.stdin.flush()
            response = encryptor.stdout.readline().strip()
            log("PASSWORD", "Password set")
            print(response)

        elif command == "encrypt":
            text = input("Enter text to encrypt: ").strip().upper()
            if not text.isalpha():
                print("ERROR Only letters allowed")
                continue
            encryptor.stdin.write(f"ENCRYPT {text}\n")
            encryptor.stdin.flush()
            response = encryptor.stdout.readline().strip()
            log("ENCRYPT", response)
            print(response)
            history.append(response.split(" ", 1)[1])  # Store encrypted text in history

        elif command == "decrypt":
            text = input("Enter text to decrypt: ").strip().upper()
            encryptor.stdin.write(f"DECRYPT {text}\n")
            encryptor.stdin.flush()
            response = encryptor.stdout.readline().strip()
            log("DECRYPT", response)
            print(response)

        elif command == "history":
            print("Encryption History:", history)

        elif command == "quit":
            log("QUIT", "Driver shutting down.")
            encryptor.stdin.write("QUIT\n")
            encryptor.stdin.flush()
            logger.stdin.write("QUIT\n")
            logger.stdin.flush()
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <logfile>")
        sys.exit(1)
    main(sys.argv[1])
