from openai import OpenAI
import os
from few_shot import FewShotPosts


client = OpenAI(
    api_key= os.environ.get("groq_api_key"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input= FewShotPosts,
    model="openai/gpt-oss-20b",
)
print(response.output_text)


