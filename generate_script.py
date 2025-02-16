import openai

# Set your OpenAI API key
OPENAI_API_KEY = "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"  # Replace with actual key
openai.api_key = OPENAI_API_KEY  # This should be on a new line

def generate_script(topic, prompt):
    full_prompt = f"{prompt}\n\nWrite a script about: {topic}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": full_prompt}],
        temperature=0.7,
        max_tokens=800
    )

    return response["choices"][0]["message"]["content"]
