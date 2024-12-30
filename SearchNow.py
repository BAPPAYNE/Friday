import pywhatkit
import webbrowser
from TakeCommand import speak
from mediawiki import MediaWiki
import wikipedia as googleScrap


def searchGoogle(query):
    if "google" in query:
        query = query.replace("friday","").strip()
        query = query.replace("google search","").strip()
        query = query.replace("google","").strip()
        # speak("This is what i found in google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("Whoops! Looks like I couldn't find anything to talk about.")


def searchYouTube(query):
    if "youtube" in query:
        speak("This is what i found.")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("friday","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done")

def searchWikipedia(query):
    if "search" in query:
        speak("Searching from wikipedia...")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("friday","")
        results = MediaWiki().summary(query,sentences = 2)
        speak("According to wikipedia...")
        print(results)
        speak(results)


    
