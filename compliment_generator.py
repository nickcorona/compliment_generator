import random

import openai

from constants import OPENAI_API_KEY
from env_handler import get_env_var, load_env_vars

# load environment variables
load_env_vars()


# load OpenAI API key
openai.api_key = get_env_var(OPENAI_API_KEY)


def generate_compliment(name, adjectives, attributes):
    """Generate a compliment using OpenAI API."""
    attribute = random.choice(attributes)
    adjective = random.choice(adjectives)
    prompt = (
        f"Craft a compliment for {name}, highlighting their {adjective} {attribute}."
    )

    # load OpenAI API key
    openai.api_key = get_env_var(OPENAI_API_KEY)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=100,
    )

    return response.choices[0].text.strip()  # type: ignore
