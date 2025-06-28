from web3 import Web3
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timezone, datetime, timedelta
load_dotenv(dotenv_path=Path('.') / '.env')
url_web3 = os.getenv('BLAST_API_CHAVE')
w3 = Web3(Web3.HTTPProvider(url_web3))


def buscar_bloco_por_timestamp(w3, timestamp_alvo):
    # estrutura de busca binaria para encontrar o bloco mais proximo do timestamp
    bloco_mais_baixo = 1
    bloco_mais_alto = w3.eth.block_number

    while bloco_mais_baixo <= bloco_mais_alto:
        bloco_meio = (bloco_mais_baixo + bloco_mais_alto) // 2
        bloco = w3.eth.get_block(bloco_meio)
        timestamp_bloco = bloco.timestamp

        if timestamp_bloco < timestamp_alvo:
            bloco_mais_baixo =  bloco_meio + 1
        elif timestamp_bloco > timestamp_alvo:
            bloco_mais_alto = bloco_meio - 1
        else:
            return bloco_meio
    return bloco_mais_baixo

def gerar_intervalos_temporais():
    agora = datetime.now(timezone.utc)
    return {
        '24h': int((agora - timedelta(hours=24)).timestamp()),
        '6h': int((agora - timedelta(hours=6)).timestamp()),
        '1h': int((agora - timedelta(hours=1)).timestamp())
    }
    
def gerar_blocos_por_intervalo(w3):
    timestamps = gerar_intervalos_temporais()
    blocos = {}
    bloco_atual = w3.eth.block_number
    bloco_criacao = 4817819
    for intervalo, timestamp in timestamps.items():
        bloco_calculado = buscar_bloco_por_timestamp(w3, timestamp)
        bloco_inicio = max(bloco_calculado, bloco_criacao)
        blocos[intervalo] = {'inicio': bloco_inicio, 'fim': bloco_atual}
    return blocos