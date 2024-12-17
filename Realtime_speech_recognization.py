#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:blue";font-size:30px;>Multifunctional Speech Recognition System with Translation and Sentimentaion Analysis</h1>
# 

# In[1]:


READ SAVED AUDIO FILE
import os
print(os.path.abspath("output.wav"))
from IPython.display import FileLink
FileLink("output.wav")


# In[3]:


import os
import webbrowser
import speech_recognition as sr
from googletrans import Translator
from textblob import TextBlob
from gtts import gTTS

recognizer = sr.Recognizer()
translator = Translator()

commands = {
    "open browser": "Opening the web browser...",
    "open mail": "Opening the email client...",
    "open spotify": "Opening Spotify...",
}

def recognize_speech_from_mic():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Sorry, the service is down. Please try again later.")
            return None

def speak(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    filename = "output.mp3"
    tts.save(filename)
    os.system(f"start {filename}")  

def execute_command(command):
    command = command.lower()  

    if "open browser" in command:
        print(commands["open browser"])
        webbrowser.open("http://www.google.com")  

    elif "open mail" in command:
        print(commands["open mail"])
        os.system("start mailto:")  

    elif "open spotify" in command:
        print("Opening Spotify...")
        os.system("start spotify") 

    else:
        print("Command not recognized.")

def recognize_and_translate():
    text = recognize_speech_from_mic()
    if text:
       
        translated = translator.translate(text, dest='hi')
        print(f"Translated Text (Hindi): {translated.text}")

        
        speak(translated.text, lang='hi') 

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        print("Positive sentiment detected!")
    elif sentiment < 0:
        print("Negative sentiment detected!")
    else:
        print("Neutral sentiment.")

def continuous_listen():
    print("Starting continuous listening mode... (Press Ctrl+C to stop)")
    listening = True
    while listening:
        try:
            text = recognize_speech_from_mic()
            if text:
                print(f"Recognized: {text}")
                execute_command(text)  
        except KeyboardInterrupt:
            print("Stopping listening mode...")
            listening = False
        except Exception as e:
            print(f"An error occurred: {e}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Execute command")
        print("2. Translate speech (English to Arabic)")
        print("3. Analyze sentiment")
        print("4. Read back your speech")
        print("5. Exit")
        choice = input("Select an option (1-6): ")

        if choice == '1':
            # command
            text = recognize_speech_from_mic()
            if text:
                execute_command(text.lower())  

        elif choice == '2':
            # Translation
            recognize_and_translate()

        elif choice == '3':
            # Sentiment Analysis
            text = recognize_speech_from_mic()
            if text:
                analyze_sentiment(text)

        elif choice == '4':
           
            print("Speak something to read it back...")
            text = recognize_speech_from_mic()
            if text:
                speak(text) 

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose again.")
            menu()


# In[ ]:




