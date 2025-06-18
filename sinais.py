import json
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timedelta, timezone
dotenv_path = Path('.') / '.env'
load_dotenv(dotenv_path=dotenv_path)
apiBASEscan_chavePrivada = os.getenv('BASESCAN_API_CHAVE')
agora = datetime.now(timezone.utc)
limite_24h = agora - timedelta(hours=24)



# consulta pela API baseScan p/ obter transações recentes da pool aero/eth
enderecoPool_aeroeth = '0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6'
url_aeroethBASESCAN = (f'https://api.basescan.org/api?module=logs&action=getLogs&fromBlock=31669200&toBlock=31669219&address={enderecoPool_aeroeth}&topic0=0xd78ad95fa46c994b6551d0da85fc275fe6134f29df283f0b1c1d33a7e76c4e94&apikey={apiBASEscan_chavePrivada}')
resposta_poolaeroeth = requests.get(url_aeroethBASESCAN)
dicionarioPoolaeroeth_BASESCAN = resposta_poolaeroeth.json()
transacoes = dicionarioPoolaeroeth_BASESCAN['result']
print(json.dumps(dicionarioPoolaeroeth_BASESCAN, indent=4))
#recentes = [
#    tx for tx in transacoes
#    if datetime.fromtimestamp(int(tx['timeStamp']), tz=timezone.utc) >= limite_24h
#]
#for tx in recentes:
#    if 'swap' not in tx['functionName'].lower():
#       continue
#   print('=' * 40)
#    for chave, valor in tx.items():
#        print(f'{chave}: {valor}')