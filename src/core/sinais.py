from coleta.blocoPorTimestamp import gerar_blocos_por_intervalo
from coleta.coletorSwap import coletar_swaps24h
from core.interpretarSwap import interpretar_swaps

def analisar_dominancia(w3, preco_eth_usd):

    # analisa dominancia de compra/venda em 3 timestamps (1h 6h e 24h) com base nos eventos swaps que envolvem aero/eth
    sinais = {}
    # intervalos podem ter 2 timestamps inclusos com ['1h'] e ['6h']
    intervalos = ['1h', '6h', '24h']
    blocos = gerar_blocos_por_intervalo(w3)
    contrato_pool = '0x3d5D143381916280ff91407FeBEB52f2b60f33Cf'

    for intervalo in intervalos:
        bloco_inicio = blocos[intervalo]['inicio']
        bloco_fim = blocos[intervalo]['fim']
        eventos = coletar_swaps24h(w3, contrato_pool, bloco_inicio, bloco_fim)
        resultado = interpretar_swaps(eventos, preco_eth_usd)

        compra = resultado['compra_usd']
        venda = resultado['venda_usd'] 
        total = compra + venda if (compra + venda) > 0 else 1
        dominancia = (compra / total) * 100

        if dominancia > 55:
            sinal = f'🟢 Dominancia de compra ({dominancia:.1f}%)'
        elif dominancia < 45:
            sinal = f'🔴 Dominancia de venda ({100 - dominancia:.1f}%)'
        else:
            sinal = f'⚪️ Equilibrio ({dominancia:.1f}% compra)'
        
        sinais[intervalo] = sinal
    return sinais