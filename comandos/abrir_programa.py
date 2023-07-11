import os
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


def abrir_programa():
    print("Qual programa você deseja abrir?")
    programa = ouvir_comando()

    caminhos_programas = {
        "bloco de notas": "C:\\Windows\\System32\\notepad.exe",
        "calculadora": "C:\\Windows\\System32\\calc.exe",
        "explorador de arquivos": "C:\\Windows\\explorer.exe",
        "opera": "C:\\Users\\Viing\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
        # Adicione mais programas e seus caminhos conforme necessário
    }

    if programa.lower() in caminhos_programas:
        caminho = caminhos_programas[programa.lower()]
        os.startfile(caminho)
    else:
        print("Programa não encontrado.")


def iniciar_assistente():
    print("Olá! Como posso te ajudar hoje?")

    while True:
        comando = ouvir_comando()

        if comando == "abrir":
            abrir_programa()
        elif comando == "sair":
            print("Encerrando o assistente...")
            break
        else:
            print("Comando inválido. Por favor, tente novamente.")


if __name__ == "__main__":
    iniciar_assistente()
