from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
   
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Write a tweet about learning GenAI")

print(response.content)

response2 = model.invoke("Act as a critic and review about the film Rockstar by Imtiaz Ali")

print(response2.content)
