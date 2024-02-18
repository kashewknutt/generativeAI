import speech_recognition as sr

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        audio = None
        while audio is None:
            try:
                print("LOG: I am listening")
                audio = r.listen(source, timeout=5) 
            except sr.WaitTimeoutError:
                pass

        try:
            text = r.recognize_google(audio, language='en-in')
            print("Speak: {}".format(text))
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech Recognition service; {0}".format(e))
