import speech_recognition as sc
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sc.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sc.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sunny' in command:
                command = command.replace('sunny','')
                print(command)



    except:
        pass
    return command

def run_sunny():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('current time is' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is','')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sure darling, let us go')
    elif 'are you single' in command:
        talk('sorry, i am in a relationship with my man sunil')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'how are you' in command:
        talk('i am good, thank you, what about you')
    else:
        talk('please say it again')

while True:
    run_sunny()


run_sunny()

