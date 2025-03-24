# CS4348 Project 1
Logan Margabandu
lmm220012


## Project Overview
This project consists of three separate programs that work together to `log`, `encrypt`, and `decrypt` messages. The programs communicate via pipes, and the entire system is controlled by the `driver program`.


## Files & Their Roles
| File           | Description |
|---------------|------------|
| `logger.py`   | Logs actions into a file (`test.log`). Receives log messages via standard input. |
| `encryption.py` | Encrypts and decrypts messages using the **Vigenère cipher**. Communicates via standard input/output. |
| `driver.py`   | Controls the encryption & logging programs, handles user input, and provides a **menu-driven interface**. |
| `README.md`   | This documentation file. |
| `test.log`    | The log file where all actions are recorded. **This file is generated at runtime.** |


## How to Compile & Run the Program
`python3 driver.py TheLogFile.log`
- you should be promoted with a **menu** of commands
**Menu Commands**:
Once running, the following commands are available:
`password` — Set the encryption passkey.
`encrypt` — Encrypt a string (choose from history or enter a new one).
`decrypt` — Decrypt a string (choose from history or enter a new one).
`history` — Show previously used input/output strings.
`quit` — Exit the program and stop all processes.

  All actions are logged in the `TheLogFile` log file!


### **Setup**
Before running the project, ensure you have **Python 3** installed.  
Also, install `pytz` for timezone handling:
```bash
pip3 install pytz
