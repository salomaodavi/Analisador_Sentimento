# 🐍 Analisador de Sentimento Básico com Python 🧠

---

## Conecte-se comigo! 🤝

Ficarei feliz em conectar e trocar ideias! Você pode me encontrar no LinkedIn:

[![Meu LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/salomao-davi)

---

Boas-vindas ao meu projeto de Analisador de Sentimento Básico! 🎉 Este é um exemplo simples, mas eficaz, de como podemos usar Python para mergulhar no mundo do Processamento de Linguagem Natural (PLN). O objetivo é pegar uma frase e determinar se o sentimento expresso nela é positivo, negativo ou neutro.

Este projeto é perfeito para quem está começando em PLN ou quer ver uma aplicação prática de análise de texto de forma rápida e descomplicada. 🚀

## 🌟 O que este projeto faz?

Imagine que você quer entender o "humor" de um texto. É exatamente isso que este pequeno script faz!

* Recebe uma frase: Você digita a frase que quer analisar.
  
* Analisa o sentimento: O código processa a frase usando uma lógica simples baseada em palavras-chave (para o exemplo em português) ou uma biblioteca externa (para o exemplo em inglês).
  
* Retorna o veredito: Ele te diz se a frase tem um sentimento Positivo 😊, Negativo 😠 ou Neutro 😐.

## ⚙️ Como rodar o projeto

Você pode rodar este projeto de duas formas: com a biblioteca TextBlob (ótima para inglês) ou com uma lógica manual simplificada (adaptável para português).

Opção 1: Com ``TextBlob`` (para análises em Inglês 🇬🇧)

## 1. Pré-requisitos:

* Certifique-se de ter o Python 3.x instalado na sua máquina.

* Instale a biblioteca ``TextBlob``:

````
pip install textblob
````

* Baixe os dados necessários do ``TextBlob``:
````
python -m textblob.download_corpora
````

## 2. Clone o repositório (ou copie o código para um arquivo ``.py``):

````
git clone [LINK_DO_SEU_REPOSITORIO]
cd [NOME_DA_PASTA_DO_PROJETO]
````

## 3. Execute o script:
````
python analisador_sentimento_en.py
````

(Assumindo que você salvou o código como ``analisador_sentimento_en.py``)

## 4. Interaja! Digite suas frases em português e confira o sentimento. Para sair, digite ``sair``.

# 💻 O Código

Para Análise em Inglês (usando ``TextBlob``)

# Python
```` 
# pip install textblob
# python -m textblob.download_corpora

from textblob import TextBlob

def analisar_sentimento(texto):
    """
    Analisa o sentimento de um texto e retorna 'Positivo', 'Negativo' ou 'Neutro'.
    """
    analise = TextBlob(texto)
    if analise.sentiment.polarity > 0:
        return "Positivo"
    elif analise.sentiment.polarity < 0:
        return "Negativo"
    else:
        return "Neutro"

if __name__ == "__main__":
    print("--- Analisador de Sentimento Básico (Inglês) ---")
    while True:
        frase = input("Digite uma frase (ou 'sair' para encerrar): ")
        if frase.lower() == 'sair':
            break
        
        sentimento = analisar_sentimento(frase)
        print(f"Sentimento da frase: {sentimento}\n")
````

Para Análise em Português (lógica simplificada)

# Python
````
def analisar_sentimento_pt(texto):
    """
    Analisa o sentimento de um texto em português de forma básica.
    Esta é uma implementação simplificada e não robusta para português.
    """
    texto_lower = texto.lower()
    
    palavras_positivas = ["bom", "ótimo", "excelente", "maravilhoso", "feliz", "amo", "gosto", "incrível"]
    palavras_negativas = ["ruim", "péssimo", "horrível", "triste", "odeio", "não gosto", "problema"]

    score = 0
    for palavra in palavras_positivas:
        if palavra in texto_lower:
            score += 1
    
    for palavra in palavras_negativas:
        if palavra in texto_lower:
            score -= 1
            
    if score > 0:
        return "Positivo"
    elif score < 0:
        return "Negativo"
    else:
        return "Neutro"

if __name__ == "__main__":
    print("--- Analisador de Sentimento Básico (Português) ---")
    while True:
        frase = input("Digite uma frase (ou 'sair' para encerrar): ")
        if frase.lower() == 'sair':
            break
        
        sentimento = analisar_sentimento_pt(frase)
        print(f"Sentimento da frase: {sentimento}\n")
````

## 🚀 Próximos passos e possíveis melhorias

Este projeto é um ponto de partida! Aqui estão algumas ideias para expandi-lo e torná-lo ainda mais poderoso:

* Modelos de PLN mais avançados: Para português, explorar bibliotecas como NLTK ou SpaCy com modelos pré-treinados pode trazer resultados muito mais precisos. 📚

* Treinamento de Modelo: Treinar seu próprio modelo de classificação de sentimento usando conjuntos de dados rotulados (por exemplo, avaliações de filmes, tweets).

* Interface Gráfica: Adicionar uma interface gráfica de usuário (GUI) usando ``Tkinter``, ``PyQt`` ou ``Streamlit`` para uma experiência mais amigável. 🖥️

* API Web: Transformar o analisador em uma API RESTful usando ``Flask`` ou ``FastAPI`` para que ele possa ser consumido por outras aplicações. 🌐

* Análise de Sentimento em Tempo Real: Conectar a uma fonte de dados (ex: tweets, comentários) e analisar o sentimento em tempo real. ⏱️

---

## Conecte-se comigo! 🤝

Ficarei feliz em conectar e trocar ideias! Você pode me encontrar no LinkedIn:

[![Meu LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/salomao-davi)

---













