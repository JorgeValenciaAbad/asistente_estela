import pyttsx3, wikipedia,pywhatkit, datetime, pyjokes,webbrowser
import speech_recognition as sr
import requests
from selenium  import webdriver
from selenium.webdriver.common.keys import Keys

name = "estela"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

#Funcion para que la asistente puede hablar
def hablar(text):

    engine.setProperty('rate', 115)
    engine.say(text)
    engine.runAndWait()
#Funcion para identificar a los Pokémons
def pokemon(poke):
    res = requests.get('https://pokeapi.co/api/v2/pokemon/'+poke.strip())
    print('El pokemon es '+ res.json()['name'])
    hablar('El pokemon es ' + res.json()['name'])
#Funcion para configurar el navedador
def navegador():
    nav = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\firefox.exe"
    browser = webdriver.Firefox(executable_path=nav)
    browser.maximize_window()
    return browser
#Funcion para escuchar
def listen():
    try:
        with sr.Microphone() as source:
            print("escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language='es')
            rec = rec.lower()
            return rec

    except Exception as e:
        pass
        print(e)


#Funcion para correr al asistente
def run_Estela():

    hablar("Hola me llamo Estela soy tu asistente virtual")
    cont = 0
    bandera = True
    while bandera:
        rec = listen()
        if name in rec:
            rec = rec.replace(name, '')

            if 'reproduce' in rec:
                music = rec.replace('reproduce', '')
                print("reproduciendo " + music + " ...")
                hablar("reproduciendo " + music)
                pywhatkit.playonyt(music)

            elif 'dime el pokémon' in rec:
                poke = rec.replace('dime el pokémon', '')
                pokemon(poke)
            elif 'navegador' in rec:
                navegador().get('https://www.google.com')
            elif 'youtube' in rec:
                navegador().get('https://www.youtube.com')
            elif 'busca por wikipedia' in rec:
                search = rec.replace('busca por wikipedia', '')
                wikipedia.set_lang('es')
                wiki = wikipedia.summary(search, 2)
                print(search + ' ' + wiki)
                hablar(wiki)
            elif 'busca' in rec:
                busca = rec.replace('busca', '')
                print("Buscando " + busca + " ...")
                hablar("Buscando " + busca)
                pywhatkit.search(busca)
            elif 'cuenta un chiste' in rec:
                joke = pyjokes.get_joke(language='es', category='all')
                print(joke)
                hablar(joke)
            elif 'hora' in rec:
                hora = datetime.datetime.now().strftime('%H:%M %p')
                hablar('Son las' + hora)
            elif 'día' in rec:
                dia = datetime.datetime.now().strftime('%d %m %Y')
                print(dia)
                hablar('Hoy es' + dia)
            elif 'di' in rec:
                talk = rec.replace('di', '')
                hablar(talk)
            elif 'stop'in rec:
                hablar("Adios amigos disfrutar del dia")
                bandera=False
        else:
            print("No entiendo")
            hablar("No entiendo")

            if cont == 1:
                hablar("Algo mas?")
        cont=1



if __name__ == '__main__':
    run_Estela()
