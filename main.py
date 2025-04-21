import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# used to recognize voice speech
listener = sr.Recognizer()
# text to speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # get voice properties
engine.setProperty('voice', voices[1].id)  # set voice property to female voice


# run function to allow alexa to respond
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        # find source of audio
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')  # the word alexa will be removed before command is printed
                print(command)

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        # print('playing...')
        pywhatkit.playonyt(song)  # open browser to play song on YouTube

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)  # summarize the wikipedia search
        print(info)
        talk(info)

    elif 'where is' in command:
        place = command.replace('where is', '')
        info = wikipedia.summary(place, 3)  # summarize the wikipedia search
        print(info)
        talk(info)

    elif 'what is' in command:
        thing = command.replace('what is', '')
        info = wikipedia.summary(thing, 3)  # summarize the wikipedia search
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk("sorry, I'm in a relationship with Chat GPT")

    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    else:
        talk("Please say that again, I didn't get that.")


# keep alexa running until input is false
while True:
    # function call
    run_alexa()
