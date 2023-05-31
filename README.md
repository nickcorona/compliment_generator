# Compliment Generator

Compliment Generator is a Python project that generates personalized compliments and sends them via email at a random time between 7:00 AM and 10:00 PM.

## Getting Started

### Prerequisites

The project requires the following software:

- Python 3.8 or higher
- `openai` Python library for generating compliments
- `python-dotenv` for environment variable handling

The project also needs an OpenAI API key to generate the compliments.

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/nickcorona/ComplimentGenerator.git
   ```

2. Install the required Python packages:
   ```sh
   pip install openai python-dotenv
   ```

3. Create a `.env` file in the project root directory and set the following variables:
   - `OPENAI_API_KEY`: your OpenAI API key
   - `EMAIL_ADDRESS`: the email address from which to send the compliments
   - `EMAIL_PASSWORD`: the password for the email address
   - `SMTP_SERVER`: the SMTP server for the email provider
   - `SMTP_PORT`: the SMTP port for the email provider
   - `TO_EMAIL`: the recipient's email address
   - `NAME`: the name of the recipient

## Usage

To run the script:
```sh
python main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
