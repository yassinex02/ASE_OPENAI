import openai
response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=[{"role": "system", "content": "You are ahelpful sports assistant."}, {"role": "user", "content": "what is thefootball team that won more Champion leagues?"}])
result = ''
for choice in response.choices:
    result += choice['message']['content']
print(result)
