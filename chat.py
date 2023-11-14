# chat.py
from decouple import config
import openai


api_key = config("OPENAI_API_KEY")
openai.api_key = api_key

content = "you are randomly generating 6 individual fantasy regions for a user, please provide a region name and a description."

completion = openai.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role":"system", "content": "Generate JSON response"},
            {"role": "user", "content": content}
        ],
        response_format={"type": "json_object"}
    )
print(completion.choices[0].message.content)



