import os

import dotenv


def load_env_vars():
    """Load environment variables from .env file."""
    dotenv.load_dotenv()


def get_env_var(var_name, default=None):
    """Get a specified environment variable. Returns default if not found."""
    var = os.getenv(var_name, default)
    if var is None:
        raise ValueError(f"{var_name} not found in environment variables.")
    return var
