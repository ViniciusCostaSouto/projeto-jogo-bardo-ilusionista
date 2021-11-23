def forcar_escolha(pergunta, qtde_respostas): # Declara função de forçar escolha, pede pergunta e a quantidade de respostas possíveis
    if qtde_respostas == 1:
        while pergunta not in ("1"):
	    pergunta
        resposta = int(pergunta)
        return resposta
    if qtde_respostas == 2:
        while pergunta not in ("1", "2"):
	    pergunta
        resposta = int(pergunta)
        return resposta
    if qtde_respostas == 3:
        while pergunta not in ("1", "2", "3"):
	    pergunta
        resposta = int(pergunta)
        return resposta
    if qtde_respostas == 4:
        while pergunta not in ("1", "2", "3", "4"):
	    pergunta
        resposta = int(pergunta)
        return resposta
    if qtde_respostas == 5:
        while pergunta not in ("1", "2", "3", "4", "5"):
	    pergunta
        resposta = int(pergunta)
        return resposta