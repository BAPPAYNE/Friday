from TakeCommand import speak,takeCommand

if __name__ =="__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe(query)

            while True:
                query = takeCommand().lower()
                if "turn off" in query:
                    speak("Okay, Call me anytime")
                    break
                if "shutdown" in query:
                    speak("Okay, shutting down")
                    break
                elif "what time is it" in query:
                    from time import getTime
                    getTime()
                elif "what is your name" in query:
                    speak("My name is Friday...")
                elif "how are you" in query:
                    speak("Never better")
                elif "how r u" in query:
                    speak("Good")
                elif "shutup" in query:
                    speak("Okay")
                
                #Search
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYouTube
                    searchYouTube(query)
                elif "search" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                    pass