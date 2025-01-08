import os  
import pandas as pd  
from langchain_openai import OpenAIEmbeddings 
from langchain_chroma import Chroma  
from langchain.schema import Document 
from dotenv import load_dotenv  
load_dotenv(dotenv_path=".env.local")
CSV_FILE_PATH = "dataframe_17k_v2.csv"

# Load CSV and combine columns
# The dataset contains two columns: "Prompt" and "Response".
# Drop rows with NaN values in "Prompt" or "Response" columns
# These columns are combined into a single column to provide more context and information for processing.
df = pd.read_csv(CSV_FILE_PATH) 
df.dropna(subset=["Prompt", "Response"], inplace=True)
df["Combined"] = df["Prompt"] + " " + df["Response"]  
# Prepare documents (each row becomes a document)
documents = [Document(page_content=row) for row in df["Combined"]]

# Generate embeddings and save to Chroma database
batch_size = 5000  # You can change this number, but it should be less than 5461

# Initialize the embeddings model
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# Create a Chroma vector store
vectorstore = Chroma(persist_directory="tourism_db", embedding_function=embeddings)

# Split documents into batches and process them
for i in range(0, len(documents), batch_size):
    batch = documents[i:i + batch_size]  # Get a smaller batch of documents
    vectorstore.add_documents(batch)  # Add the batch to the vector store

print("Vectorstore saved successfully.")
# Initialize the retriever from the Chroma vector store
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})  # Retrieve top 3 similar documents

# Test query (input question)
query = "What are the top tourist destinations in Morocco?"

# Get the top 3 most relevant documents
relevant_docs = retriever.get_relevant_documents(query)

# Print the retrieved documents
print("Retrieved Documents:")
for i, doc in enumerate(relevant_docs):
    print(f"Document {i+1}: {doc.page_content}\n")