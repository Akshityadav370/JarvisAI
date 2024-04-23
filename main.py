import random
import webbrowser

import speech_recognition as sr
import os
import openai
import datetime

chatStr = ""

def chat(query):
    global chatStr
    openai.api_key = os.getenv("OPENAI_API_KEY")
    chatStr += f"Harry: {query}\n Jarvis:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
def ai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    text = f"OpenAI response for prompt: {prompt}\n"
    # chatStr +=
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Akshit: {prompt}\n Jarvis:",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/prompt- {random.randint(1, 2343243)}", "w") as f:
        f.write(text)

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing ....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Error Vachindi. sorry from Jarvis"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Jarvis A.I")
    while True:
        print("Listening...")
        command = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in command.lower():
                say(f"Opening {site[0]} sir")
                webbrowser.open(site[1])
        if "open music" in command:
            musicPath = "/Users/akshit/Downloads/23.mp3"
            os.system(f"open {musicPath}")
        elif "the time" in command:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"sir the time is {strfTime}")
        elif "open facetime".lower() in command.lower():
            os.system(f"open /System/Applications/FaceTime.app")
        elif "using artifical intelligence".lower() in command.lower():
            ai(prompt=command)
        else:
            chat(command)
        # say(command)

