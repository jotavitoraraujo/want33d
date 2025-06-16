# importação de modulos e bibliotecas internas do python
import os
import json

# importação de modulos e bibliotecas externas do python
import requests
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timedelta, timezone

# ajuste de caminho .env
dotenv_path = Path('.') / '.env'
load_dotenv(dotenv_path=dotenv_path)

# função personalizada
def want33d():

    # ajuste de data/hora
    agora = datetime.now(timezone.utc)
    limite_24h = agora - timedelta(hours=24)

    # variavel que armazena minha chave api privada
    apiBASEscan_chavePrivada = os.getenv('BASESCAN_API_CHAVE')

    # dicionário json pool aero/eth | via api dexScrenner
    url_aeroeth = 'https://api.dexscreener.com/latest/dex/pairs/base/0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6'
    resposta_aeroeth = requests.get(url_aeroeth)
    dicionario_aeroeth = resposta_aeroeth.json()

    # captura de preço
    preco_aeroeth = dicionario_aeroeth['pair']['priceUsd']
    print('-' * 40)
    print(f'Preço AERO: ${preco_aeroeth}')

    # captura de variacao de preço | 3 timestamps | 1h - 6h - 24h
    variacao_1h = dicionario_aeroeth['pair']['priceChange']['h1']
    variacao_6h = dicionario_aeroeth['pair']['priceChange']['h6']
    variacao_24h = dicionario_aeroeth['pair']['priceChange']['h24']
    print(f'Variações - 1h: {variacao_1h}% | 6h: {variacao_6h}% | 24h: {variacao_24h}%')

    # captura de volumes | 3 timestamps | 1h - 6h - 24h
    volume_1h = dicionario_aeroeth['pair']['volume']['h1']
    volume_6h = dicionario_aeroeth['pair']['volume']['h6']
    volume_24h = dicionario_aeroeth['pair']['volume']['h24']
    print(f'Volumes - 1h: ${volume_1h:,.2f} | 6h: ${volume_6h:,.2f} | 24h: ${volume_24h:,.2f}')

    # captura de transações | 3 timestamps | 1h - 6h - 24h
    compras_1h = dicionario_aeroeth['pair']['txns']['h1']['buys']
    compras_6h = dicionario_aeroeth['pair']['txns']['h6']['buys']
    compras_24h = dicionario_aeroeth['pair']['txns']['h24']['buys']
    vendas_1h = dicionario_aeroeth['pair']['txns']['h1']['sells']
    vendas_6h = dicionario_aeroeth['pair']['txns']['h6']['sells']
    vendas_24h = dicionario_aeroeth['pair']['txns']['h24']['sells']

    # transações totais | 3 timestamps | 1h - 6h - 24h
    total_1h = compras_1h + vendas_1h
    total_6h = compras_6h + vendas_6h
    total_24h = compras_24h + vendas_24h
    print(f'Transações *Buy|Sell* - 1h: {compras_1h, vendas_1h} | 6h: {compras_6h, vendas_6h} | 24h: {compras_24h, vendas_24h}')
    print(f'Total Transações *Buy|Sell* - 1h: {total_1h} | 6h: {total_6h} | 24h: {total_24h}')

    # liquidez na pool 
    liquidez = dicionario_aeroeth['pair']['liquidity']['usd']
    print(f'Liquidez AERO/ETH: ${liquidez:,.2f}')

    # captura de marketcap (na lista 0)
    marketcap = dicionario_aeroeth['pairs'][0]['marketCap']
    print(f'MarketCap: ${marketcap:,.2f}')
    print('-' * 40)

    # consulta pela API baseScan p/ obter transações recentes da pool aero/eth
    enderecoPool_aeroeth = '0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6'
    url_aeroethBASESCAN = (f'https://api.basescan.org/api?module=account&action=txlist&address={enderecoPool_aeroeth}&startblock=0&endblock=99999999&sort=desc&apikey={apiBASEscan_chavePrivada}')
    resposta_poolaeroeth = requests.get(url_aeroethBASESCAN)
    dicionarioPoolaeroeth_BASESCAN = resposta_poolaeroeth.json()
    transacoes = dicionarioPoolaeroeth_BASESCAN['result']
    recentes = [
        tx for tx in transacoes
        if datetime.fromtimestamp(int(tx['timeStamp']), tz=timezone.utc) >= limite_24h
    ]
if __name__ == '__main__':
    want33d()