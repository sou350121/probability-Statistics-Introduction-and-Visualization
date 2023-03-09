# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:40:52 2023

@author: ken3

Introduction:
    LlamaIndex 
"""


api_key='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' #OpenAI API

from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from langchain.llms import OpenAIChat

def get_llm_response(question, answer):
    template="Question: {question}\n{answer}"
    prompt = PromptTemplate(template=template, input_variables=["question", "answer"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAIChat(model_name="gpt-3.5-turbo",openai_api_key=api_key))
    response = llm_chain.run(question=question, answer=answer)
    return response


from langchain.document_loaders import UnstructuredURLLoader
from langchain.document_loaders import PDFMinerLoader
from langchain.document_loaders import TextLoader
from PyPDF2 import PdfReader

file_name = "2302.14045.pdf"
reader = PdfReader(file_name) # Read the uploaded PDF file. Upload your file in collab or read from URL
pdf_text = ""
print("Total pages=",len(reader.pages)) # Total pages in the pdf
page_numbers_to_read = [0] # Specify which pages you want to read

# Read the given pages
for page in page_numbers_to_read:
    page_text = reader.pages[page].extract_text()
    print("Reading pages {} of :\n{}".format(page+1, str(len(reader.pages))))
    #print("The contents of page {} are:\n{}".format(page+1, page_text))
    pdf_text += page_text
    
#print("All extracted text:\n", pdf_text)

#save the extracted data from pdf to a txt file
file1=open(r"pdf2text.txt","a")
file1.writelines(pdf_text)
print("file saved")


# Call the LLM with input data and instruction
input_data=pdf_text
instruction="What are the main findings of this paper?"
response = get_llm_response(input_data, instruction)
print("LLM Response:\n",str(response))
