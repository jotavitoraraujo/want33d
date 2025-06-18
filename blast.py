from web3 import Web3
from hexbytes import HexBytes
import pprint
url_web3 = 'https://base-mainnet.blastapi.io/db346726-b849-4a23-a11b-71b798c290d1'
w3 = Web3(Web3.HTTPProvider(url_web3))
print(w3.is_connected())

contrato_pool_aeroeth = Web3.to_checksum_address('0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6')
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
contrato_aeroeth = w3.eth.contract(address=contrato_pool_aeroeth, abi=abi_swap)
bloco_atual = w3.eth.block_number
blocos_24h = 43200
bloco_inicio = bloco_atual - blocos_24h
print(f'Bloco atual: {bloco_atual} | Bloco ~24h atrás: {bloco_inicio}')
from_block = bloco_inicio
to_block = bloco_atual
topic0_swap = '0xb3e2773606abfd36b5bd91394b3a54d1398336c65005baf7bf7a05efeffaf75b'
filtros = {
    'fromBlock': from_block,
    'toBlock': to_block,
    'address': contrato_pool_aeroeth,
    'topics': [HexBytes(topic0_swap)]
}
pprint.pprint(filtros)
# logs = w3.eth.get_logs(filtros)
all_logs = []
intervalo = 1000
bloco_atualTemp = bloco_inicio
while bloco_atualTemp < bloco_atual:
    if 31668776 <= bloco_atualTemp <= 31669776: 
        ajuste_intervalo = 500
    elif 31670012 <= bloco_atualTemp <= 31671012:
        ajuste_intervalo = 250
    else: 
        ajuste_intervalo = intervalo
    bloco_fim = min(bloco_atualTemp + ajuste_intervalo, bloco_atual)
    filtros_pagina = {
        'fromBlock': bloco_atualTemp,
        'toBlock': bloco_fim,
        'address': contrato_pool_aeroeth,
        'topics': [HexBytes(topic0_swap)]
    }
    try:
        logs_parciais = w3.eth.get_logs(filtros_pagina)
        all_logs.extend(logs_parciais)
        print(f'Blocos {bloco_atualTemp} a {bloco_fim} => {len(logs_parciais)} eventos (swaps) encontrados')
    except Exception as e:
        print(f' Erro entre os blocos {bloco_atualTemp} e {bloco_fim}')
        print(e)
        break
    bloco_atualTemp = bloco_fim + 1
logs = all_logs
print(Web3.keccak(text='Swap(address,address,uint256,uint256,uint256,uint256)').hex())
print(f'Eventos Swap encontrados nas ultimas 24h: {len(logs)}')
if logs:
    print(logs[0]['topics'][0])