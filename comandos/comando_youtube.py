import webbrowser
import pyttsx3


def reproduzir_resposta(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


def pesquisar_no_youtube(pesquisa):
    reproduzir_resposta("Carregando...")
    print("Carregando...")
    url = f"https://www.youtube.com/results?search_query={pesquisa}"
    webbrowser.open(url)
