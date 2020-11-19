import speech_recognition as sr 
import playsound 
from gtts import gTTS 
import os 
import wolframalpha 
from selenium import webdriver 



num = 1
def assistant_speaks(output): 
          global num 
          
          num += 1
          print("PerSon : ", output) 

          toSpeak = gTTS(text = output, lang ='en', slow = False) 
          file = str(num)+".mp3" 
          toSpeak.save(file) 
          

          playsound.playsound(file, True) 
          os.remove(file) 



def get_audio(): 

          rObject = sr.Recognizer() 
          audio = '' 

          with sr.Microphone() as source: 
                    print("Speak...") 
                    
                    
                    audio = rObject.listen(source, phrase_time_limit = 3) 
          print("Stop.") 

          try: 

                    text = rObject.recognize_google(audio, language ='en-US') 
                    print("You : ", text) 
                    return text 

          except: 

                    assistant_speaks("Could not understand your audio, PLease try again !") 
                    return 0



if __name__ == "__main__": 
          assistant_speaks("What's your name?") 
          name ='Human'
          name = get_audio() 
          assistant_speaks("Hello, " + name + '.') 
          
          while(1): 

                    assistant_speaks("What can i do for you?") 
                    text = get_audio().lower() 

                    if text == 0: 
                              continue

                    elif "detect environment" in str(text) or "define environment" in str(text): 
                              assistant_speaks("starting in a second")
                              import ObjectDetectionAPI
                              break
                    elif "break" in str(text):
                        assistant_speaks("Have a Good Day")
                        break
                    elif "not well" in str(text):
                        assistant_speaks("ok, calling ambulance")
                        import MAILALERT
                   
