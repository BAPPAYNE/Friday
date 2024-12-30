import datetime
from TakeCommand import speak


def greetMe(query):
    if "wake up" in query:
        hour = int(datetime.datetime.now().hour)
        if hour>0 and hour<=5:
            speak("Good Morning!, You awake early? How can i help you?")
        elif hour>=8 and hour<=11:
            speak("Good Morning! How can i help you?")
        elif hour>11 and hour<=16:
            speak("Good Afternoon! How can i help you?")
        elif hour>16 and hour<=19:
            speak("Hey!, Its early evening How can i help you?")
        elif hour>19 and hour<21:
            speak("Good Evening! How can i help you?")
        elif hour>21 and hour<=22:
            speak("Good Night! How can i help you?")
        elif hour>22 and hour<24:
            speak("Good Night! How can i help you?")



formatted_now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
print("Current Date and Time in 12-hour format:", formatted_now)