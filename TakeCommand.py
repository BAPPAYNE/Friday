import pyttsx3
import speech_recognition
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")

# japaneese_voice_female = voices[3]
english_voice_female = voices[2]
english_voice_male = voices[0]

engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 180)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand() :
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source :
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 300
        print("Listening...")
        audio = r.listen(source,0,4)
        
    try :
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")
        # query = input("Command : ")
    except Exception as  e :
        print("Say that again.")
        return "None"
    return query
    
    