
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
•	A Twilio account: You can sign up for a free trial here"https://www.twilio.com/login?iss=https%3A%2F%2Flogin.twilio.com%2F".
•	A Twilio number with Voice capabilities: Here are instructions to purchase a phone number (https://help.twilio.com/articles/223135247-How-to-Search-for-and-Buy-a-Twilio-Phone-Number-from-Console) .
•	An OpenAI account and an OpenAI API Key. 
•	A livekit account.
•	A Twilio Dev-Phone: [Here are instructions](https://www.twilio.com/docs/labs/dev-phone#install-the-dev-phone).
________________________________________
Project Files
•	agent.py: Contains the main implementation of the voice assistant. It initializes the embeddings, handles RAG-based response generation, and manages voice interactions.
•	build_data.py: Script to prepare and store vectorized documents using OpenAI embeddings and the Chroma vector store. Useful for building the vector store from datasets.
________________________________________
How to Run
1.	Clone the repository:
git clone https://github.com/ElBrahimiMeriem/MaghrebIA_voiceBot.git
cd MaghrebIA_voiceBot/MaghribIA_voiceBot
2.  Install the dependencies using:
pip install -r requirements.txt
3.	Set up the .env.local file:
Create a file named .env.local in the root directory and add your OpenAI API key and other configurations. Example:
OPENAI_API_KEY=your_openai_api_key
4.	Get your trunk ID:
Follow this video https://www.youtube.com/watch?v=8O1_j9c-Lls&t=583s (start watching from minute 8) to obtain your trunk ID. Add the trunk ID to the dispatch-rule.json file.
5.	Get your Twilio number:
Obtain a Twilio number and add it to the inboundLivekitTrunk.json file.
6.	Build the vector store:
If the vector store is not already built, run the following command:
python build_data.py
7.	Start the voice assistant:
Run the following command to start the assistant:
python agent.py
________________________________________
Usage
The voice assistant is designed to:
1.	Receive user queries via voice input.
2.	Convert the voice input to text using OpenAI STT.
3.	Retrieve relevant context from the Chroma vector store using OpenAI embeddings.
4.	Generate responses using OpenAI LLM and output them via text-to-speech (TTS).
________________________________________

=======
# MaghrebIA_voiceBot

