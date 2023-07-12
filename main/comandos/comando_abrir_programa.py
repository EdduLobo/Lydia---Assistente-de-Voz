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
    programa = programa.replace("abrir ", "").lower()

    if programa in programas:
        nome_programa = programas[programa]
        try:
            subprocess.Popen(nome_programa)
        except FileNotFoundError:
            reproduzir_resposta(f"O programa '{nome_programa}' não foi encontrado.")
            print(f"O programa '{nome_programa}' não foi encontrado.")
    else:
        reproduzir_resposta("O programa especificado não está na lista de programas suportados.")
        print("O programa especificado não está na lista de programas suportados.")
        
