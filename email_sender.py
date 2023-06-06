import smtplib

from constants import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_PORT, SMTP_SERVER
from env_handler import get_env_var


def send_email(to_email, subject, body):
    """Send an email using SMTP."""
    with smtplib.SMTP(get_env_var(SMTP_SERVER), int(get_env_var(SMTP_PORT))) as server:
        server.starttls()
        server.login(get_env_var(EMAIL_ADDRESS), get_env_var(EMAIL_PASSWORD))
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(get_env_var(EMAIL_ADDRESS), to_email, msg)
