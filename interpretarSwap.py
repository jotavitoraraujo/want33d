# === 1. Função principal de interpretação ===

def interpretar_swaps(logs_swap, token0_decimals=18, token1_decimals=18):
    
    # Interpreta os eventos Swap e calcula os volumes totais de compra e venda.
    # Assume: token0 = AERO, token1 = ETH (padrão da Aerodrome na Base).

    total_compraeth = 0
    total_vendaeth = 0

    for log in logs_swap:
        data_hex = log['data'].hex()
        # quebra o campo data em blocos de 64 hexchars (uint256)
        campos = [data_hex[i:i+64] for i in range(0, len(data_hex), 64)]

        amount0In  = int(campos[0], 16)
        amount1In  = int(campos[1], 16)
        amount0Out = int(campos[2], 16)
        amount1Out = int(campos[3], 16)

        # compra de AERO = entrou ETH (1In), saiu AERO (0Out)
        if amount1In > 0 and amount0Out > 0:
            total_compraeth += amount1In / (10 ** token1_decimals)

        # venda de AERO = entrou AERO (0In), saiu ETH (1Out)
        elif amount0In > 0 and amount1Out > 0:
            total_vendaeth += amount1Out / (10 ** token1_decimals)

    return {
        'compra_usd': total_compraeth,
        'venda_usd': total_vendaeth
    }