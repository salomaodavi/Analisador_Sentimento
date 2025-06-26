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