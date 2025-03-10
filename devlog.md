# Devlog

Logan Margabandu
lmm220012

## 2025-03-10 10:00 AM  
### Thoughts So Far  
I have read the project instructions and understand that I need to implement three separate programs:  
1. **Logger** – Responsible for logging actions with timestamps.  
2. **Encryption Program** – Uses the Vigenère cipher to encrypt and decrypt messages.  
3. **Driver** – Handles user input, launches the other two programs, and manages communication via pipes.  

I plan to implement the programs in Python using the `subprocess` module for inter-process communication.

### Plan for This Session  
- Set up a new Git repository and initialize a `devlog.md` file.  
- Write an initial commit.  
- Implement the basic structure of the **logger program** to handle writing log messages to a file.  

### Session Progress  
- Created the Git repository and added `devlog.md`.  
-  Wrote the initial commit.  
-  Implemented the `logger.py` script to write log messages to a file in the correct format.  
-  Committed `logger.py` to Git.  

### Problems Encountered  
- Had to decide how to format log messages properly. Used `[ACTION] MESSAGE` format with timestamps.  
- Had a small issue where `input()` would cause errors if blank lines were entered. Fixed it by using `.strip()` before processing.  

### Next Steps  
- Implement the **encryption program**, ensuring it properly handles Vigenère cipher encryption/decryption.  
- Ensure the encryption program properly processes `PASS`, `ENCRYPT`, `DECRYPT`, and `QUIT` commands.  


