import time
import sys

def temporizador(passo_atual, total_passos, inicio_execucao, prefixo="⏳ Progresso"):
    """
    Exibe uma barra de progresso com tempo decorrido no terminal.

    passo_atual (int): Iteração atual (ex: página atual, bloco atual)
    total_passos (int): Total de iterações previstas
    inicio_execucao (float): Timestamp inicial (time.time())
    prefixo (str): Texto inicial da linha
    """
    progresso = passo_atual / total_passos
    barra_tamanho = 30 
    barra = '█' * int(barra_tamanho * progresso) + '-' * (barra_tamanho - int(barra_tamanho * progresso))
    tempo_decorrido = time.time() - inicio_execucao
    tempo_formatado = time.strftime('%H:%M:%S', time.gmtime(tempo_decorrido))
    linha = f'\r{prefixo} |{barra}| {passo_atual}/{total_passos} • ⏱️ {tempo_formatado}'
    sys.stdout.write(linha)
    sys.stdout.flush()
    if passo_atual == total_passos:
        sys.stdout.write('\n')

    