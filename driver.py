#!/usr/bin/env python3
import sys
import subprocess

def main(log_file):
    logger = subprocess.Popen(["python3", "logger.py", log_file], stdin=subprocess.PIPE, text=True)
    encryptor = subprocess.Popen(["python3", "encryption.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    def log(action, message):
        logger.stdin.write(f"{action} {message}\n")
        logger.stdin.flush()

    log("START", "Driver started.")
    history = []

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
            if history:
                print("Choose a string from history or enter a new string:")
                for i, item in enumerate(history, start=1):
                    print(f"{i}. {item}")
                choice = input("Enter choice (number or new string): ").strip()
                if choice.isdigit():
                    index = int(choice) - 1
                    if 0 <= index < len(history):
                        text = history[index]
                    else:
                        print("Invalid selection.")
                        continue
                else:
                    text = choice.upper()
                    if not text.isalpha():
                        print("ERROR Only letters allowed")
                        continue
                    history.append(text)
            else:
                text = input("Enter text to encrypt: ").strip().upper()
                if not text.isalpha():
                    print("ERROR Only letters allowed")
                    continue
                history.append(text)

            encryptor.stdin.write(f"ENCRYPT {text}\n")
            encryptor.stdin.flush()
            response = encryptor.stdout.readline().strip()
            log("ENCRYPT", response)
            print(response)

            if response.startswith("RESULT "):
                result = response.split(" ", 1)[1]
                history.append(result)

        elif command == "decrypt":
            if history:
                print("Choose a string from history or enter a new string:")
                for i, item in enumerate(history, start=1):
                    print(f"{i}. {item}")
                choice = input("Enter choice (number or new string): ").strip()
                if choice.isdigit():
                    index = int(choice) - 1
                    if 0 <= index < len(history):
                        text = history[index]
                    else:
                        print("Invalid selection.")
                        continue
                else:
                    text = choice.upper()
                    if not text.isalpha():
                        print("ERROR Only letters allowed")
                        continue
                    history.append(text)
            else:
                text = input("Enter text to decrypt: ").strip().upper()
                if not text.isalpha():
                    print("ERROR Only letters allowed")
                    continue
                history.append(text)

            encryptor.stdin.write(f"DECRYPT {text}\n")
            encryptor.stdin.flush()
            response = encryptor.stdout.readline().strip()
            log("DECRYPT", response)
            print(response)

            if response.startswith("RESULT "):
                result = response.split(" ", 1)[1]
                history.append(result)

        elif command == "history":
            print("Encryption History:")
            for i, item in enumerate(history, start=1):
                print(f"{i}. {item}")

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
