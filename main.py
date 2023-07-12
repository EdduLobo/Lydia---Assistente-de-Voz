import speech_recognition as sr
import keyboard
import time

import pyttsx3

def reproduzir_resposta(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

from comandos.comando_google import pesquisar_no_google
from comandos.comando_youtube import pesquisar_no_youtube
from comandos.comando_abrir_programa import abrir_programa

def aguardar_pressionar_botao():
   while True:
       if keyboard.is_pressed("'"):
           while keyboard.is_pressed("'"):
               pass
           return
       time.sleep(0.1)

def ouvir_microfone():
   aguardar_pressionar_botao()

   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("Diga algo...")
       audio = r.listen(source, phrase_time_limit=5)  # Limite de 5 segundos para cada comando de voz
   try:
       print("Analisando o áudio...")
       texto = r.recognize_google(audio, language='pt-BR')
       reproduzir_resposta("carregando... " + texto)
       print("Você disse: " + texto)
       return texto.lower()
   except sr.UnknownValueError:
       reproduzir_resposta("erro...")
       print("Não entendi o que você disse.")
       return ''
   
reproduzir_resposta("Bem-vindo(a) ao assistente de desktop!")
print("Bem-vindo(a) ao assistente de desktop!")

while True:
   aguardar_pressionar_botao()
   texto = ouvir_microfone()

   if "pesquisar no google" in texto:
       pesquisar_no_google(texto)
   elif "pesquisar no youtube" in texto:
       pesquisar_no_youtube(texto)
   elif "abrir" in texto:
       abrir_programa(texto)
   elif "sair" in texto:
       reproduzir_resposta("Encerrando o assistente...")
       print("Encerrando o assistente...")
       break
   else:
       reproduzir_resposta("Comando não reconhecido.")
       print("Comando não reconhecido.")
