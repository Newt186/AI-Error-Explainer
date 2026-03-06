# AI Error Explainer
import requests


def get_error():
    error = input("Enter the error you are getting: ")
    return error


def build_prompt(error):

    prompt = f"""
Explain the programming error below.

Provide the following:

1. Programming language
2. What the error means
3. Why it happens
4. Example mistake
5. How to fix it
6. Correct code example

Error:
{error}
"""

    return prompt


def ask_ai(prompt):

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        return data["response"]

    except:
        return "Error: Could not connect to Ollama. Make sure it is running."


# Program flow
error = get_error()

prompt = build_prompt(error)

ai_response = ask_ai(prompt)

print("\nAI Error Explanation:\n")
print(ai_response)