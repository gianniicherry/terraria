from decouple import config
import openai

api_key = config("OPENAI_API_KEY")

openai.api_key = api_key


completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are telling Fantasy story based on a users choices"},
    {"role": "user", "content": "Introduce Grok, a fabled warrior to the kingdom of Nysteria"}
  ]
)

print(completion.choices[0].message)