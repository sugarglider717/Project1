#!/usr/bin/env python
import sys
import datetime
import pytz #for timezone

#log_message: log messages to a log file with timestamp, action, and message
def log_message(log_file, action, message):
    #current timestamp in YYYY-MM-DD HH:MM format with timezone handling
    timezone = pytz.timezone("America/Chicago")  # change to CST
    timestamp = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M") #timezone format
    
    #log entry as: YYYY-MM-DD HH:MM [ACTION] MESSAGE
    log_entry = f"{timestamp} [{action}] {message}\n"
    
    #open the log file in append mode and write the log entry
    with open(log_file, 'a') as f:
        f.write(log_entry)

#main: function where the logger listens for input
def main():
    #make sure that the user gives the logfile name as an argument 
    if len(sys.argv) != 2:
        print("Usage: python logger.py <logfile>")
        sys.exit(1)
    log_file = sys.argv[1]
    
    #keep reading input from stdin 
    while True:
        #read input and remove extra whitespace 
        log_input = sys.stdin.readline().strip()
        
        #if the command is 'QUIT' -> STOP
        if log_input == "QUIT":
            break
        
        #split the input into action and message (to help format)
        if log_input:
            parts = log_input.split(' ', 1)
            action = parts[0] #first word
            message = parts[1] if len(parts) > 1 else ""
            
            #log to log file
            log_message(log_file, action, message)

if __name__ == "__main__":
    main()
