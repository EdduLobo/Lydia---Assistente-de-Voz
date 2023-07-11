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


def iniciar_assistente():
    print("Olá! Como posso te ajudar hoje?")
    while True:
        comando = ouvir_comando()
        if "sexta-feira" in comando:
            print("Comandos liberados.")
            break
        else:
            print("Aguarde para liberar os comandos.")

    while True:
        comando = ouvir_comando()
        if comando == "abrir":
            os.system("python comandos/abrir_programa.py")
        elif comando == "calcular":
            os.system("python comandos/fazer_calculos.py")
        elif comando == "pesquisar":
            os.system("python comandos/fazer_pesquisa.py")
        elif comando == "reproduzir":
            os.system("python comandos/reproduzir_musica.py")
        elif comando == "sair":
            print("Encerrando o assistente...")
            break
        else:
            print("Comando inválido. Por favor, tente novamente.")


if __name__ == "__main__":
    iniciar_assistente()
