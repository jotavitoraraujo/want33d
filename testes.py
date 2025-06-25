from sinais import analisar_dominancia
from web3 import Web3
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path('.') / '.env')
url = os.getenv('BLAST_API_CHAVE')
w3 = Web3(Web3.HTTPProvider(url))

preco_eth = 2430

sinais = analisar_dominancia(w3, preco_eth)
print('Sinais do Mercado (Dominancia):')
for intervalo, resultado in sinais.items():
    print(f'[{intervalo}] {resultado}')