import json
import logging
import os
import time as time_module
from datetime import date, datetime, time, timedelta
from random import randint
from time import sleep

from compliment_generator import generate_compliment
from constants import NAME, TO_EMAIL
from utils.email_sender import send_email
from utils.env_handler import get_env_var, load_env_vars

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")


# Configure logging to write messages to a file with a timestamp in the filename
log_filename = f"logs/app_{int(time_module.time())}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def load_config():
    """Load configuration from config.json."""
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, "..", "data", "config.json"), "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Configuration file not found.")
    except json.JSONDecodeError:
        raise Exception("Configuration file is not properly formatted.")
    return config


def calculate_delay(config):
    """Calculate the delay based on the current time and the start time."""
    current_time = datetime.now().time()
    start_time = time(config["start_hour"], 0)

    if current_time < start_time:
        delay = (
            datetime.combine(date.today(), start_time)
            - datetime.combine(date.today(), current_time)
        ).total_seconds()
    else:
        delay = 0
    return delay


def calculate_sleep_time(config):
    """Calculate the sleep time based on the delay and the desired window."""
    delay = calculate_delay(config)
    random_seconds = randint(0, config["sleep_window_seconds"])
    sleep_seconds = delay + random_seconds
    return sleep_seconds


def send_compliment(to_email, name, adjectives, attributes):
    """Generate a compliment and send it via email."""
    try:
        compliment = generate_compliment(name, adjectives, attributes)
        subject = "Your Daily Compliment!"
        body = compliment
        send_email(to_email, subject, body)
        logging.info(f"Compliment sent to {to_email} at {datetime.now()}")
    except Exception as e:
        logging.exception(f"Error occurred while sending compliment: {str(e)}")


if __name__ == "__main__":
    # Load environment variables
    load_env_vars()

    to_email = get_env_var(TO_EMAIL)
    name = get_env_var(NAME)

    # Load configuration
    config = load_config()

    sleep_seconds = calculate_sleep_time(config)
    wake_up_time = datetime.now() + timedelta(seconds=sleep_seconds)

    logging.info(
        f"Sleeping for {sleep_seconds/3600:.2f} hours. Will wake up at {wake_up_time}"
    )

    sleep(sleep_seconds)
    send_compliment(to_email, name, config["adjectives"], config["attributes"])
