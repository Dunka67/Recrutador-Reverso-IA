# 🤖 Recrutador Reverso com IA e Automação

## 🎯 O Problema
Buscar vagas manualmente em diversos sites consome muito tempo e gera baixa eficiência. Como estudante de ADS vindo da indústria, meu foco é otimizar processos.

## 🚀 A Solução
Desenvolvi um ecossistema autônomo que monitora, filtra e analisa vagas de emprego em tempo real.

### 🛠️ Tecnologias Utilizadas
* **n8n:** Orquestração do fluxo e automação Low-Code.
* **Python:** Tratamento de dados (Pandas) e scripts auxiliares.
* **AI Agents (LLM):** Análise semântica da vaga para dar uma "Nota de Compatibilidade" baseada no meu perfil.
* **Telegram API:** Notificação em tempo real apenas das vagas aprovadas.
* **RSS/Web Scraping:** Coleta de dados de múltiplas fontes (GitHub, TabNews, Portais).

## ⚙️ Como funciona
1.  O sistema monitora feeds de vagas a cada hora.
2.  Filtra palavras-chave irrelevantes (limpeza de dados).
3.  O Agente de IA lê a descrição da vaga e compara com meu currículo.
4.  Se a compatibilidade for alta (>70%), recebo um alerta no Telegram com link e resumo.

---
Desenvolvido por **Wesley Norato**.
www.linkedin.com/in/wesley-s-norato
