#CHAT BOT APP USING GOOGLE GEMINI LLM
import streamlit as st
import os
#streamlit is python based UI Framework
from langchain_google_genai import ChatGoogleGenerativeAI
#according to OOP llm is an instance of google
#here langchain_google_genai is package/module
#chatgoogleGenerativeAI is class
from dotenv import load_dotenv
#here dotenv is module where load_dotenv is the function
#or method
#it reads key-value settings from a local memory
#.env file into enviromental variables .
load_dotenv() #method calling
#streamlit UI
api_key = os.getenv("GOOGLE_API_KEY")
st.title("Gemini Chatbot App")
llm=ChatGoogleGenerativeAI(model='gemini-3.5-flash',
                           api_key=api_key,
                           temperature=0.5)
#here llm is an object for the class ChatGoogleGenerateAI
#IF class is passing through certain variables called
#instance variables
'''here gemini llm model is gemini-3.5-flash and 
temparature is the parameter help to llm to retrieve
creative answer for the given prompt'''
#ask the question to the llm
question=st.text_area('Enter desired query',height=120)
if st.button("Ask LLM:"):
    if question.strip()=='':
        st.warning("Please enter a query")
    else:
        with st.spinner('Thinking LLM to bring ur answer: '):
            response=llm.invoke(question)
        st.write(response.content)