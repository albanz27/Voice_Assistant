import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

# --- Carica variabili d'ambiente ---
load_dotenv()
AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

# --- Configura il contesto dell'assistente ---
user_name = "Alban"
schedule = "Meeting with Marco on Monday at 18:00; Alberto's Laurea on Tuesday at 11:00; Hang out with girlfriend on Saturday"
prompt = f"You are a helpful assistant. Your interlocutor has the following schedule: {schedule}."
first_message = f"Hello {user_name}, how can I help you today?"

conversation_override = {
    "agent": {
        "prompt": {"prompt": prompt},
        "first_message": first_message,
    }
}

# --- Configurazione della conversazione ---
config = ConversationConfig(
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={},
    user_id="alban_27", 
)

# --- Inizializza client ElevenLabs ---
client = ElevenLabs(api_key=API_KEY)

# --- Callback per gestire le risposte ---
def print_agent_response(response):
    print(f"\nAgent: {response}")
    with open("conversation_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Agent: {response}\n")

def print_interrupted_response(original, corrected):
    print(f"\nAgent interrupted, truncated response: {corrected}")
    with open("conversation_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Agent interrupted, truncated response: {corrected}\n")

def print_user_transcript(transcript):
    print(f"\nUser: {transcript}")
    with open("conversation_log.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {transcript}\n")

# --- Crea la sessione di conversazione ---
conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

# --- Avvia l'assistente vocale ---
try:
    print("Voice Assistant started. Speak into your microphone. Press Ctrl+C to stop.")
    conversation.start_session()
except KeyboardInterrupt:
    print("\nSession terminated by user.")
