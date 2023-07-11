import subprocess
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


def fazer_pesquisa():
    print("Digite o termo da pesquisa: ")
    termo = ouvir_comando()
    pesquisa = termo.replace(" ", "+")

    # Definindo o caminho para o executável do Opera GX
    caminho_opera_gx = r"C:\Users\Viing\AppData\Local\Programs\Opera GX\launcher.exe"

    try:
        # Abrindo a URL de pesquisa com o Opera GX usando subprocess.run()
        subprocess.run(
            [caminho_opera_gx, f"https://www.google.com/search?q={pesquisa}"])
    except FileNotFoundError:
        print("Caminho para o Opera GX inválido ou Opera GX não encontrado.")


fazer_pesquisa()
