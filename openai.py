from dotenv import load_dotenv
import openai
import os


my_secret_key = os.getenv('MY_SECRET_KEY')
conversation = [
    {"role": "system", "content": "You are a curious football fan."},
    {"role": "user", "content": "What football team has the most wins in the Champions League?"}
]

# Make an API call to GPT-3.5 Turbo
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation  # Use 'conversation' here, not 'messages'
)

# Extract and print the model's reply
answer = response.choices[0].message['content']
print("Answer:", answer)
