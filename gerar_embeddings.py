import requests
url = "http://localhost:11434/api/embeddings"
payload = {
    "model": "nomic-embed-text",  
    "prompt": "Este é um texto simples para gerar embeddings."
}
resposta = requests.post(url, json=payload).json()
vetor = resposta["embedding"]
print(f"Tamanho do vetor: {len(vetor)}")
print(f"Valores iniciais: {vetor[:5]}")