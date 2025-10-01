# chatbot/config.py

"""
Module for centralizing configuration and environment variable management.
Ensures sensitive information (like API keys) is loaded securely and that project
paths (e.g., logging directories) are consistently initialized.

Design:
- Loads environment variables from a .env file for development flexibility (using python-dotenv).
- Raises a clear runtime error if required secrets are missing.
- Prepares required directories (e.g., for log files) at module import time.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Define the path to the .env file (project root).
dotenv_path = Path('.') / '.env'

# Conditionally load environment variables from .env if the file exists.
# This is useful for local development and testing; production can rely on real env vars.
if dotenv_path.exists():
    load_dotenv(dotenv_path)

# Attempt to retrieve the OpenAI API key from environment variables.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    # Fail-fast: catch missing API key at startup for safer debugging and security.
    raise RuntimeError("OPENAI_API_KEY not found. Add it to .env or set environment variable.")

# Directory path for persistent log file storage.
LOGS_DIR = Path("logs")
# Create logs/ if it does not already exist - preparing for downstream logging utilities.
LOGS_DIR.mkdir(exist_ok=True)

# Reason: By centralizing secrets/config in this module, all other code like  API clients
# can import from here without repeating env-handling logic.
