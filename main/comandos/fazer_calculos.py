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


def fazer_calculos():
    print("Digite a Operação (+, -, *, /): ")
    operacao = ouvir_comando()

    num1 = 0
    num2 = 0

    if operacao in ["+", "-", "*", "/"]:
        print("Digite o primeiro número: ")
        num1 = float(ouvir_comando())
        print("Digite o segundo número: ")
        num2 = float(ouvir_comando())

    resultado = 0

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Divisão por zero não é possível"
    else:
        resultado = "Operação inválida"

    print("Resultado:", resultado)


fazer_calculos()
