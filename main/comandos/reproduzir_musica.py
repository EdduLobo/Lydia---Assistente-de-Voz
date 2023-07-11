import webbrowser
import speech_recognition as sr


def ouvir_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Processando...")
        comando = r.recognize_google(audio, language='pt-BR')
        return comando.lower()
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender o comando.")
        return ""
    except sr.RequestError:
        print("Desculpe, ocorreu um erro na comunicação com o serviço de reconhecimento de voz.")
        return ""


def reproduzir_musica():
    print("Digite o nome da música: ")
    musica = ouvir_comando()
    pesquisa = musica.replace(" ", "+")
    webbrowser.open(f"https://www.youtube.com/results?search_query={pesquisa}")


reproduzir_musica()
