from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import PyPDFDirectoryLoader, DirectoryLoader, TextLoader
from dotenv import load_dotenv

load_dotenv()

directory = 'My Documents'

llm = ChatGoogleGenerativeAI(
    model='gemini-3-flash-preview'
)

# Load pdf data

pdf_loader = PyPDFDirectoryLoader(directory)
pdf_docs = pdf_loader.load()
# Load text documents
text_loder = DirectoryLoader(
    directory,
    glob='**/*.txt',
    loader_cls=TextLoader
)

text_docs = text_loder.load()

docs = pdf_docs + text_docs

# Add user query

user_query = input("Enter your query:-")

# Implement embeddings and vector store
embeddings = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-miniLM-L6-v2'
)

vector_store = InMemoryVectorStore(embeddings)

vector_store.add_documents(docs)