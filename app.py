import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
from dotenv import load_dotenv
import os

# Load the .env file to access the API token
load_dotenv()

# Access the Hugging Face API token from the environment
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

## Function To get response from LLAma 3 model
def getLLamaresponse(input_text,no_words,blog_style):
    ### Hugging Face model using HuggingFaceHub
    llm = HuggingFaceHub(repo_id="unsloth/Llama-3.2-1B-Instruct",
                         huggingfacehub_api_token=api_token, 
                         model_kwargs={'max_new_tokens': 256, 'temperature': 0.01})
    ## Prompt Template
    template="""
        Write a blog for {blog_style} on {input_text} topic
        within {no_words} words.
            """
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    ## Generate the ressponse from the LLama 3 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    # print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the Blog Topic")

## creating to more columns for additonal 2 fields
col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)

submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))