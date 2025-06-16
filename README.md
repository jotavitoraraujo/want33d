
# 🧠 want33d — Agente Autônomo de Monitoramento Cripto

Este projeto tem como objetivo criar um agente autônomo em Python, chamado **want33d**, capaz de monitorar em tempo real o comportamento do token **AERO** (Aerodrome Finance) na rede **Base**, utilizando APIs públicas para análise de preço, volume, liquidez e força compradora/vendedora.

---

## ⚙️ Funcionalidades Atuais

- ✅ Coleta de preço em tempo real via API da **DexScreener**
- ✅ Monitoramento de variação percentual de preço (1h, 6h, 24h)
- ✅ Captura de volume negociado em diferentes janelas de tempo
- ✅ Leitura da liquidez atual da pool AERO/ETH
- ✅ Exibição do **marketcap** atual
- ✅ Consulta à **BaseScan** para análise de transações recentes da pool (últimas 24h)
- ✅ Filtro para transações reais com movimentação de valor (> 0 ETH)
- 🚧 Identificação de tipo de chamada (`methodId`) com futura classificação como compra/venda
- ✅ Estrutura modular com `main.py` como ponto de entrada

---

## 🧱 Tecnologias Utilizadas

- [Python 3.13+](https://www.python.org/)
- [VS Code](https://code.visualstudio.com/)
- Bibliotecas padrão:
  - `datetime`, `os`, `json`, `pathlib`
- Bibliotecas externas:
  - `requests` — acesso a APIs REST
  - `python-dotenv` — leitura de variáveis de ambiente

---

## 🚀 Como Executar

1. Clone o projeto:
```bash
git clone https://github.com/want33d/want33d.git
cd want33d
```

2. Crie um arquivo `.env` e adicione sua chave da BaseScan:
```
BASESCAN_API_CHAVE=suachaveaqui
```

3. Execute o projeto:
```bash
python main.py
```

---

## 🧩 Estrutura Atual do Projeto

```
want33d/
├── want33d.py      # Código principal encapsulado na função want33d()
├── main.py         # Ponto de entrada que chama a função principal
├── .env            # Armazena sua chave privada da API BaseScan
├── README.md       # Este documento
├── LICENSE
```

---

## 👨‍💻 Autor

Desenvolvido por **João Vitor Araújo** — Estudante de Análise e Desenvolvimento de Sistemas.  
Foco em aprendizado raiz, disciplina e domínio técnico na prática.

🔗 [LinkedIn](https://www.linkedin.com/in/joaoaraujo015/)  
🔗 [Instagram](https://www.instagram.com/vt2.1/)

---

## 📅 Histórico de Atualizações

- **09/06/2025** — Análise de TVL entre data atual e 30 dias atrás via DefiLlama
- **12/06/2025** — Refatoração com separação em `preco.py` e `tvl.py`
- **15/06/2025** — Reestruturação total: código principal agora em `want33d.py`, execução via `main.py`, com foco em análise técnica e comportamento real da pool via BaseScan

---

## 📌 Observações Finais

> O projeto está evoluindo rumo à construção de um agente que possa detectar **padrões de dominância de compra ou venda** com base em dados brutos on-chain. O foco é detectar oportunidades para entradas estratégicas, com base em ciclos de curto prazo, e defender-se de manipulações de bots.
