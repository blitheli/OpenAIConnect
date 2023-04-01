import os
import openai

print('----openai------')
openai.organization = "org-DaDfB9xHQ5ySB3qRdJC8G0zD"
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.Model.list()

# 调用openAi接口
response = openai.Completion.create(model="text-davinci-003",
                                    prompt="中国的陆地面积多大？",
                                    max_tokens=100,
                                    temperature=0.5)


print("-------------GPT返回的消息----------------------")

print(response.choices[0].text.strip())
