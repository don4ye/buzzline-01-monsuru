"""
basic_consumer_prince.py

Read a log file as it is being written, with prince's unique alerts.
"""

#####################################
# Import Modules
#####################################

import os
import time
from utils.utils_logger import logger, get_log_file_path

#####################################
# Define a function to process a single message
#####################################


def process_message(log_file) -> None:
    """
    Read a log file and process each message.

    Args:
        log_file (str): The path to the log file to read.
    """
    with open(log_file, "r") as file:
        # Move to the end of the file
        file.seek(0, os.SEEK_END)
        print("Consumer prince is ready and waiting for a new log message...")

        # Use while True loop so the consumer keeps running forever
        while True:
            # Read the next line of the file
            line = file.readline()

            # If the line is empty, wait for a new log entry
            if not line:
                # Wait a second for a new log entry
                delay_seconds = 1
                time.sleep(delay_seconds)
                continue

            # We got a new log entry!
            # Remove any leading/trailing white space and log the message
            message = line.strip()
            print(f"Consumed log message: {message}")

            # Monitor and alert on prince's special conditions
            if "I just explored a travel destination! It was mind-blowing." in message:
                print(f"ALERT: Prince's special message was found! \n{message}")
                logger.warning(f"ALERT: Prince's special message was found! \n{message}")

            if "I just enjoyed a mystery book! It was incredible." in message:
                print(f"ALERT: Another amazing message spotted! \n{message}")
                logger.info(f"ALERT: Another amazing message spotted! \n{message}")


#####################################
# Define main function for this script.
#####################################


def main() -> None:
    """Main entry point."""
    logger.info("START prince's consumer...")

    # Call the function to get the path to the log file
    log_file_path = get_log_file_path()
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        # Try to call the process_message function
        process_message(log_file_path)

    except KeyboardInterrupt:
        print("User stopped the process.")

    logger.info("END prince's consumer...")


#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    main()
