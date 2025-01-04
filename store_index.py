from src.helper import *
from pinecone import Pinecone, ServerlessSpec
from langchain.vectorstores import Pinecone as PineconeVecStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

extracted_data = load_pdf_file("./Data/")
text_chunks = text_split(extracted_data)
embeddings = download_embeddings()

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "healthcarebotsindex"

pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)

# Embed each chunk and upsert the embeddings into your Pinecone index
docsearch = PineconeVecStore.from_documents(
    documents = text_chunks,
    index_name = index_name,
    embedding = embeddings
)