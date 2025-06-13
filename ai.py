import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

def call_ai_api(prompt):
    """
    Call the OpenRouter AI API to get a response for the given prompt.
    
    Args:
        prompt (str): The prompt to send to the AI model.
        
    Returns:
        str: The AI's response.
        
    Raises:
        ValueError: If OPENROUTER_API_KEY is not set in the environment.
        Exception: For other errors during the API call.
    """
    if not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY is not set in the environment.")

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an expert summarizer. Summarize the user's note in 2-3 sentences. "
                    "Only return the summary, not the original text."
                )
            },
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("API Error:", response.text)  # This will show the real error in your terminal
        raise
    result = response.json()
    return result["choices"][0]["message"]["content"]

# Example usage
if __name__ == "__main__":
    print("API KEY:", OPENROUTER_API_KEY)