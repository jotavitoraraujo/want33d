
# 🧠 want33d — Agente Autônomo de Monitoramento Cripto

Este projeto tem como objetivo criar um agente autônomo em Python, chamado **want33d**, capaz de monitorar em tempo real o comportamento do token **AERO** (Aerodrome Finance) na rede **Base**, utilizando APIs públicas e dados on-chain para análise de preço, liquidez e dominância de mercado, com foco especial em **formadores de mercado**.

---

## ⚙️ Funcionalidades Atuais

- ✅ Coleta de preço em tempo real via API da **DexScreener**
- ✅ Monitoramento de variação percentual de preço (1h, 6h, 24h)
- ✅ Leitura da liquidez atual e marketcap da pool AERO/ETH
- ✅ Geração precisa de blocos com base em **timestamps psicológicos** (1h, 6h, 24h)
- ✅ Consulta direta ao RPC da rede **Base** (via BlastAPI) para análise on-chain de eventos **Swap**
- ✅ Páginação eficiente com barra de progresso única e interativa
- ✅ Filtro para **transações reais com movimentação de valor** (> 0 ETH)
- ✅ Interpretação dos eventos Swap (entrada/saída de ETH) com cálculo do volume comprado/vendido em USD
- ✅ Motor de sinais com cálculo da **dominância de mercado** (🟢 Compra | 🔴 Venda | ⚪️ Equilíbrio)
- ✅ Diagnóstico visual da força de mercado com base no volume comprado/vendido por intervalo
- ✅ Interface no terminal com saída humanizada e informativa
- ✅ Estrutura modular com ponto de entrada em `main.py`
- 🛠️ Em breve: Rastreamento do token AERO em múltiplas pools da Base, independente do contrato

---

## 🧱 Tecnologias Utilizadas

- **Python 3.13+**
- **VS Code**

### Bibliotecas padrão:

- `datetime`, `os`, `json`, `pathlib`, `time`

### Bibliotecas externas utilizadas no projeto:

- `web3==7.12.0`
- `hexbytes==1.3.1`
- `requests==2.32.4`
- `python-dotenv==1.1.0`

Essas dependências estão listadas no arquivo `requirements.txt`, gerado com base no uso real do projeto.

---

## 🚀 Como Executar

1. Clone o projeto:

```bash
git clone https://github.com/want33d/want33d.git
cd want33d
```

2. Configure o arquivo `.env` com suas chaves:

```env
BLAST_API_CHAVE=<sua_rpc_url>
BASESCAN_API_CHAVE=<sua_api_key_basescan>
```

3. Execute o projeto:

```bash
python main.py
```

O terminal exibirá a leitura técnica da pool AERO/ETH baseada em blocos recentes, com destaque para volume comprado, volume vendido, dominância e equilíbrio de forças no mercado.

---

## 🧩 Estrutura Atual do Projeto

```
want33d/
├── dicionario_apis/                   # Dicionários com as signatures dos eventos e padrões de APIs
│   ├── dictBASESCAN.py                    # Topics e ABI do contrato da pool AERO/ETH na BaseScan
│   └── dictDEXScreener.py                 # Identificadores da DexScreener para coleta de preço
│
├── src/
│   ├── coleta/                        # Módulos responsáveis por buscar os dados brutos (preço, swaps, blocos)
│   │   ├── analiseBasica.py              # Consulta dados da DexScreener
│   │   ├── blocoPorTimestamp.py         # Converte timestamps para blocos na Base
│   │   ├── coletorSwap.py               # Coleta eventos Swap da AERO/ETH via RPC
│   │   └── rastrearPools.py            # (WIP) Rastreia o token AERO em múltiplas pools
│   │
│   ├── core/                          # Camada lógica do projeto (interpretação e sinais)
│   │   ├── interpretarSwap.py           # Determina direção (compra/venda) e volume real de swaps
│   │   ├── sinais.py                    # Calcula dominância com base nos volumes
│   │   └── utils.py                     # Funções auxiliares (formatação, temporizador etc.)
│   │
│   └── estudos/                       # Arquivos de estudo e execução local
│       └── testes.py                    # Scripts para testes manuais
│       
├── main.py                            # Ponto de entrada do projeto com output formatado no terminal
├── requirements.txt                   # Dependências externas utilizadas no projeto
├── .env                               # Variáveis sensíveis (não deve ser versionado)
├── .gitignore                         # Arquivos/pastas ignorados pelo Git
├── README.md                          # Este documento
└── LICENSE                            # Licença de uso do projeto
```

---

## 👨‍💻 Autor

Desenvolvido por **João Vitor Araújo** — Estudante de Análise e Desenvolvimento de Sistemas.  
Foco em aprendizado raiz, disciplina e **formação de mercado** com dados reais e blockchain.

- [LinkedIn](https://www.linkedin.com/in/joaoaraujo-dev/)
- [Instagram](https://www.instagram.com/vt2.1/)

---

## 📅 Histórico de Atualizações

- **09/06/2025** — Análise de TVL entre data atual e 30 dias atrás via DefiLlama
- **12/06/2025** — Refatoração com separação em `preco.py` e `tvl.py`
- **15/06/2025** — Reestruturação total: Execução via `main.py`, com foco em análise técnica e comportamento real da pool via BaseScan
- **18/06/2025** — Coleta de eventos Swap via RPC da Blast com paginação, limite de blocos e estratégia baseada em timestamps psicológicos (em planejamento)
- **19/06/2025** — Interpretação dos eventos Swap finalizada com cálculo de volumes reais comprados/vendidos em USD. Adição de temporizador animado para feedback contínuo durante a coleta. Interface de leitura no terminal totalmente reformulada para simular uma leitura de mercado profissional.
- **21/06/2025** — Implementação da lógica de timestamp → bloco para múltiplas janelas de tempo (1h, 6h, 24h) com busca binária. Início da nova fase: rastrear todos os eventos Swap com o token AERO em toda a blockchain Base.
- **24/06/2025** — Finalização do motor de sinais com leitura real de dominância de mercado por intervalo. Estrutura modular 100% funcional. Suspeita de manipulação identificada na pool AERO/ETH usada como base. Investigação em andamento.
- **28/06/2025** — Conclusão da primeira versão estável do want33d como agente de leitura técnica para formadores de mercado.

---

## 📌 Observações Finais

O **want33d** foi desenvolvido com foco em **formadores de mercado**, priorizando dados on-chain confiáveis para leitura de comportamento de pool e tomada de decisão. Com análises em múltiplos intervalos e leitura da dominância real de fluxo, o projeto oferece ferramentas para identificar desequilíbrios, sinais de manipulação ou oportunidades de entrada baseadas em movimentações reais na blockchain.

A próxima fase do projeto foca no rastreamento de **todas as pools** onde o token AERO circula, elevando o nível da análise e antecipando movimentos relevantes do mercado.
