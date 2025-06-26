# Seu código original:
# from textblob import TextBlob # Esta linha está correta
# import TextBlob             # Esta linha está causando o aviso

# Para corrigir, deixe apenas:
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
    print("--- Analisador de Sentimento Básico ---")
    while True:
        frase = input("Digite uma frase (ou 'sair' para encerrar): ")
        if frase.lower() == 'sair':
            break
        
        sentimento = analisar_sentimento(frase)
        print(f"Sentimento da frase: {sentimento}\n")