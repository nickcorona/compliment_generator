import os

import dotenv


def load_env_vars():
    """Load environment variables from .env file."""
    dotenv.load_dotenv()


def get_env_var(var_name):
    """Get a specified environment variable."""
    var = os.getenv(var_name)
    if not var:
        raise ValueError(f"{var_name} not found in environment variables.")
    return var
