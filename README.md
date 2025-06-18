# 🧠 want33d — Agente Autônomo de Monitoramento Cripto

Este projeto tem como objetivo criar um agente autônomo em Python, chamado **want33d**, capaz de monitorar em tempo real o comportamento do token **AERO** (Aerodrome Finance) na rede **Base**, utilizando APIs públicas para análise de preço, volume, liquidez e força compradora/vendedora.

---

## ⚙️ Funcionalidades Atuais

* ✅ Coleta de preço em tempo real via API da **DexScreener**
* ✅ Monitoramento de variação percentual de preço (1h, 6h, 24h)
* ✅ Captura de volume negociado em diferentes janelas de tempo
* ✅ Leitura da liquidez atual da pool AERO/ETH
* ✅ Exibição do **marketcap** atual
* ✅ Consulta direta ao RPC da rede **Base** (via BlastAPI) para análise on-chain de eventos Swap na pool AERO/ETH
* ✅ Filtro para transações reais com movimentação de valor (> 0 ETH)
* 🚧 Identificação de tipo de chamada (`methodId`) com futura classificação como compra/venda
* ✅ Estrutura modular com `main.py` como ponto de entrada

---

## 🧱 Tecnologias Utilizadas

* [Python 3.13+](https://www.python.org/)
* [VS Code](https://code.visualstudio.com/)

### Bibliotecas padrão:

* `datetime`, `os`, `json`, `pathlib`

### Bibliotecas externas utilizadas no projeto:

* `web3==7.12.0`
* `hexbytes==1.3.1`
* `requests==2.32.4`
* `python-dotenv==1.1.0`

Essas dependências estão listadas no arquivo `requirements.txt`, gerado com base no uso real do projeto.

---

## 🚀 Como Executar

1. Clone o projeto:

```bash
git clone https://github.com/want33d/want33d.git
cd want33d
```

2. Execute o projeto:

```bash
python main.py
```

Atualmente, todas as análises estão concentradas no módulo `analiseBasica.py`, responsável por capturar dados da pool AERO/ETH diretamente da blockchain da Base e apresentar métricas como preço, volume, liquidez e número de transações.

---

## 🧩 Estrutura Atual do Projeto

```
want33d/
├── analiseBasica.py     # Módulo com toda a lógica de análise da pool AERO/ETH
├── blast.py             # Consulta direta ao RPC da rede Base com paginação de blocos
├── sinais.py            # Em desenvolvimento — motor de sinais técnicos
├── main.py              # Ponto de entrada do projeto
├── requirements.txt     # Dependências reais do projeto
├── .env                 # Variáveis de ambiente sensíveis (não deve ser versionado)
├── .gitignore           # Arquivos ignorados pelo Git
├── README.md            # Este documento
├── LICENSE
```

---

## 👨‍💻 Autor

Desenvolvido por **João Vitor Araújo** — Estudante de Análise e Desenvolvimento de Sistemas.
Foco em aprendizado raiz, disciplina e domínio técnico na prática.

🔗 [LinkedIn](https://www.linkedin.com/in/joaoaraujo-dev/)
🔗 [Instagram](https://www.instagram.com/vt2.1/)

---

## 📅 Histórico de Atualizações

* **09/06/2025** — Análise de TVL entre data atual e 30 dias atrás via DefiLlama
* **12/06/2025** — Refatoração com separação em `preco.py` e `tvl.py`
* **15/06/2025** — Reestruturação total: código principal agora em `want33d.py`, execução via `main.py`, com foco em análise técnica e comportamento real da pool via BaseScan
* **18/06/2025** — Coleta de eventos Swap via RPC da Blast com paginação, limite de blocos e estratégia baseada em timestamps psicológicos

---

## 📌 Observações Finais

> O projeto está evoluindo rumo à construção de um agente que possa detectar **padrões de dominância de compra ou venda** com base em dados brutos on-chain. O foco é detectar oportunidades para entradas estratégicas, com base em ciclos de curto prazo, e defender-se de manipulações de bots.
