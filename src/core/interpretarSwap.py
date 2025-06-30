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

        def converte_hex_com_sinal(hex_str):
            valor = int(hex_str, 16)
            if valor >= 2**255:
                valor -= 2**256
            return valor
        amount0 = converte_hex_com_sinal(campos[0])
        amount1 = converte_hex_com_sinal(campos[1])

        # compra de AERO = entrou ETH (1), saiu AERO (0)
        if amount0 > 0 and amount1 < 0:
            total_compraeth += abs(amount1) / (10 ** token1_decimals)

        # venda de AERO = entrou AERO (0), saiu ETH (1)
        elif amount0 < 0 and amount1 > 0:
            total_vendaeth += amount1 / (10 ** token1_decimals)

    return {
        'compra_usd': total_compraeth,
        'venda_usd': total_vendaeth
    }