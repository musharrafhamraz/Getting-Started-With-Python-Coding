import pyttsx3
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Set properties for the speech
engine.setProperty('rate', 150)  # Speed in words per minute
engine.setProperty('volume', 0.7)  # Volume, from 0 to 1

# Define the text to be spoken
text = "Hello, world! This is a test of the text-to-speech system."

# Iterate over the available voices and speak the text using each voice
for voice in voices:
    engine.setProperty('voice', voice.id)
    print(f"Speaking with voice: {voice.name}")
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Save the spoken text as an audio file
documents_folder = os.path.expanduser("~/Documents")
engine.save_to_file(text, os.path.join(documents_folder, "spoken_text.mp3"))
