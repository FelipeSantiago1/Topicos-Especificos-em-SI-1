import requests
url = "http://localhost:11434/api/embeddings"
payload = {
    "model": "nomic-embed-text",  
    "prompt": "Una canción para tu hijo, para tu hija. Para esa persona a la que llevarías en brazos hasta que quiera correr.Y a la que, aunque duela, dejarás volar."
}
resposta = requests.post(url, json=payload).json()
vetor = resposta["embedding"]
print(f"Tamanho do vetor: {len(vetor)}")
print(f"Valores iniciais: {vetor[:5]}")
