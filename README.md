Markdown
# Geração de Embeddings com Ollama

Este repositório foi criado para a atividade de geração de embeddings utilizando o Ollama rodando localmente com Python.

O script é simples: ele conecta na API local do Ollama, envia um texto de exemplo e devolve o tamanho do vetor gerado junto com os primeiros valores numéricos.

## Como rodar o projeto

Antes de executar, certifique-se de ter o [Python](https://www.python.org/) e o [Ollama](https://ollama.com/) instalados na sua máquina.

1. **Baixe o modelo de texto:**
   Abra o seu terminal e rode o comando abaixo para baixar o modelo no Ollama:
   ```bash
   ollama pull nomic-embed-text
Instale a dependência do Python:
No terminal, instale a biblioteca requests, que faz a comunicação com a API:

Bash
pip install requests
Execute o script:
Com o Ollama rodando em segundo plano, execute o arquivo Python:

Bash
python gerar_embeddings.py
Exemplo de saída
Se tudo estiver configurado corretamente, o script vai retornar algo assim no seu console:

Plaintext
Tamanho do vetor: 768
Valores iniciais: [0.5887492299079895, 1.458122730255127, -2.715240478515625, -1.5796717405319214, 0.2747862935066223]
