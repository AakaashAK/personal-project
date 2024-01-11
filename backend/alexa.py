import requests
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk('listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
                if 'stop' in command:
                    requests.post('http://localhost:5000/stop')
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        talk("Sorry, I didn't understand that.")
        command = ""
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        talk("Sorry, my speech service is down.")
        command = ""
    return command
def run_alexa():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)    
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'where is' in command:
            place = command.replace('where is', '')
            info = wikipedia.summary(place, 2)
            print(info)
            talk(info)
        elif 'what is' in command:
            place = command.replace('what is', '')
            info = wikipedia.summary(place, 2)
            print(info)
            talk(info)                
        elif 'whatsapp message' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            h, m = time.split(':')
            talk("what message do you want to send")
            message = take_command()
            print(message)
            talk("say me the number")
            number = take_command()
            print('+91' + number)
            pywhatkit.sendwhatmsg('+91' + number, message, int(h), int(m) + 2)
        else:
            talk('Please say the command again.')

talk('Hi Aakaash am your personal assistant jarvis')
#print('Hi Aakaash am your personal assistant jarvis')

while True:
    command = take_command()
    if 'terminate' in command or 'stop' in command:
        talk('I Hope. I have helped you. Goodbye!')
        print('I Hope. I have helped you. Goodbye!')
        break
    else:
        run_alexa()
