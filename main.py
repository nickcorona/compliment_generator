import logging
import os
import random
import smtplib
from datetime import date, datetime, time, timedelta
from random import randint
from time import sleep

import dotenv
import openai

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# List of attributes for personalized compliments
attributes = [
    "kindness",
    "intelligence",
    "creativity",
    "courage",
    "positivity",
    "determination",
    "patience",
    "humor",
    "passion",
    "sensitivity",
    "empathy",
    "adventurous",
    "resilience",
    "generosity",
    "ambition",
    "grace",
    "charm",
    "confidence",
    "humility",
    "integrity",
    "honesty",
    "perseverance",
    "respectfulness",
    "responsibility",
    "sincerity",
    "sympathy",
    "tolerance",
    "wit",
    "adaptability",
    "compassion",
    "devotion",
    "discipline",
    "enthusiasm",
    "forgiveness",
    "loyalty",
    "optimism",
    "spirituality",
    "thoughtfulness",
    "wisdom",
    "elegance",
    "insightfulness",
    "modesty",
    "motivation",
    "originality",
    "resourcefulness",
    "spontaneity",
]


def load_env_vars():
    """Load environment variables from .env file."""
    dotenv.load_dotenv()


def get_env_var(var_name):
    """Get a specified environment variable."""
    var = os.getenv(var_name)
    if not var:
        raise ValueError(f"{var_name} not found in environment variables.")
    return var


def generate_compliment(name):
    """Generate a compliment using OpenAI API."""
    openai.api_key = get_env_var("OPENAI_API_KEY")

    attribute = random.choice(attributes)
    prompt = (
        f"Craft a personalized compliment for {name}, highlighting their {attribute}."
    )

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.9,
        max_tokens=100,
    )

    return response.choices[0].text.strip()  # type: ignore


def send_email(to_email, subject, body):
    """Send an email using SMTP."""
    email = get_env_var("EMAIL_ADDRESS")
    password = get_env_var("EMAIL_PASSWORD")
    smtp_server = get_env_var("SMTP_SERVER")
    smtp_port = int(get_env_var("SMTP_PORT"))  # convert to int

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email, password)
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(email, to_email, msg)


def send_compliment(to_email, name):
    """Generate a compliment and send it via email."""
    try:
        compliment = generate_compliment(name)
        subject = "Your Daily Compliment!"
        body = compliment
        send_email(to_email, subject, body)
        logging.info(f"Compliment sent to {to_email} at {datetime.now()}")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise


if __name__ == "__main__":
    load_env_vars()
    to_email = get_env_var("TO_EMAIL")
    name = get_env_var("NAME")

    current_time = datetime.now().time()

    if current_time < time(7, 0):
        delay = (
            datetime.combine(date.today(), time(7, 0))
            - datetime.combine(date.today(), current_time)
        ).total_seconds()
    else:
        delay = 0

    random_seconds = randint(0, 15 * 60 * 60)  # 15 hours = 15*60*60 seconds
    sleep_seconds = delay + random_seconds

    wake_up_time = datetime.now() + timedelta(seconds=sleep_seconds)

    logging.info(
        f"Sleeping for {sleep_seconds} seconds. Will wake up at {wake_up_time}"
    )

    sleep(sleep_seconds)
    send_compliment(to_email, name)
