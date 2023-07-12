import subprocess
import pyttsx3


def reproduzir_resposta(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


programas = {
    "bloco de notas": "notepad.exe",
    "calculadora": "calc.exe",
    "word": "WINWORD.EXE",
    "opera": r"C:\Users\Viing\AppData\Local\Programs\Opera GX\launcher.exe",

    # Adicione mais programas conforme necessário
}


def abrir_programa(programa):

    programa_encontrado = False
    for key in programas.keys():
        if key in programa:
            nome_programa = programas[key]
            try:
                subprocess.Popen(nome_programa)
                programa_encontrado = True
                break
            except FileNotFoundError:
                reproduzir_resposta(
                    f"O programa '{nome_programa}' não foi encontrado.")
                print(f"O programa '{nome_programa}' não foi encontrado.")

    if not programa_encontrado:
        reproduzir_resposta(
            "O programa especificado não está na lista de programas suportados.")
        print("O programa especificado não está na lista de programas suportados.")
