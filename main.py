import smtplib
import openai
import os
import dotenv
import logging
import random

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# List of attributes for Jessica
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

    # Select a random attribute
    attribute = random.choice(attributes)
    prompt = (
        f"Craft a personalized compliment for {name}, highlighting their {attribute}."
    )

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.7,
            max_tokens=100,
        )
    except Exception as e:
        logging.error(f"Error when calling OpenAI API: {e}")
        raise

    return response.choices[0].text.strip()  # type: ignore


def send_email(to_email, subject, body):
    """Send an email using SMTP."""
    email = get_env_var("EMAIL_ADDRESS")
    password = get_env_var("EMAIL_PASSWORD")
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email, password)
            msg = f"Subject: {subject}\n\n{body}"
            server.sendmail(email, to_email, msg)
    except Exception as e:
        logging.error(f"Error when sending email: {e}")
        raise


def send_compliment(to_email, name):
    """Generate a compliment and send it via email."""
    compliment = generate_compliment(name)
    subject = "Your Daily Compliment!"
    body = compliment
    send_email(to_email, subject, body)


if __name__ == "__main__":
    load_env_vars()
    to_email = "jessicasarah.christian@gmail.com"
    name = "Jessica"
    send_compliment(to_email, name)
