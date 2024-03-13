from langchain.llms import OpenAI
#from langchain.llms import OpenAI

#import streamlit as st
import streamlit as st
import os


# def get_openai_response(question):
#     llm=OpenAI(model_name="text-davinci-003",temperature=0.5)
#     response=llm(question)
#     return response

import os
os.environ['openai_api_key']="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"

def get_openai_response(question):
    llm = OpenAI(openai_api_key = os.getenv('openai_api_key'),model_name="gpt-3.5-turbo-instruct",temperature=0.5)
    response = llm(question)
    return(response)

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)