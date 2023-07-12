import webbrowser

import pyttsx3

def reproduzir_resposta(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def pesquisar_no_google(pesquisa):
    pesquisa = pesquisa.replace("pesquisar no Google por ", "")
    pesquisa = pesquisa.replace("pesquisar no Google ", "")
    pesquisa = pesquisa.replace("pesquisar ", "")
    pesquisa = pesquisa.replace(" ", "+")
    reproduzir_resposta("Carregando...")
    print("Carregando...")
    url = f"https://www.google.com/search?q={pesquisa}"
    webbrowser.open(url)
