import speech_recognition as sr
import pyttsx3 
r = sr.Recognizer()
file = open("voice.txt","w+")
lis=[]
def closefunc():
    file.close()
    exit()

while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            if(MyText=='start' or MyText=='Start'):
                print("Listening. . . . ")
                while(1):
                    try:
                        with sr.Microphone() as source2:
                            r.adjust_for_ambient_noise(source2, duration=0.2)
                            audio = r.listen(source2)
                            MyText = r.recognize_google(audio)
                            MyText = MyText.lower()
                            print(MyText)
                            if(MyText=='stop' or  MyText=='Stop' or MyText=='exit' or MyText=='Exit'):
                                print("Listening Stopped....")
                                closefunc()
                            lis.append(MyText)
                            file.write(MyText+'\n')
                    except sr.RequestError as e:
                        print("Could not request results; {0}".format(e))
          
                    except sr.UnknownValueError:
                        print("unknown error occured")
              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")

    
    
