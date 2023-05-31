# Compliment Generator

A Python application that generates a personalized compliment for a specific person and sends it via email. It is designed to be scheduled to run at a random time each day.

## How to Use

1. Clone this repository.
2. Install the required dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file to store your environment variables (email details, OpenAI API key, recipient's email, and name).
4. Run the script manually to test it: `python main.py`.

## Environment Variables

This project requires certain environment variables to be set in a `.env` file in the root directory of the project. These are:

- `OPENAI_API_KEY`: Your OpenAI API key. Used for generating the compliment.
- `EMAIL_PASSWORD`: The password for the email account you're using to send the email.
- `EMAIL_ADDRESS`: The email address you're using to send the email.
- `SMTP_SERVER`: The SMTP server for your email provider (for example, for Gmail it's `smtp.gmail.com`).
- `SMTP_PORT`: The SMTP port for your email provider (for Gmail, use `587` with TLS).
- `TO_EMAIL`: The recipient's email address. This is where the compliment will be sent.
- `NAME`: The name of the recipient. This will be used to personalize the compliment.

Please do not commit your `.env` file to the repository. This file should be kept private as it contains sensitive information.

Here's an example of what your `.env` file should look like:

```bash
OPENAI_API_KEY=your-openai-api-key
EMAIL_PASSWORD=your-email-password
EMAIL_ADDRESS=your-email-address@example.com
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
TO_EMAIL=recipient-email@example.com
NAME=RecipientName
```

Please replace the values above with your actual information.

## Scheduling the Task

You can schedule the script to run daily at a random time using either the Windows Task Scheduler or a cron job in Linux.

### Windows

Follow these steps to schedule the task with Task Scheduler:

1. Open the Task Scheduler application.
2. Click on `Create Basic Task`.
3. Name the task and set the trigger to `Daily`.
4. In the `Action` step, select `Start a program` and browse to the Python executable file (usually located in your Python installation directory) and add the path to `main.py` script in the `Add arguments` section.
5. Finish the setup.

You might need to adjust these steps based on your specific version of Windows.

### Linux

To schedule the script to run daily with cron, follow these steps:

1. Open your terminal.
2. Type `crontab -e` to edit the cron file.
3. Add a new line in the following format:  
   `0 7 * * * /usr/bin/python3 /path/to/your/script/main.py >> /path/to/your/logfile.log 2>&1`  
   This will run the script daily at 7:00 AM. Adjust the time according to your needs. The output will be logged to the specified log file.
4. Save and close the file.

Please note that the frequency and exact timing will depend on the specific configuration of your cron file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.