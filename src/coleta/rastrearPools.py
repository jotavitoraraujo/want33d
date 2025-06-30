from web3 import Web3
import os
import time
from dotenv import load_dotenv
from pathlib import Path
from coleta.blocoPorTimestamp import gerar_blocos_por_intervalo
from hexbytes import HexBytes
from core.utils import temporizador

dotenv_path = Path('.') / '.env'
load_dotenv(dotenv_path=dotenv_path)
url2_web3 = os.getenv('BLAST_API_CHAVE')
w3 = Web3(Web3.HTTPProvider(url2_web3))
# print('Conectado a rede Base:', w3.is_connected())

# === Definição do contrato do token AERO ===
# endereço do contrato do token AERO (no formato checksum)
endereco_aero = Web3.to_checksum_address('0x940181a94a35A4569E4529A3CDfB74e38FD98631')
# indenticador de eventos swap
topic0_swap = HexBytes('0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67')
# função de buscar todas as pools q contenham AERO
def buscar_pools_com_aero():
    print('Buscando pools que interagiram com AERO nas ultimas 1h...')
    blocos_dict, _ = gerar_blocos_por_intervalo(w3)
    bloco_inicio = blocos_dict['6h'][0]
    bloco_atual = blocos_dict['6h'][1]    
    intervalo = 400
    bloco_temp = bloco_inicio
    contratos_envolvidos = set()
    total_paginas = ((bloco_atual - bloco_inicio) // intervalo) + 1
    pagina = 1
    inicio_execucao = time.time()
    

    while bloco_temp <= bloco_atual:
        bloco_fim = min(bloco_temp + intervalo - 1, bloco_atual)        
        filtros = {
            'fromBlock': bloco_temp,
            'toBlock': bloco_fim,
            'topics': [HexBytes(topic0_swap)]
        }        
        try:
            logs = w3.eth.get_logs(filtros)
            for log in logs:
                contratos_envolvidos.add(log['address'])
        except Exception as e:
            print(f'Erro na coleta entre blocos {bloco_temp} e {bloco_fim}: {e}')
            break        
        temporizador(
            passo_atual = bloco_temp - bloco_inicio,
            total_passos = max(bloco_atual - bloco_inicio, 1),
            inicio_execucao = inicio_execucao,
            prefixo ='🧠 Rastreando Pools'
        )
        pagina += 1
        bloco_temp = bloco_fim + 1
    print(f'\nTotal de pools unicas envolvendo AERO: {len(contratos_envolvidos)}')
    return contratos_envolvidos
    