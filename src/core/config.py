import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(key: str, default: str = None, required: bool = False) -> str:
    """Get an environment variable or return a default value."""
    value = os.getenv(key, default)
    if required and value is None:
        raise ValueError(f"Environment variable '{key}' is required but not set.")
    return value

DATABASE_URL = get_env_variable("DATABASE_URL", required=True)
#BUCKET_NAME = get_env_variable("BUCKET_NAME", required=True)
#BUCKET_KEY = get_env_variable("BUCKET_KEY", required=True)