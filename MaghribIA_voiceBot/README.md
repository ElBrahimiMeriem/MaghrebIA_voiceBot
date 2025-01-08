
________________________________________

# MaghrebIA: Moroccan Tourism Voice Assistant

This repository contains the implementation of a voice assistant named **MaghrebIA**, designed to provide accurate, culturally-sensitive, and practical information about Moroccan tourism. The assistant uses **Retrieval-Augmented Generation (RAG)** to enhance responses, leveraging embeddings and vector search for context retrieval.

A custom dataset was created by scraping data from various websites, including **Booking** and **Visit Morocco**, to compile a CSV file with **17,153 entries**, each containing a **Prompt** (question) and a **Response** (answer). This dataset is the foundation for generating relevant and precise responses.

---
##  Data Sources: 
 The dataset was built by scraping tourism-related content from trusted sources, such as:
  - [Booking.com](https://www.booking.com/)
  - [Lonely Planet](https://www.lonelyplanet.com/)
  - [Visit Morocco](https://www.visitmorocco.com/)
  - [Memphis Tours](https://www.memphistours.com/)
  - [TasteAtlas](https://www.tasteatlas.com/)
  - [Nomadic Matt](https://www.nomadicmatt.com/)
  - [GetYourGuide](https://www.getyourguide.com/)
  - [Site of Moroccan Ministry of Youth, Culture, and Communication](https://mtaess.gov.ma/fr/annuaires/annuaire-des-etablissements-dhebergements-touristique/)
  - [Morocco.com](https://www.morocco.com/)
  - [Best Restaurants Maroc](https://www.bestrestaurantsmaroc.com/)


## Architecture 

The architecture of MaghrebIA is designed to provide seamless and interactive voice-based assistance for Moroccan tourism. Below is an overview of the methodology and flow:

1. **Call Initialization**: The user initiates a call via Twilio, which serves as the voice gateway.
2. **Speech Processing**: OpenAI's Whisper model transcribes the user's voice input into text.
3. **Query Embedding**:
   - The transcribed query is vectorized using OpenAI's **text-embedding-ada-002** model.
   - The resulting query vector is used to perform similarity searches in the Chroma vector store.
4. **Context Retrieval**:
   - The Chroma vector store retrieves the top 5 most relevant documents from the custom tourism dataset.
5. **Response Generation**:
   - OpenAI's GPT-4 model generates a response by combining the retrieved documents and the user's query.
6. **Voice Output**:
   - OpenAI's TTS model converts the response into speech.
   - The spoken response is delivered back to the user via Twilio.

### Visual Representation

Below is the architecture of the system:

<img width="834" alt="image" src="https://github.com/user-attachments/assets/8545add5-3ea7-41f4-a990-3322c0ccf7a3" />

---

## Prerequisites

To use the app, you will need:

- Python 3.9+
- A Twilio account: You can sign up for a free trial [here](https://www.twilio.com/login?iss=https%3A%2F%2Flogin.twilio.com%2F).
- A Twilio number with Voice capabilities: [Instructions here](https://help.twilio.com/articles/223135247-How-to-Search-for-and-Buy-a-Twilio-Phone-Number-from-Console).
- An OpenAI account and API Key.
- A Livekit account.
- A Twilio Dev-Phone: [Instructions here](https://www.twilio.com/docs/labs/dev-phone#install-the-dev-phone).

---

## Project Files

- **agent.py**: The main implementation of the voice assistant, initializing embeddings, handling RAG-based response generation, and managing voice interactions.
- **build\_data.py**: Prepares and stores vectorized documents using OpenAI embeddings and the Chroma vector store. Essential for building the vector store from datasets.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ElBrahimiMeriem/MaghrebIA_voiceBot.git  
   cd MaghrebIA_voiceBot/MaghribIA_voiceBot
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the `.env.local` file:
   Create a file named `.env.local` in the root directory and add your OpenAI API key and other configurations. Example:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```
4. Get your trunk ID:
   Follow this [video](https://www.youtube.com/watch?v=8O1_j9c-Lls\&t=583s) (start from minute 8) to obtain your trunk ID and add it to the `dispatch-rule.json` file.
5. Get your Twilio number:
   Obtain a Twilio number and add it to the `inboundLivekitTrunk.json` file.
6. Build the vector store:
   Run the following command to create the vector store:
   ```bash
   python build_data.py
   ```
7. Start the voice assistant:
   Run the following command to start the assistant:
   ```bash
   python agent.py
   ```

---

## Usage

The voice assistant is designed to:

1. Receive user queries via voice input.
2. Convert the voice input to text using OpenAI STT.
3. Retrieve relevant context from the Chroma vector store using OpenAI embeddings.
4. Generate responses using OpenAI LLM and output them via TTS.

---

Thank you for exploring MaghrebIA VoiceBot! We hope this assistant provides valuable and engaging support for all your Moroccan tourism needs. If you have any feedback or suggestions, feel free to contribute to the repository or reach out.
