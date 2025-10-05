
"""
OpenAI client wrapper: single responsibility, easy to unit test.
Uses the official OpenAI Python client and adds simple retry logic.
"""
from typing import List, Dict
import time
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
from openai import OpenAI
from . import config



# Create a single client instance reading key from config
# Official recommended usage is to instantiate OpenAI() which will use OPENAI_API_KEY env var if provided.

client = OpenAI(api_key=config.OPENAI_API_KEY)

@retry(wait=wait_exponential(multiplier=1, min=1, max=10), stop=stop_after_attempt(4), retry=retry_if_exception_type(Exception))
def chat_with_model(messages: List[Dict[str, str]], model: str = "gpt-4o-mini", temperature: float = 0.7, max_tokens: int = 512) -> str:
    """
    Send messages (list of role/content dicts) and return assistant text.
    This uses the Chat Completions API pattern via the client.chat.completions.create() wrapper.
    """
    # messages is expected: [{"role":"system","content":"..."}, {"role":"user","content":"..."}, ...]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    # Navigate response safely
    try:
        return response.choices[0].message.content
    except Exception as e:
        # Raise to trigger tenacity retry if transient
        raise RuntimeError("Malformed response from OpenAI API") from e
