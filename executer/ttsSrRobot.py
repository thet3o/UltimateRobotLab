# Importing required modules
# importing pyttsx3
from gettext import find
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
#numeri casuali
import random
from random import choice



listaFrasi = ["muovi il braccio destro","alza il dito medio","scuoti la testa","muovi la mano destra","apri la mano sinistra","muovi il braccio sinistro"]
listaErrori = ["Puoi ripetere","ripeti per favore","ripetilo","non ho capito","Non mi è chiaro","potresti rifrasarmelo?","Non ho compreso"]
listaYes = ["ok, lo faccio", "procedo", "vamos", "eseguo", "capito","daje"]
listaNo = ["ok sto fermo", "mi arresto", "non faccio nulla", "non mi muovo", "ok stop"]


comandi = {
    "muovi il braccio destro": "moveRightArm",
    "alza il dito medio": "raiseMiddleFinger",
    "muovi la mano destra": "moveRightHand",
    "apri la mano sinistra": "openLeftHand",
    "muovi il braccio sinistro": "moveLeftArm",
    "scuoti la testa":  "shakeYourHead"

}



def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Ascolto...')
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Riconoscimento")
            # Recognizing audio using google api
            Query = r.recognize_google(audio,language="it-IT").lower()
            print("Questo è ciò che ho capito='", Query, "'")
        except Exception as e:
            print(e)
            print("Prova a ripetere")
            # returning none if there are errors
            return "None"
    # returning audio as text
    import time
    time.sleep(2)
    return Query



def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    voice_id = 'italian'
    engine.setProperty('voice', voice_id)
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()

def errori():
    a = random.randint(0,len(listaErrori)-1)
    Speak(listaErrori[a])

def okComandi():

    a = random.randint(0,len(listaYes)-1)
    Speak(listaYes[a])

def noComandi():

    a = random.randint(0,len(listaNo)-1)
    Speak(listaNo[a])


def scegliRisposta(lista):
    risposta = choice(lista)
    Speak(risposta)




"""
while counterErrori < 3:
    command = take_commands()
    controlloPresenza = False

    for i in listaFrasi:
        #print(i)
        if i.casefold() == command.casefold():
            controlloPresenza = True
            Speak("mi hai detto: "+i+"?")
            while not controllo:
                answer = take_commands()
            #sarebbe no
                if "papavero" in answer:
                    controllo = True
                    Speak("ok sto fermo")
                #sarebbe sì
                elif "cornetto" in answer:
                    controllo = True
                    Speak("ok lo faccio")
                else:
                    errori()
    
    if not controlloPresenza:
        errori()
        counterErrori = counterErrori + 1

Speak("mi metto in pausa")
"""



counterErrori = 0
controllo = False
controlloPresenza = False


while True:
    command = take_commands()
    a =  command.find("contenitore marrone")
    if a != -1:
        Speak("mi attivo")
        print("attivo")
        counterErrori = 0
        while counterErrori < 10:
            command = take_commands()
            controlloPresenza = False
            controllo = False
            for i in listaFrasi:
                #print(i)
                if command.find(i) != -1:
                    controlloPresenza = True
                    Speak("mi hai detto: "+i+"?")
                    while not controllo:
                        answer = take_commands()
                    #sarebbe no
                        if "no" in answer:
                            controllo = True
                            #noComandi()
                            scegliRisposta(listaNo)
                        #sarebbe sì
                        elif answer.find("confermo") != -1:
                            controllo = True
                            print(comandi.get(i))
                            #okComandi()
                            scegliRisposta(listaYes)
                        else:
                            #errori()
                            scegliRisposta(listaErrori)
            
            if not controlloPresenza:
                
                if "fermati" in command:
                    counterErrori = 10
                else:
                    errori()
                    counterErrori = counterErrori + 1
        Speak("mi metto in pausa")
        
        

    

        


