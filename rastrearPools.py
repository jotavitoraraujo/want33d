from web3 import Web3
import os
from dotenv import load_dotenv
from pathlib import Path

# === Conectando ao nó da BlastAPI ===
# Carrega a chave API do arquivo .env
dotenv_path = Path('.') / '.env'
load_dotenv(dotenv_path=dotenv_path)

# Puxa a chave do ambiente
url2_web3 = os.getenv('BLAST_API_CHAVE')

# Cria a instancia web3 com o endpoint http
w3 = Web3(Web3.HTTPProvider(url2_web3))

# Verifica a conexão com a rede
print('Conectado a rede Base:', w3.is_connected())

# === Definição do contrato do token AERO ===
# endereço do contrato do token AERO (no formato checksum)
endereco_aero = Web3.to_checksum_address('0x940181a94a35A4569E4529A3CDfB74e38FD98631')
#abi minima para interagir com os eventos do token aero
abi_aero = []
# cria instancia do contrato
contrato_aero = w3.eth.contract(address=endereco_aero, abi=abi_aero)
# obtem o numero do bloco mais recente
bloco_atual = w3.eth.block_number
# pega o timestamp do bloco atual
bloco_info = w3.eth.get_block(bloco_atual)
timestamp_atual = bloco_info['timestamp']
timestamp_24hatras = timestamp_atual - 86400 
# loop binario para achar o bloco mais proximo das ultimas 24h
bloco_inicio = 0
bloco_fim = bloco_atual
bloco_24hatras = None
while bloco_inicio <= bloco_fim:
    bloco_meio = (bloco_inicio + bloco_fim) // 2
    bloco_info = w3.eth.get_block(bloco_meio)
    timestamp_bloco = bloco_info['timestamp']
    if timestamp_bloco < timestamp_24hatras:
        bloco_inicio = bloco_meio + 1
    elif timestamp_bloco > timestamp_24hatras
        bloco_fim = bloco_meio + 1
    else:
        bloco_24hatras = bloco_meio
        break
# se nao encontrar o exato, pego o mais proximo
if bloco_24hatras is None
    bloco_24hatras = bloco_fim
# indenticador de eventos swap
topic0_swap = '0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67'