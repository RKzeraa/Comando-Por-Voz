import speech_recognition as sr
import os
import pyttsx3

# Dicionário mapeando comandos para os aplicativos correspondentes
comandos_aplicativos = {
    "navegador": "chrome.exe",
    "bloco de notas": "notepad.exe",
    "calculadora": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "vs code": "code.exe"
}

# Lista para armazenar os processos dos aplicativos abertos
processos_abertos = []

# Função responsável por ouvir e reconhecer a fala
def ouvir_microfone(engine):
    # Habilita o microfone para ouvir o usuário
    microfone = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            # Chama a função de redução de ruído disponível na speech_recognition
            microfone.adjust_for_ambient_noise(source)

            # Avisa ao usuário que está pronto para ouvir
            print("Diga alguma coisa: ")

            try:
                # Armazena a informação de áudio na variável
                audio = microfone.listen(source, timeout=500000)  # Adicionando um timeout de 5 segundos

                # Passa o áudio para o reconhecedor de padrões do speech_recognition
                frase = microfone.recognize_google(audio, language='pt-BR')

                # Após alguns segundos, retorna a frase falada
                print("Você disse: " + frase)

                # Transforma a frase em minúsculas
                frase = frase.lower()

                if "fechar" in frase:
                    # Verifica se há outros comandos na frase
                    for comando, aplicativo in comandos_aplicativos.items():
                        if comando in frase:
                            # Fecha o aplicativo se estiver aberto
                            if aplicativo in processos_abertos:
                                os.system(f"taskkill /F /IM {aplicativo}")
                                processos_abertos.remove(aplicativo)
                                resposta = f"Aplicativo {comando} fechado."
                                print(resposta)
                                falar(engine, resposta)

                    # Se "sair" ou "encerrar script" estiver presente na frase, encerra o script
                    if "sair" in frase or "encerrar" in frase or "encerrar script" in frase:
                        resposta = "Encerrando o programa..."
                        print(resposta)
                        falar(engine, resposta)
                        return

                else:
                    # Executa os comandos de abrir aplicativos
                    for comando, aplicativo in comandos_aplicativos.items():
                        if comando in frase:
                            os.system(f"start {aplicativo}")
                            processos_abertos.append(aplicativo)
                            resposta = f"Aplicativo {comando} aberto."
                            print(resposta)
                            falar(engine, resposta)

                    # Se "sair" ou "encerrar script" estiver presente na frase, encerra o script
                    if "sair" in frase or "encerrar" in frase or "encerrar script" in frase:
                        resposta = "Encerrando o programa..."
                        print(resposta)
                        falar(engine, resposta)
                        return

            except sr.UnknownValueError:
                resposta = "Não entendi. Por favor, fale algo."
                print(resposta)
                falar(engine, resposta)

# Função para converter texto em fala
def falar(engine, texto):
    engine.say(texto)
    engine.runAndWait()

# Configurando a engine de síntese de voz
engine = pyttsx3.init()

# Exemplo de uso
ouvir_microfone(engine)
