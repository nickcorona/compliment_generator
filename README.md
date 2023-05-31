# Compliment Generator

A Python application that generates a personalized compliment for a specific person and sends it via email. It is designed to be scheduled to run at a random time each day.

## How to Use

1. Clone this repository.
2. Install the required dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file to store your environment variables (email details, OpenAI API key, recipient's email, and name).
4. Run the script manually to test it: `python main.py`.

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
   `* * * * * /usr/bin/python3 /path/to/your/script/main.py >> /path/to/your/logfile.log 2>&1`  
   This will run the script every minute. Adjust the time according to your needs. The output will be logged to the specified log file.
4. Save and close the file.

Please note that the frequency and exact timing will depend on the specific configuration of your cron file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.