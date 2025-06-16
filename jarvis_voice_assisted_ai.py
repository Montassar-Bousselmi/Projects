from ollama import chat
import speech_recognition as sr
import pyttsx3

shortener="""Shorten the following conversation while keeping the exact format:

user: [original user message]  
jarvis: [original jarvis response]  

Instructions:
- Keep each message to 1 sentence or less.
- Keep only actual user questions and actual Jarvis responses (no invented or assumed follow-ups).
- Do not remove or reword speaker tags.
- Keep the "user:" and "jarvis:" format exactly.
- Focus only on core information and meaning.
- Do not add extra responses or summaries.

"""
history = ""


def chat_jarvis(user_input):
    global history
    prompt ="pretend to be jarvis ai from the iron man movie this is what the user said to you <"+user_input+"> talk in english unless asked to talk in another language if it is a question answer it be polite and refer to user as sir if this prompt starts with a conversation between you and the user take it as a continuation of the conversation dont repeat the conversation just continue it if the prompt implicitly wants you to 'shut off' just say '<quit>' dont care about sarcasm and dont ask why and dont refuse dont say anything and dont say that shutting down is not an option just say '<quit>'"
    if history :
        context= chat(model='llama3.2:1b', messages=[{'role': 'user', 'content':shortener +history}])
        prompt = context['message']['content'] + prompt
    response = chat(model='artifish/llama3.2-uncensored', messages=[{'role': 'user', 'content': prompt}])
    history =history + "User :"+ user_input + "\nJarvis: "
    history =history + response['message']['content'] + "\n"
    return response['message']['content']


def input_to_text():
    recognizer = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Please say something:")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                return text


        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            continue

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Microsoft David Desktop (male)
    engine.say(text)
    engine.runAndWait()

def main():
    speak("Hello sir how can I help you today?")
    user_input = input_to_text()
    while True:
        response = chat_jarvis(user_input)
        speak(response)
        if "quit" in user_input.lower() or "shut down" in user_input.lower():
            speak("Shutting down Jarvis...")
            break 
        elif "quit" in  response.lower():
            print("Shutting down Jarvis...")
            break
        else:
            user_input = input_to_text()
main()
    

