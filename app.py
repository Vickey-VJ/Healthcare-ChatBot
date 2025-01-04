from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
from langchain.vectorstores import Pinecone as PineconeVStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app=Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

embeddings = download_embeddings()

index_name = "healthcarebotsindex"

# Embed each chunk and upsert the embeddings into your Pinecone
docsearch = PineconeVStore.from_existing_index(
    index_name = index_name,
    embedding = embeddings)

retriever = docsearch.as_retriever(search_type = "similarity",
                                   search_kwargs = {"k": 3})

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=1,
    max_retries=2,
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

question_answering_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answering_chain)

@app.route('/')
def index():
    return render_template('index.html')

@app. route("/get", methods= ["GET", "POST"])
def chat() :
    input = request.form["msg"]
    print(input)
    response = rag_chain.invoke({"input": input})
    print ("Response : ", response ["answer"])
    return str(response["answer"])

if __name__ == "__main__":
    app.run(debug=True)