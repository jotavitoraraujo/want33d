# === 1. Importações e configuração do ambiente ===

from web3 import Web3
from hexbytes import HexBytes
import time
import pprint
import os
from dotenv import load_dotenv
from pathlib import Path

def coletar_swaps24h():
    inicio_execucao = time.time()
    print('⏳ Aguarde: Analisando o Mercado em Tempo Real...')
    # Carrega variáveis do .env, incluindo a chave da BlastAPI
    dotenv_path = Path('.') / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    # Conecta ao nó RPC da BlastAPI usando Web3
    url_web3 = os.getenv('BLAST_API_CHAVE')
    w3 = Web3(Web3.HTTPProvider(url_web3))
    ######## print(w3.is_connected()) ------ DESATIVADO

    # === 2. Definição do contrato e evento Swap ===
    # Endereço da pool AERO/ETH no padrão checksum da EVM
    contrato_pool_aeroeth = Web3.to_checksum_address('0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6')

    # ABI mínima apenas com o evento Swap necessário
    abi_swap = [
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "internalType": "address", "name": "sender", "type": "address"},
                {"indexed": True, "internalType": "address", "name": "to", "type": "address"},
                {"indexed": False, "internalType": "uint256", "name": "amount0In", "type": "uint256"},
                {"indexed": False, "internalType": "uint256", "name": "amount1In", "type": "uint256"},
                {"indexed": False, "internalType": "uint256", "name": "amount0Out", "type": "uint256"},
                {"indexed": False, "internalType": "uint256", "name": "amount1Out", "type": "uint256"}
            ],
            "name": "Swap",
            "type": "event"
        }
    ]
    # Instancia o contrato para decodificação futura (se necessário)
    contrato_aeroeth = w3.eth.contract(address=contrato_pool_aeroeth, abi=abi_swap)

    # === 3. Intervalo de blocos para análise (últimas 24h) ===
    # Bloco atual e cálculo de ~24 horas atrás (43200 blocos em média na Base)
    bloco_atual = w3.eth.block_number
    blocos_24h = 43200
    bloco_inicio = bloco_atual - blocos_24h
    # print(f'Bloco atual: {bloco_atual} | Bloco ~24h atrás: {bloco_inicio}') ###### DESATIVADO

    # Filtro básico para o evento Swap no intervalo definido
    from_block = bloco_inicio
    to_block = bloco_atual
    topic0_swap = '0xb3e2773606abfd36b5bd91394b3a54d1398336c65005baf7bf7a05efeffaf75b'
    filtros = {
        'fromBlock': from_block,
        'toBlock': to_block,
        'address': contrato_pool_aeroeth,
        'topics': [HexBytes(topic0_swap)]
    }

    # === 4. Coleta dos eventos Swap via paginação ===
    # Inicializa variáveis para armazenar resultados e contagem
    all_logs = []
    total_eventos = 0
    intervalo = 400 # Limite de blocos por requisição
    bloco_atualTemp = bloco_inicio # Ponteiro que será incrementado

    # Loop para coletar os eventos Swap de 400 em 400 blocos
    total_blocos = to_block - from_block
    total_paginas = (total_blocos // intervalo) + 1
    pagina_atual = 1
    while bloco_atualTemp <= bloco_atual:
        bloco_fim = min(bloco_atualTemp + intervalo - 1, bloco_atual)
        filtros_pagina = {
            'fromBlock': bloco_atualTemp,
            'toBlock': bloco_fim,
            'address': contrato_pool_aeroeth,
            'topics': [HexBytes(topic0_swap)]
        }
        try:
            logs_parciais = w3.eth.get_logs(filtros_pagina)
            # calcula progresso
            barra_tamanho = 30
            progresso = pagina_atual / total_paginas
            blocos_preenchidos = int(barra_tamanho * progresso)
            barra = '█' * blocos_preenchidos + '-' * (barra_tamanho - blocos_preenchidos)
            print(f'⏳ Coletando blocos... [{barra}]{pagina_atual}/{total_paginas} páginas          ', end='\r', flush=True)
            pagina_atual += 1
            all_logs.extend(logs_parciais)
            total_eventos += len(logs_parciais)
        except Exception as e:
            print(f' Erro entre os blocos {bloco_atualTemp} e {bloco_fim}: {e}')
            break
        bloco_atualTemp = bloco_fim + 1

    # === 5. Resumo final da coleta ===
    # Salva os logs em uma variável de escopo explícito
    # print('🧾 Resumo da coleta de eventos Swap (últimas 24 horas):') ######## DESATIVADO
    # print(f'✅ Total de eventos Swap encontrados nas ultimas 24h: {total_eventos}') ######## DESATIVADO
    logsSwap24h = all_logs
    tempo_total = time.time() - inicio_execucao
    minutos = int(tempo_total // 60)
    segundos = int(tempo_total % 60)
    print(f'✅ Coleta concluída: {total_eventos} eventos Swap encontrados nas últimas 24h.')
    print(f'⏱️ Tempo total de coleta: {minutos}m {segundos}s.')
    print()
    return logsSwap24h