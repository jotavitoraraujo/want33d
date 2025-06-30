import time
import os
from time import sleep
from dotenv import load_dotenv
from web3 import Web3
from pathlib import Path
from coleta.analiseBasica import want33d 
from coleta.coletorSwap import coletar_swaps24h
from core.interpretarSwap import interpretar_swaps
from coleta.blocoPorTimestamp import gerar_blocos_por_intervalo
load_dotenv(dotenv_path=Path('.') / '.env')
url_web3 = os.getenv('BLAST_API_CHAVE')
w3 = Web3(Web3.HTTPProvider(url_web3))

print('=' * 40)
mensagens = [
    "📡 Escaneando blocos da rede...",
    "🔍 Coletando dados on-chain...",
    "⛓️  Aguardando eventos Swap...",
    "🧠 Analisando a força do mercado...",
    "📊 Consolidando leitura técnica..."
]
for mensagem in mensagens:
    print(mensagem)
    time.sleep(1.5)
print('=' * 40)

blocos = gerar_blocos_por_intervalo(w3)
dados, w3 = want33d()
intervalos = ['1h', '6h', '24h']
resultados = {}
print("⏳ Aguarde: Analisando o Mercado em Tempo Real...")
for i, intervalo in enumerate(intervalos, 1):
    inicio = blocos[intervalo]['inicio']
    fim = blocos[intervalo]['fim']
    swaps = coletar_swaps24h(w3, inicio, fim)
    resultados[intervalo] = interpretar_swaps(swaps, dados['precoETH_usd'])
    total = len(swaps)    
    progresso = int((i / len(intervalos)) * 100)
    barra = '█' * (progresso // 4) + '-' * (25 - (progresso // 4))
    print(f'\r🔄 Progresso: [{barra}] {progresso}% ({intervalo})', end='', flush=True)
    
def barra_progresso_global(porcentagem):
    barra_tamanho = 30
    preenchido = int(barra_tamanho * porcentagem / 100)
    barra = '█' * preenchido + '-' * (barra_tamanho - preenchido)
    print(f'\r⏳ Coletando blocos... [{barra}] {porcentagem:.1f}% concluído', end='', flush=True)



def calcular_dominancia(compra, venda):
    total = compra + venda
    if total == 0:
        return 0
    return (compra / total) * 100

if __name__ == '__main__':
    dados, w3 = want33d() # ⬅️ Coleta dados básicos
    blocos = dados['blocos']
    swaps_1h = coletar_swaps24h(w3, blocos['1h']['inicio'], blocos['1h']['fim'], callback_progresso=barra_progresso_global, progresso_offset=0, progresso_total=33.3)
    swaps_6h = coletar_swaps24h(w3, blocos['6h']['inicio'], blocos['6h']['fim'], callback_progresso=barra_progresso_global, progresso_offset=33.3, progresso_total=33.3)
    swaps_24h = coletar_swaps24h(w3, blocos['24h']['inicio'], blocos['24h']['fim'], callback_progresso=barra_progresso_global, progresso_offset=66.6, progresso_total=33.3)
    print()
    resultado_1h = interpretar_swaps(swaps_1h, dados['precoETH_usd'])
    resultado_6h = interpretar_swaps(swaps_6h, dados['precoETH_usd'])
    resultado_24h = interpretar_swaps(swaps_24h, dados['precoETH_usd'])
    dom_1h = calcular_dominancia(resultado_1h['compra_usd'], resultado_1h['venda_usd'])
    dom_6h = calcular_dominancia(resultado_6h['compra_usd'], resultado_6h['venda_usd'])
    dom_24h = calcular_dominancia(resultado_24h['compra_usd'], resultado_24h['venda_usd'])
    

print("=" * 40)
print("📊 want33d — Análise Técnica AERO/ETH")
print("=" * 40)
print(f"💰 Preço AERO: ${dados['preco_usd']}")
print(f'💰 Preço ETH: ${dados['precoETH_usd']:,.2f}')
print(f"📈 Variações - 1h: {dados['variacao']['1h']}% | 6h: {dados['variacao']['6h']}% | 24h: {dados['variacao']['24h']}%")
print(f"📦 Volume Total *Compras|Vendas* - 1h: ${resultado_1h['compra_usd'] + resultado_1h['venda_usd']:,.2f} | 6h: ${resultado_6h['compra_usd'] + resultado_6h['venda_usd']:,.2f} | 24h: ${resultado_24h['compra_usd'] + resultado_24h['venda_usd']:,.2f}")
print(f'🟩 Comprado em USD - 1h: ${resultado_1h["compra_usd"]:,.2f} | 6h: ${resultado_6h["compra_usd"]:,.2f} | 24h: ${resultado_24h["compra_usd"]:,.2f}')
print(f'🟥 Vendido em USD - 1h: ${resultado_1h["venda_usd"]:,.2f} | 6h: ${resultado_6h["venda_usd"]:,.2f} | 24h: ${resultado_24h["venda_usd"]:,.2f}')
print(f"🌊 Liquidez AERO/ETH: ${dados['liquidez_usd']:,.2f}")
print(f"🏦 MarketCap: ${dados['marketCap']:,.2f}")
print(f'🧠 Total de eventos *Swap* detectados - 1h: {len(swaps_1h)}, 6h: {len(swaps_6h)}, 24h: {len(swaps_24h)}')
print(f'🧠 Dominância - 1h: {'🟢' if dom_1h > 50 else '🔴'} {dom_1h:.1f}% | 6h: {'🟢' if dom_6h > 50 else '🔴'} {dom_6h:.1f}% | 24h: {'🟢' if dom_24h > 50 else '🔴'} {dom_24h:.1f}%')
print("=" * 40)
print("📢 Projeto pessoal de João Vitor Araújo — LinkedIn - linkedin.com/in/joaoaraujo-dev | Instagram - @vt2.1")
print("=" * 40)
