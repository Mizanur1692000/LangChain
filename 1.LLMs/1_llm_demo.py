import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # load GOOGLE_API_KEY from .env
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

result = llm.invoke("What is the capital of Bangladesh?")
print(result.content)
