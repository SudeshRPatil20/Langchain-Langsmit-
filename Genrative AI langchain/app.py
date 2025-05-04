import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRAINCING_V2']="true"
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')

prompts=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistent. Please respond to the question asked"),
        ("user","Question{question}")
    ]
)

st.title("Lnagchain Demo with OLLAMA")
input_text=st.text_input("What question you have in mind")

llms=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompts|llms|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))