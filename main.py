import smtplib
import openai
import os
import dotenv

# load the environment variables
dotenv.load_dotenv()

# your email credentials
email = "nicklucianocorona@gmail.com"
password = "bintmepakbdjbwei"

# recipient's email
to_email = "jessicasarah.christian@gmail.com"
to_email = email

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


# function to generate compliment
def generate_compliment():
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a creative and heartwarming compliment",
        temperature=0.7,
        max_tokens=60,
    )

    # access the text attribute of the first item in the choices list
    return response.choices[0].text.strip()  # type: ignore


# function to send email
def send_compliment():
    # generate a compliment
    compliment = generate_compliment()

    # establish a secure session
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # login to your email
    server.login(email, password)

    # compose the email
    subject = "Your Daily Compliment!"
    body = compliment
    msg = f"Subject: {subject}\n\n{body}"

    # send the email
    server.sendmail(email, to_email, msg)

    # logout from your email
    server.quit()


# send the compliment
send_compliment()
