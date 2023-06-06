import random

import openai

# adjectives for compliments
adjectives = [
    "lovely",
    "wonderful",
    "amazing",
    "awesome",
    "fantastic",
    "great",
    "superb",
    "excellent",
    "incredible",
    "fabulous",
    "terrific",
    "outstanding",
    "spectacular",
    "stunning",
    "marvelous",
    "magnificent",
    "brilliant",
    "exceptional",
    "perfect",
    "splendid",
    "glorious",
    "super",
    "tremendous",
    "phenomenal",
    "remarkable",
    "extraordinary",
    "mind-blowing",
    "mind-boggling",
    "jaw-dropping",
    "breathtaking",
    "miraculous",
    "astounding",
]


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
    "beautiful",
    "pretty",
    "amazing",
    "cute",
    "gorgeous",
    "lovely",
]


def generate_compliment(name):
    """Generate a compliment using OpenAI API."""
    attribute = random.choice(attributes)
    adjective = random.choice(adjectives)
    prompt = (
        f"Craft a compliment for {name}, highlighting their {adjective} {attribute}."
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=100,
    )

    return response.choices[0].text.strip()  # type: ignore
