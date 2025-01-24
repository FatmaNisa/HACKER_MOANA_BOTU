import speech_recognition

def konuş_tr():
    mikrofon=speech_recognition.Microphone()
    kayıt=speech_recognition.Recognizer()

    with mikrofon as ses:
        kayıt.adjust_for_ambient_noise(ses)
        fatma=kayıt.listen(ses)
        try:
            return kayıt.recognize_google(fatma,language="tr-TR")
        except:
            return "dediğini anlayamadım lütfen tekrar deneyin"
    


def konuş_en():
    mikrofon=speech_recognition.Microphone()
    kayıt=speech_recognition.Recognizer()

    with mikrofon as ses:
        kayıt.adjust_for_ambient_noise(ses)
        fatma=kayıt.listen(ses)
        try:
            return kayıt.recognize_google(fatma,language="en-US")
        except:
            return "I didn't understand what you said, please try again."

if __name__=="__main__":
    print("şimdi konuşabilirsiniz-you can talk now")
    ses=konuş_tr()
    print(ses)