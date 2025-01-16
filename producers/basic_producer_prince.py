"""
basic_producer_prince.py

Generate some streaming buzz messages with a unique twist.
"""

import os
import random
import time
from dotenv import load_dotenv
from utils.utils_logger import logger

# Load environment variables from .env
load_dotenv()

def get_message_interval() -> int:
    """
    Fetch message interval from environment or use a default value.
    """
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval

# Define custom lists for generating unique buzz messages
ADJECTIVES: list = ["incredible", "unbelievable", "mind-blowing", "fantastic", "peculiar"]
ACTIONS: list = ["experienced", "discovered", "explored", "created", "enjoyed"]
TOPICS: list = ["a recipe", "a workout routine", "a travel destination", "a coding trick", "a mystery book"]

def generate_messages():
    """
    Generate a stream of custom buzz messages.
    """
    while True:
        adjective = random.choice(ADJECTIVES)
        action = random.choice(ACTIONS)
        topic = random.choice(TOPICS)
        yield f"I just {action} {topic}! It was {adjective}."

def main() -> None:
    """
    Main entry point for this producer.
    """
    logger.info("START prince's producer...")
    logger.info("Custom producer in action! Generating unique messages.")
    
    interval_secs: int = get_message_interval()

    for message in generate_messages():
        logger.info(message)
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END producer...")

if __name__ == "__main__":
    main()
