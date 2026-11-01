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

