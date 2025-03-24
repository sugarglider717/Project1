# Devlog

Logan Margabandu
lmm220012
CS 4348.501

## 2025-03-10 10:00 AM  
### Thoughts So Far  
I have read the project instructions and understand that I need to implement three separate programs:  
1. **Logger** – Responsible for logging actions with timestamps.  
2. **Encryption Program** – Uses the Vigenère cipher to encrypt and decrypt messages.  
3. **Driver** – Handles user input, launches the other two programs, and manages communication via pipes.
- not confident on what the process files are for in the assignment instructions, im assuming those are for reference ~

I plan to implement the programs in Python using the `subprocess` module for inter-process communication.

### Plan for This Session  
- Set up a new Git repository and initialize a `devlog.md` file.  
- Write an initial commit.  
- Implement the basic structure of the **logger program** to handle writing log messages to a file.
- Implement the basic structure of the **encryption program** to encrypt and decrpt messages.
- Implement the basic structure of the **driver program** to take in what the user types and run the other two programs

### Session Progress  
- Created the Git repository and added `devlog.md`.  
-  Wrote the initial commit.  
-  Implemented the `logger.py` script to write log messages to a file in the correct format.  
-  Committed `logger.py` to Git.
-  Implemented the `encryption.py` script to uses the Vigenère cipher to encrypt and decrypt messages.
-  Committed the `encryption.py` to Git.
-  Implemented the `driver.py` script to handle user input, launch the other two programs, and manage communication via pipes.
-  Commited the `driver.py` to Git. 
  
### Problems Encountered  
- Had to decide how to format log messages properly. Used `[ACTION] MESSAGE` format with timestamps.  
- Had a small issue where `input()` would cause errors if blank lines were entered. Fixed it by using `.strip()` before processing.
- issue with the encryption program properly processes `PASS`, `ENCRYPT`, `DECRYPT`, and `QUIT` commands.  
 

### Next Steps  
- Make sure everything is good to go before submitting and finish the very last bit of the project (error handling)

## 2025-03-21 9:00 AM
### Plans For This Session
- Going to finish the very last bit of the project (error handling and whatnot), but I essentially just finished it in one very long session.
- Going to make sure all submission guidlines are followed to ensure maximum score
- update devlog (currently doing)
- commit all changes and make sure that's reflected on Github
### Encountered any issues?
- the driver program is creating a new log file instead of writing to the existing `TheLogFile.log` :(
- i believe the history is not displaying as a menu with numerics to select from :(

### Session Progress
- Fixed issue where the driver program was creating a new log file instead of writing to the existing `TheLogFile.log`
- Fixed issue where the input strings were not being saved in the history and could not retrieve it.
  


