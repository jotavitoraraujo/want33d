import time
from analiseBasica import want33d 
from coletorSwap import coletar_swaps24h
from interpretarSwap import interpretar_swaps
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
    time.sleep(2)
print('=' * 40)
if __name__ == '__main__':
    dados = want33d() # ⬅️ Coleta dados básicos
    swaps = coletar_swaps24h() # ⬅️ Coleta os eventos
    swaps24h = len(swaps) # Conta os eventos coletados
    resultado_swaps = interpretar_swaps(swaps, dados['precoETH_usd'])
    compra = resultado_swaps['compra_usd']
    venda = resultado_swaps['venda_usd']

print("=" * 40)
print("📊 want33d — Análise Técnica AERO/ETH")
print("=" * 40)
print(f"💰 Preço AERO: ${dados['preco_usd']}")
print(f'💰 Preço ETH: ${dados['precoETH_usd']:,.2f}')
print(f"📈 Variações - 1h: {dados['variacao']['1h']}% | 6h: {dados['variacao']['6h']}% | 24h: {dados['variacao']['24h']}%")
print(f"📦 Volumes   - 1h: ${dados['volume']['1h']:,.2f} | 6h: ${dados['volume']['6h']:,.2f} | 24h: ${dados['volume']['24h']:,.2f}")
print(f"🛒 Transações *Buy|Sell* - 1h: ({dados['transacoes']['c1h']}, {dados['transacoes']['v1h']}) | 6h: ({dados['transacoes']['c6h']}, {dados['transacoes']['v6h']}) | 24h: ({dados['transacoes']['c24h']}, {dados['transacoes']['v24h']})")
print(f"🔁 Total Transações *Buy|Sell* - 1h: {dados['transacoesTotal']['t1h']} | 6h: {dados['transacoesTotal']['t6h']} | 24h: {dados['transacoesTotal']['t24h']}")
print(f'🟩 Volume Real comprado em USD (últimas 24h): ${resultado_swaps['compra_usd']:,.2f}')
print(f'🟥 Volume Real vendido em USD (últimas 24h): ${resultado_swaps['venda_usd']:,.2f}')
print(f"🌊 Liquidez AERO/ETH: ${dados['liquidez_usd']:,.2f}")
print(f"🏦 MarketCap: ${dados['marketCap']:,.2f}")
print(f'🧠 Total de eventos *Swap* detectados nas últimas 24 horas: {swaps24h}')
print("=" * 40)
print("⚙️  Isso aqui não foi gerado por IA, foi suado mesmo 😅")
print("📢 Projeto pessoal do João Araújo — me segue lá no LinkedIn, vai que eu viro dev famoso: linkedin.com/in/joaoaraujo-dev")
print("=" * 40)
