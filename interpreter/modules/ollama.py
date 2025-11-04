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


if __name__ == "__main__":
    Ollama.generate('Escreva duas letras aleatórias.', "True")