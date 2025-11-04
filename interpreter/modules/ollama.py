import requests
import json

class Ollama():
    @staticmethod
    def generate(prompt, show='False'):
        url = "http://localhost:11434/api/generate"
        content = {"model": "mistral", "prompt": prompt, "stream":False}
        requestResponse = requests.post(url, json=content).json()
        data = requestResponse


        finalResponse=data["response"]

        if show == "False":
            return finalResponse
        else:
            print(finalResponse)

    def chat(prompt, chatFile, show):
        f = open(f'{chatFile}.memo', "a")
        f.write(f'\nUser: {prompt}')
        chatHistory = open(f'{chatFile}.memo', "r").read()
        url = "http://localhost:11434/api/generate"
        content = {"model": "mistral", "prompt": f'Use the chat history as a base for the conversation: {chatHistory} New prompt: {prompt}', "stream":False}
        requestResponse = requests.post(url, json=content).json()
        data = requestResponse


        finalResponse=data["response"]
        f.write(f"\nOllama model: {finalResponse}")
        if show == "False":
            pass
        else:
            print(finalResponse)

    def clearMemo(target):
        f = open(target, "w")
        f.write(f'')




if __name__ == "__main__":
    option = 3
    if option == 1:
        Ollama.generate('Escreva duas letras aleatórias.', "True")
    if option == 2:
        Ollama.chat('Qual o mais BARATO para se viver?', "chat1.memo", "True")
    if option == 3:
        Ollama.clearMemo("chat1.memo")