import webbrowser
import pyttsx3

def reproduzir_resposta(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    
def pesquisar_no_youtube(pesquisa):
    pesquisa = pesquisa.replace("pesquisar no YouTube por ", "")
    pesquisa = pesquisa.replace("pesquisar no YouTube ", "")
    pesquisa = pesquisa.replace(" ", "+")
    reproduzir_resposta("Carregando...")
    print("Carregando...")
    url = f"https://www.youtube.com/results?search_query={pesquisa}"
    webbrowser.open(url)
