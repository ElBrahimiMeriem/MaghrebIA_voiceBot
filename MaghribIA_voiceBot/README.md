
________________________________________
Moroccan Tourism Voice Assistant
This repository contains the implementation of a voice assistant named MaghrebIA, designed to provide accurate, culturally-sensitive, and practical information about Moroccan tourism. The assistant uses Retrieval-Augmented Generation (RAG) to enhance responses, leveraging embeddings and vector search for context retrieval.
________________________________________
Features
•	Voice interaction with text-to-speech (TTS) and speech-to-text (STT) capabilities.
•	Contextual response generation using RAG.
•	Powered by OpenAI's language models and embeddings.
•	Supports similarity search with Chroma vector store for retrieving relevant documents.
•	Customizable responses tailored for Moroccan tourism.
________________________________________
Prerequisites
To use the app, you will need:
•	Python 3.9+ 
•	A Twilio account: You can sign up for a free trial here.
•	A Twilio number with Voice capabilities: Here are instructions to purchase a phone number.
•	An OpenAI account and an OpenAI API Key: You can sign up here. 
•	A livekit account: You can sign up here.
•	A Twilio Dev-Phone: Here are instructions.
________________________________________
Requirements
The project uses the following dependencies, listed in requirements.txt:
Install the dependencies using:
pip install -r requirements.txt
________________________________________
Project Files
•	agent.py: Contains the main implementation of the voice assistant. It initializes the embeddings, handles RAG-based response generation, and manages voice interactions.
•	build_data.py: Script to prepare and store vectorized documents using OpenAI embeddings and the Chroma vector store. Useful for building the vector store from datasets.
________________________________________
How to Run
1.	Clone the repository:
2.	git clone <repository-url>
3.	cd <repository-folder>
4.	Set up the .env.local file: Provide your OpenAI API key and other configurations in a file named .env.local. Example:
5.	OPENAI_API_KEY=your_openai_api_key
6.	Build the vector store (if not already built): python build_data.py
8.	Start the voice assistant:	python agent.py
________________________________________
Usage
The voice assistant is designed to:
1.	Receive user queries via voice input.
2.	Convert the voice input to text using Silero STT.
3.	Retrieve relevant context from the Chroma vector store using OpenAI embeddings.
4.	Generate responses using OpenAI LLM and output them via text-to-speech (TTS).
________________________________________

=======
# MaghrebIA_voiceBot

