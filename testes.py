from sinais import analisar_dominancia
from blocoPorTimestamp import gerar_blocos_por_intervalo
from coletorSwap import coletar_swaps24h
from web3 import Web3
import json
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path('.') / '.env')
url = os.getenv('BLAST_API_CHAVE')
w3 = Web3(Web3.HTTPProvider(url))

#blocos = gerar_blocos_por_intervalo(w3)
#for intervalo, b in blocos.items():
#    print(f'[{intervalo}] Bloco inicial: {b['inicio']} => Bloco final: {b['fim']}')

preco_eth = 2477

sinais = analisar_dominancia(w3, preco_eth)
print('Sinais do Mercado (Dominancia):')
for intervalo, resultado in sinais.items():
    print(f'[{intervalo}] {resultado}')

#print('\nDEBUG: Qnt de swaps por intervalo')
#blocos = gerar_blocos_por_intervalo(w3)
#for intervalo in ['1h', '6h', '24h']:
    #bloco_inicio = blocos[intervalo]['inicio']
    #bloco_fim = blocos[intervalo]['fim']
    #eventos = coletar_swaps24h(w3,'0x3d5D143381916280ff91407FeBEB52f2b60f33Cf', bloco_inicio, bloco_fim)
    #print(f'[{intervalo}] {len(eventos)} eventos coletados')