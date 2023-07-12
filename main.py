from comandos.comando_google import pesquisar_no_google
from comandos.comando_abrir_programa import abrir_programa
from comandos.comando_youtube import pesquisar_no_youtube
import speech_recognition as sr
import pyttsx3


def reproduzir_resposta(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


def ouvir_microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando...")
        # Limite de 5 segundos para cada comando de voz
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Analisando...")
        texto = r.recognize_google(audio, language='pt-BR')
        print("Você disse: " + texto)
        return texto.lower()
    except sr.UnknownValueError:
        print("Aguardando...")
        return ''


reproduzir_resposta("Bem-vindo de volta, Edu!")
print("Bem-vindo de volta, Edu!")

while True:
    texto = ouvir_microfone()

    if "lydia pesquisar no google" in texto or "lídia pesquisar no google" in texto or "lidia pesquisar no google" in texto:
        pesquisa = texto.replace("lydia pesquisar no google", "").replace(
            "lídia pesquisar no google", "").replace("lidia pesquisar", "").strip()
        pesquisar_no_google(pesquisa)
    elif "lydia pesquisar no youtube" in texto or "lídia pesquisar no youtube" in texto or "lidia pesquisar no youtube" in texto:
        pesquisa = texto.replace("lydia pesquisar no youtube", "").replace(
            "lídia pesquisar no youtube", "").replace("lidia pesquisar no youtube", "").strip()
        pesquisar_no_youtube(pesquisa)
    elif "lydia abrir" in texto or "lídia abrir" in texto or "lidia abrir" in texto:
        programa = texto.replace("lydia abrir", "").replace(
            "lídia abrir", "").replace("lidia abrir", "").strip()
        abrir_programa(programa)
    elif "sair" in texto:
        reproduzir_resposta("Encerrando...")
        print("Encerrando...")
        break
    else:
        print("Comando não reconhecido.")
