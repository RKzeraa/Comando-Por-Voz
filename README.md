# <img  height="40" width="40" src='https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/python/python-original.svg' > Comando por Voz

Este é um simples script em Python que utiliza a biblioteca `speech_recognition` para permitir a execução de comandos por voz no sistema operacional Windows. O script reconhece comandos específicos e realiza ações correspondentes, como abrir programas ou fechar o script.

## Pré-requisitos
Certifique-se de ter o módulo `pyaudio` instalado no seu ambiente Python.
Certifique-se de ter a biblioteca `pyttsx3` e `speech_recognition` instalada em seu ambiente Python. Você pode instalá-los usando o seguinte comando:

```bash
pip install pyaudio
pip install pyttsx3
pip install SpeechRecognition
```

# Como Usar

1. Execute o script Python.
2. Após a mensagem "Diga alguma coisa:", fale um dos comandos suportados.

## Comandos Suportados

- **Navegador:** Abre o navegador Google Chrome.
- **Bloco de Notas:** Abre o Bloco de Notas.
- **Calculadora:** Abre a Calculadora.
- **Paint:** Abre o Microsoft Paint.
- **CMD:** Abre o Prompt de Comando.
- **VS Code:** Abre o Visual Studio Code.
- **Fechar 'Comandos Suportados':** Finaliza de acordo com o comando que está aberto. _[Exemplo: "Fechar CMD" -> Irá Finalizar o CMD aberto]._
- **Encerrar/Sair:** Encerra a execução do script.

## Exemplo de Uso

```bash
Diga alguma coisa:
(usuário): "Abra o Bloco de Notas"
(script): "Você disse: Abra o Bloco de Notas"
```

## Observações

- Certifique-se de ter um microfone funcional conectado ao seu sistema.
- Os comandos são sensíveis ao idioma e foram configurados para o idioma português brasileiro (`pt-BR`).
- O script foi projetado para sistemas operacionais Windows.
