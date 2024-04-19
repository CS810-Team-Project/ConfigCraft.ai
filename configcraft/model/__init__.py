# from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# from llama_index.llms.llama_cpp import LlamaCPP
# import faiss
# from llama_index.core import (
#     SimpleDirectoryReader,
#     load_index_from_storage,
#     VectorStoreIndex,
#     StorageContext,
# )
# from llama_index.vector_stores.faiss import FaissVectorStore
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# print("System initializing...")
# sentence transformers
# embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

# # model_url = "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q4_0.bin"
# model_url = "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/resolve/main/llama-2-13b-chat.Q4_0.gguf"

# llm = LlamaCPP(
#     # You can pass in the URL to a GGML model to download it automatically
#     model_url=model_url,
#     # optionally, you can set the path to a pre-downloaded model instead of model_url
#     model_path=None,
#     temperature=0.1,
#     max_new_tokens=256,
#     # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
#     context_window=3900,
#     # kwargs to pass to __call__()
#     generate_kwargs={},
#     # kwargs to pass to __init__()
#     # set to at least 1 to use GPU
#     model_kwargs={"n_gpu_layers": 1},
#     verbose=True,
# )

# dimensions of text-ada-embedding-002
# d = 1536
# faiss_index = faiss.IndexFlatL2(d)
# documents = SimpleDirectoryReader(os.getenv("DATA_PATH")).load_data()
# vector_store = FaissVectorStore(faiss_index=faiss_index)
# storage_context = StorageContext.from_defaults(vector_store=vector_store)
# index = VectorStoreIndex.from_documents(
#     documents, storage_context=storage_context
# )
# index.storage_context.persist()
# vector_store = FaissVectorStore.from_persist_dir("./storage")
# storage_context = StorageContext.from_defaults(
#     vector_store=vector_store, persist_dir="./storage"
# )
# index = load_index_from_storage(storage_context=storage_context)

from typing import List

# Function to convert documents to embeddings
# def embed_documents(documents: List[str]):
#     return embed_model.encode(documents)

# Function to perform search and retrieve documents
# def search_documents(query: str, k=5):
#     print("Searching for:", query)
#     # Convert the query to an embedding
#     query_embedding = embed_documents([query])[0]
#     # Perform search
#     distances, indices = vector_store.faiss_index.search(query_embedding.reshape(1, -1), k)
#     return [documents[i] for i in indices[0]], distances[0]

# Function to generate a response using the LLAMA model and retrieved documents
# def generate_response(query: str):
#     print("Generating response for:", query)
#     # Retrieve documents based on the query
#     retrieved_docs, _ = search_documents(query)
#     # Combine the query and the retrieved documents to form the input context
#     context = f"Question: {query}\n\n" + "\n\n".join([f"Document: {doc}" for doc in retrieved_docs])
#     # Generate a response using the LLAMA model
#     response = llm.generate(context)
#     return response

# Process input text and get an AI response
# def get_ai_response(input_text: str):
#     print("Processing input:", input_text)
#     # First, retrieve relevant context from your data
#     retrieved_context, _ = search_documents(input_text)
    
#     # Then, use the retrieved context and the input text to generate a response
#     response = llm.generate(f"{input_text} {retrieved_context[0]}", max_new_tokens=50)
#     return response

# Example usage
# input_text = "What are the latest trends in technology?"
# ai_response = get_ai_response(input_text)
# print(ai_response)

# from openai import OpenAI
from llama_index.llms.openai import OpenAI
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    download_loader,
    RAKEKeywordTableIndex,
)

llm = OpenAI(temperature=0, model="gpt-3.5-turbo")
print("System initializing...")
reader = SimpleDirectoryReader(input_files=["./data/iptables.pdf"])
data = reader.load_data()
index = VectorStoreIndex.from_documents(data)
query_engine = index.as_query_engine(streaming=True, similarity_top_k=3)
import os

# Assuming you've set your OpenAI API key in your environment variables:

# Your embedding and search functionality remains the same as before.

# Replace the LLAMA generation function with a function that uses GPT-4
# def generate_response_with_gpt4(prompt):
#     try:
#         response = llm.chat.completions.create(
#             model="gpt-4-turbo",  # You can specify GPT-4 once it's available to you.
#             messages=[
#                 {"role": "system", "content": """
#                 You are an advanced AI assistant tasked with facilitating a team of developers working on the ConfigCraft.ai project. 
#                 Your primary role is to assist the team in generating configuration files for iptables by providing intelligent recommendations and generating code snippets based on the user's requirements
#                 You are equipped with cutting-edge natural language understanding and generative AI capabilities, allowing you to understand complex technical requirements and translate them into functional iptables rules.
#                 """},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.7,
#             max_tokens=150
#         )
#         return response.choices[0].message.content
#     except Exception as e:
#         return f"An error occurred: {str(e)}"

# Function to handle the RAG process
def get_ai_response(input_text: str):
    resp = query_engine.query(input_text).get_response()
    if resp and resp.response:
        return resp.response
    else:
        return "I'm sorry, I don't have an answer for that."