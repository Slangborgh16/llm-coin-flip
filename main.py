from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

model = 'gpt-3.5-turbo'
client = OpenAI()

response = client.chat.completions.create(
    model=model,
    messages = [
        {'role' : 'system', 'content' : 'Reply in one word'},
        {'role' : 'user', 'content' : 'Flip a coin'}
    ]
)

result = response.choices[0].message.content
print(result)
