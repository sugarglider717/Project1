# CS4348 Project 1
Logan Margabandu
lmm220012

This project and its Git log are viewable at `https://github.com/sugarglider717/Project1` ~~

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
- `password` — Set the encryption passkey.
<img width="400" alt="image" src="https://github.com/user-attachments/assets/fc574899-5735-445d-8e0d-afcc74f72e28" />



- `encrypt` — Encrypt a string (choose from history or enter a new one).
<img width="421" alt="image" src="https://github.com/user-attachments/assets/ed507619-5e7d-43eb-9368-4bbc665635ee" />

- `decrypt` — Decrypt a string (choose from history or enter a new one).
<img width="393" alt="image" src="https://github.com/user-attachments/assets/de627b6a-0ca6-4c36-817f-27141902cf8f" />

- `history` — Show previously used input/output strings.
<img width="390" alt="image" src="https://github.com/user-attachments/assets/d2536765-0011-4f6a-9e84-a2f819ae5475" />

- `quit` — Exit the program and stop all processes.
<img width="372" alt="image" src="https://github.com/user-attachments/assets/7b15d22f-975e-4f35-b009-c029840b9860" />

<img width="369" alt="image" src="https://github.com/user-attachments/assets/8ddd423f-44f9-4c58-a08a-684f3cf27e5d" />


All actions are logged in the `TheLogFile` log file!  
<img width="439" alt="image" src="https://github.com/user-attachments/assets/bf3549b7-fe25-4b89-93d2-4cc1c7923808" />


### **Setup**
Before running the project, ensure you have **Python 3** installed.  
Also, install `pytz` for timezone handling:
```bash
pip3 install pytz
