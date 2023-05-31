import smtplib
import openai
import os
import dotenv


def load_env_vars():
    """Load environment variables from .env file."""
    dotenv.load_dotenv()


def get_email_credentials():
    """Get email credentials from environment variables."""
    email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    if not email or not password:
        raise ValueError(
            "Email address or password not found in environment variables."
        )
    return email, password


def get_openai_api_key():
    """Get OpenAI API key from environment variables."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not found in environment variables.")
    return api_key


def generate_compliment(name):
    """Generate a compliment using OpenAI API."""
    openai.api_key = get_openai_api_key()
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Write a creative and heartwarming compliment including their name, {name}.",
        temperature=0.7,
        max_tokens=60,
    )
    return response.choices[0].text.strip()  # type: ignore


def send_email(to_email, subject, body):
    """Send an email using SMTP."""
    email, password = get_email_credentials()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(email, to_email, msg)
    server.quit()


def send_compliment(to_email, name):
    """Generate a compliment and send it via email."""
    compliment = generate_compliment(name)
    subject = "Your Daily Compliment!"
    body = compliment
    send_email(to_email, subject, body)


if __name__ == "__main__":
    load_env_vars()
    to_email = "nicklucianocorona@gmail.com"
    name = "Jessica"
    send_compliment(to_email, name)
