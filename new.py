import tkinter as tk
import pyttsx3
import os
from google.cloud import texttospeech

# Initialize tkinter and pyttsx3
root = tk.Tk()
root.title("Text-to-Speech Converter")
engine = pyttsx3.init()

# Define function to speak the input text
def speak_text():
    global running
    running = True
    text = input_field.get("1.0", "end-1c")
    engine.say(text)
    engine.runAndWait()

# Define function to stop speaking
def stop_speaking():
    global running
    running = False
    engine.stop()


# Define function to save the input text as a audio file
def save_text():
    # Set up Text-to-Speech client
    client = texttospeech.TextToSpeechClient()

    # Get the text from the input field
    text = input_field.get("1.0", "end-1c")

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code and the voice gender
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save the audio file
    with open("speech_audio.mp3", "wb") as out:
        out.write(response.audio_content)

    # Optionally, you can play the audio file using a media player
    os.system("start speech_audio.mp3")

# Create GUI window elements
input_label = tk.Label(root, text="Enter text to speak:")
input_label.pack(pady=(20, 5))

input_frame = tk.Frame(root, bg="#ffffff")
input_frame.pack(padx=20, pady=5, ipady=10, ipadx=10)

input_field = tk.Text(input_frame, font=("Helvetica", 14), height=10)
input_field.pack(fill="both", expand=True)

speak_button = tk.Button(root, text="Speak", command=speak_text)
speak_button.pack(side=tk.BOTTOM, pady=(20, 10), padx=20)
speak_button.config(borderwidth=0, highlightthickness=0, pady=12, padx=20, bd=0, highlightbackground="#cccccc", highlightcolor="#cccccc", relief=tk.SOLID, cursor="hand2", bg="#3f51b5", fg="#ffffff", activebackground="#ffffff", activeforeground="#3f51b5")

save_button = tk.Button(root, text="Save File", command=save_text)
save_button.pack(side=tk.BOTTOM, pady=(0, 10), padx=20)
save_button.config(borderwidth=0, highlightthickness=0, pady=12, padx=20, bd=0, highlightbackground="#cccccc", highlightcolor="#cccccc", relief=tk.SOLID, cursor="hand2", bg="#3f51b5", fg="#ffffff", activebackground="#ffffff", activeforeground="#3f51b5")

stop_button = tk.Button(root, text="Stop", command=stop_speaking)
stop_button.pack(side=tk.LEFT, pady=(20, 10), padx=20)
stop_button.config(borderwidth=0, highlightthickness=0, pady=12, padx=20, bd=0, highlightbackground="#cccccc", highlightcolor="#cccccc", relief=tk.SOLID, cursor="hand2", bg="#3f51b5", fg="#ffffff", activebackground="#ffffff", activeforeground="#3f51b5")
# Round the corners of the input field
input_frame.bind("<Configure>", lambda e: input_frame.config(highlightthickness=0, borderwidth=0, padx=2, pady=2, relief=tk.FLAT))

# Round the corners of the buttons
for button in [speak_button, save_button]:
    button.config(bd=0, highlightthickness=0, relief=tk.FLAT)

# Run the GUI window
root.mainloop()
