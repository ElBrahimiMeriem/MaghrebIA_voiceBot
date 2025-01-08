import logging  # Importing logging to capture logs and debug information.
from dotenv import load_dotenv  
from livekit.agents import (
    AutoSubscribe,  # Importing AutoSubscribe to automatically manage subscription settings.
    JobContext,  # Importing JobContext to handle job-related metadata.
    JobProcess,  # Importing JobProcess to define processing steps.
    WorkerOptions,  # Importing WorkerOptions to configure the worker behavior.
    cli,  # Importing cli to run the application through the command line interface.
    llm,  # Importing llm to interact with the language model.
)
from livekit.agents.pipeline import VoicePipelineAgent  # Importing VoicePipelineAgent to handle voice interactions.
from livekit.plugins import openai, silero  # Importing OpenAI and Silero plugins for speech-to-text and text-to-speech.
from langchain_community.vectorstores import Chroma  # Importing Chroma vector store for similarity search.
from langchain_openai import OpenAIEmbeddings  # Importing OpenAI embeddings to convert text into vector representations.

load_dotenv(dotenv_path=".env.local")  # Loading environment variables from the .env.local file for configuration.
logger = logging.getLogger("voice-agent")  # Setting up a logger to track the operations of the voice agent.

# Chargement du vectorstore existant
persist_directory = "tourism_db"  

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")  # Initializing OpenAI embeddings with the specified model to ensure consistent embeddings.

# Charger ou initialiser Chroma DB
try:
    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)  # Attempting to load the Chroma DB from the directory.
    logger.info("Chroma DB chargé avec succès.")  # Logging a success message if the vector store is loaded correctly.
except Exception as e:
    logger.error("Erreur lors du chargement de Chroma DB : ", e)  
    raise  

# Function to enrich the user's messages with relevant context using the Retrieval-Augmented Generation (RAG) approach.
async def _enrich_with_rag(agent: VoicePipelineAgent, chat_ctx: llm.ChatContext):
    user_msg = chat_ctx.messages[-1]  # Retrieving the last message in the chat context.
    user_embedding = await openai.create_embeddings(  # Creating embeddings for the user's message.
        input=[user_msg.content],
        model="text-embedding-ada-002"
    )
    query_vector = user_embedding[0].embedding  # Extracting the vector representation of the user's message.
    results = vectorstore.similarity_search_by_vector(query_vector, k=5)  # Searching the vector store for the top 5 most similar documents.
    
    if results:  
        closest_doc = results[0]  # Selecting the closest document based on the similarity score.
        paragraph = closest_doc.page_content  # Extracting the content of the closest document.
        logger.info(f"Enriching with RAG: {paragraph}")  # Logging the context being used to enrich the response.

        rag_msg = llm.ChatMessage.create(  # Creating a new chat message with the retrieved context.
            text="Context:\n" + paragraph,
            role="assistant",
        )
        chat_ctx.messages[-1] = rag_msg  # Replacing the last message in the context with the enriched message.
        chat_ctx.messages.append(user_msg)  # Appending the user's original message to maintain the conversation flow.
    
# Point d'entrée de l'application
async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(  
        role="system",
        text=(
            """
You are مَغْرِبِيَة, an AI-powered voice assistant specialized in Moroccan tourism. Your role is to provide accurate, culturally-sensitive, and practical information using Retrieval-Augmented Generation (RAG) to enhance responses.  

**Core Guidelines**  
- Use retrieved context if relevant and accurate; ignore it if unsuitable for the query.  
- Provide concise, practical, and respectful information tailored to user needs.  
- Avoid unverified data, assumptions, or political topics.  

**Knowledge Scope**  
- Moroccan geography, culture, attractions, and practical travel tips.  
- Accommodations, dining, transportation, and safety information.  
Your primary goal is to assist travelers effectively while respecting Moroccan heritage and customs."""
        ),
    )

    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)  # Connecting to the job context and setting the subscription mode to audio-only.

    agent = VoicePipelineAgent( 
        chat_ctx=initial_ctx, 
        vad=silero.VAD.load(),  # Loading the voice activity detection model from Silero.
        stt=openai.STT(),  # Setting up speech-to-text using OpenAI's model.
        llm=openai.LLM(),  # Setting up the language model for generating responses.
        tts=openai.TTS(voice="nova"),  # Setting up text-to-speech using OpenAI's model with a specific voice.
        before_llm_cb=_enrich_with_rag,  # Assigning the RAG enrichment function to be executed before the LLM.
    )
    agent.start(ctx.room)  # Starting the voice pipeline agent in the specified room.
    await agent.say("Welcome! I am مَغْرِبِيَة, your voice assistant here to help you explore the beauty of Morocco. How can I assist you today?", allow_interruptions=True)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))  
