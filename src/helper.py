from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

# Extract data from PDF
def load_pdf_file(data_path):
    loader = DirectoryLoader(data_path,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader)
    return loader.load()

# Split the data into text chunks
def text_split(data):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    return splitter.split_documents(data)

#Download the embeddings from HuggingFace
def download_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings