import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_object_info(object_name):
    prompt = f"""
    You are an industrial maintenance assistant.

    Explain the industrial object "{object_name}" clearly.
    Include:
    - What it is
    - Where it is used
    - Common faults
    - Safety precautions

    Keep it concise and technician-friendly.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
