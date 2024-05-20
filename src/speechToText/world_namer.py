from openai import OpenAI
import datetime

def generate_filename(text):
    prompt = f"Summarize this description into a short, coherent filename perfect for Windows directories: '{text}'. Keep the filename short and in English."

    client = OpenAI()
    gpt_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ], 

    )

    filename = gpt_response.choices[0].message.content.strip().replace(' ', '_').replace('"', '')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    full_filename = f"{filename}-{timestamp}.txt"

    return full_filename





