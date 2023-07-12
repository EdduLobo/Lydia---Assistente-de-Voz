# Lydia - Assistente de Voz

Lydia é um assistente de voz desenvolvido em Python que permite executar comandos por meio de reconhecimento de voz. Com o Lydia, você pode pesquisar no Google, pesquisar no YouTube e abrir programas no seu computador usando apenas comandos de voz.

Pré-requisitos
Certifique-se de ter o seguinte instalado em seu ambiente de desenvolvimento:
Python 3.x
Bibliotecas: speech_recognition, pyttsx3

Instalação

Clone este repositório para o seu ambiente local:

https://github.com/EdduLobo/Desktop-Assistente

Navegue até o diretório do projeto:

cd lydia-assistente

Instale as dependências do projeto:

pip install -r requirements.txt

Utilização

Execute o arquivo main.py:

python main.py

O Lydia irá aguardar por comandos de voz.

Quando solicitado, fale o comando desejado:

Para pesquisar no Google: "Lydia pesquisar no Google {sua pesquisa}"
Para pesquisar no YouTube: "Lydia pesquisar no YouTube {sua pesquisa}"
Para abrir um programa: "Lydia abrir {nome do programa}"
Para encerrar o assistente: "sair"

O Lydia processará o comando de voz e executará a ação correspondente.

Personalização

Você pode personalizar o Lydia adicionando mais comandos e funcionalidades de acordo com suas necessidades. Para isso, siga as etapas abaixo:

Crie um novo arquivo de comando na pasta comandos com o formato comando_novo.py.
Implemente a lógica do novo comando no arquivo criado. Você pode se basear nos arquivos existentes comando_abrir_programa.py, comando_google.py e comando_youtube.py.
No arquivo main.py, importe a função do novo comando e adicione uma nova condição no loop while True para identificar e executar o novo comando.

Exemplo de novo comando no arquivo main.py

from comandos.comando_novo import executar_comando_novo

...

while True:
texto = ouvir_microfone()

    if "lydia novo comando" in texto:
        executar_comando_novo()
    # ...

    Reinicie o Lydia para que as alterações sejam aplicadas.

Uma versão executavel do projeto está disponível na pasta "main".

Este projeto está sendo desenvolvido com o objetivo de aprender os fundamentos básicos de Python e aprimorar meu conhecimento nessa linguagem. Estou empolgado em explorar as possibilidades do Python e aplicá-las na construção deste assistente de desktop. Espero que vocês também se interessem e apreciem o projeto!
