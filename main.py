import os
import pygame
import speech_recognition as sr
from scraper.bot_scraper import *
import pyautogui
import pywhatkit
from datetime import datetime

def speak(text):
    voice = "en-US-AriaNeural"

    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "audio/output.mp3"'

    os.system(command)

    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load("audio/output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_google(audio,language='en-us')
    except Exception as e:
        print(e)
        return " "
    return query


#speak("hello i am your virtual assistant. how can i assist you today")
#query=take_command()
#print(query)
click_on_chat_button()
while True:
    query = take_command().lower()
    print('\n You: '+ query)
    
    if 'open' in query:
        app_name=query.replace('open','')
        speak('opening' + app_name)
        pyautogui.press('super')
        pyautogui.typewrite(app_name)
        pyautogui.sleep(10)
        pyautogui.press('enter')

    elif 'close tab' in query:
        pyautogui.hotkey('ctrl','w')
        speak('done pal')

    elif 'close' in query:
        pyautogui.hotkey('alt','f4')
        speak('done pal')

    elif 'play' in query:
        song_name=query.replace('play','')
        speak('playing'+song_name+' in youtube')
        pywhatkit.playonyt(song_name)

    elif 'time' in query:
        current_time=datetime.now().strftime('%H:%M:%p')
        speak('current time is ' +current_time)

    elif 'switch' in query:
        pyautogui.hotkey('ctrl','tab')
        speak('done pal')

    elif query == ' ':  
        take_command().lower()

    else:
        sendQuery(query)
        isBubbleLoaderVisible()
        response = retriveData()
        speak(response)
        