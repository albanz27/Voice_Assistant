# Voice Virtual Assistant with ElevenLabs

A Python-based voice assistant that listens, understands, and talks back in real-time using the ElevenLabs Conversational AI API. Fully customizable and easy to extend with your own prompts, schedules, or additional integrations.

---

## Features

- Real-time voice input and output
- Customizable system prompt and first message
- Handles user interruptions
- Extendable with calendars, home automation, or other APIs
- Simple setup with Python and ElevenLabs SDK

---

## Prerequisites

- Python 3.11 or higher
- ElevenLabs account
- Microphone and speakers

---

## Installation

1. Clone the repository:

git clone https://github.com/albanz27/Voice_Assistant.git
cd Voice_Assistant

2. Install required Python packages:

pip install elevenlabs elevenlabs[pyaudio] python-dotenv

3. Install system dependencies if needed:

Linux:
sudo apt install portaudio19

MacOS:
brew install portaudio
