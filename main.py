import json
import logging
from datetime import date, datetime, time, timedelta
from random import randint
from time import sleep

from compliment_generator import generate_compliment
from constants import NAME, TO_EMAIL
from email_sender import send_email
from env_handler import get_env_var, load_env_vars

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_config():
    """Load configuration from config.json."""
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Configuration file not found.")
    except json.JSONDecodeError:
        raise Exception("Configuration file is not properly formatted.")
    return config


def calculate_sleep_time(config):
    """Calculate the sleep time based on the current time and the desired window."""
    current_time = datetime.now().time()
    random_seconds = randint(0, config["sleep_window_seconds"])

    if current_time < time(7, 0):
        delay = (
            datetime.combine(date.today(), time(7, 0))
            - datetime.combine(date.today(), current_time)
        ).total_seconds()
    else:
        delay = 0

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
        logging.exception(
            "Error occurred while sending compliment."
        )  # includes traceback


if __name__ == "__main__":
    load_env_vars()

    to_email = get_env_var(TO_EMAIL)
    name = get_env_var(NAME)

    # Load configuration
    config = load_config()

    sleep_seconds = calculate_sleep_time(config)
    wake_up_time = datetime.now() + timedelta(seconds=sleep_seconds)

    logging.info(
        f"Sleeping for {sleep_seconds} seconds. Will wake up at {wake_up_time}"
    )

    sleep(sleep_seconds)
    send_compliment(to_email, name, config["adjectives"], config["attributes"])
