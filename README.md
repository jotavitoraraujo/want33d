# 🧠 want33d — Agente Autônomo de Monitoramento Cripto

Este projeto tem como objetivo criar um agente autônomo em Python capaz de monitorar o preço e os volumes de negociação do token **AERO** (Aerodrome Finance), utilizando a API pública da **DefiLlama**.

## 🟩 Funcionalidades

- ✅ Coleta em tempo real do preço do token AERO  
- ✅ Análise simples de suporte/resistência baseada em thresholds definidos manualmente  
- 📊 Coleta e agregação de volumes de negociação de 24h, 7d e 30d  
- 🧠 Organização dos dados em dicionários Python com semântica clara  
- 📉 Comparação entre o TVL atual e o de 30 dias atrás com busca automática da data mais próxima e retorno da análise no terminal

## 🛠️ Tecnologias

- [Python 3.13+](https://www.python.org)
- [VS Code](https://code.visualstudio.com/)
- Bibliotecas padrão:
  - `datetime`, `timezone`, `timedelta` — manipulação de datas e horários
- Biblioteca externa:
  - `requests` — acesso a APIs REST (instalável via `pip install requests`)

## 📦 Instalação e Execução

```bash
# Clone este repositório
git clone https://github.com/want33d/want33d.git
cd want33d

# Execute o script principal
python main.py
```

## 📁 Estrutura do Projeto

```
want33d/
want33d/
├── preco.py   # Responsável pela coleta de preço, volumes e análise de suporte/resistência
├── tvl.py     # Responsável pela análise de variação do TVL entre a data atual e 30 dias atrás
├── README.md  # Instruções e documentação do projeto
```

## 👨‍💻 Autor

Desenvolvido por **João Vitor Araújo** — Estudante de Análise e Desenvolvimento de Sistemas.
Focado em aprendizado raiz, disciplina prática e construção de projetos reais desde o primeiro código.

[🔗 LinkedIn](www.linkedin.com/in/joaoaraujo015/)
[🔗 Instagram](https://www.instagram.com/vt2.1/)

## 📅 Histórico de Atualizações

- [09/06/2025] Adicionado recurso de comparação entre o TVL atual e o de 30 dias atrás, com análise automática da variação (aumento, queda ou estabilidade), exibido diretamente no terminal.
- [12/06/2025] Refatorado o projeto com separação de responsabilidades em arquivos distintos (`preco.py` e `tvl.py`). A função de análise de TVL agora retorna a variação (aumento/queda/estável) com base na data mais próxima possível de 30 dias atrás.

## ⚖️ Licença

Este projeto é de uso pessoal e educacional. Sinta-se livre para estudar, adaptar e evoluir a ideia.