import pandas as pd
import streamlit as st
import os # permissão para mover pastas
import requests #para acessar links, e get, put para sites e api's

# --- Configuração da Página ---
# Esta linha configura a janela do navegador (a aba)
st.set_page_config(page_title="Recrutador Reverso", page_icon="🤖") 

# Estas linhas configura o corpo da página
st.title("🤖 Recrutador Reverso IA")
st.sidebar.header("📝 Seus Dados")

# Input do usuário
cv_input = st.sidebar.text_area("Cole o texto do seu currículo aqui")

# Um botão para o usuario clicar e comçar a analise que terá a lógica logo abaixo
botao_processar = st.sidebar.button("Analisar Compatibilidade")

# --- Carregamento dos Dados ---
try:
    #Verifica se o arquivo foi carregado corretamente, caso contrário printa um erro
    tabela_vagas = pd.read_csv("vagas.csv") 
    st.write("Essas são as vagas disponíveis no arquivo:")
    st.dataframe(tabela_vagas)

except FileNotFoundError:
    st.error("ERRO: O arquivo 'vagas.csv' não foi encontrado.")
    st.stop() # Se o arquivo estiver faltando

# --- Processamento ---
# Só entra aqui se o botão foi clicado
if botao_processar:
    
    # Só continua se tiver texto no currículo
    if cv_input:
        st.success("Iniciando análise com agente n8n...")
        
        # URL do  Webhook
        url_n8n = "https://wesley67.app.n8n.cloud/webhook/analisar-vaga"

        # --- O Loop ---
        # iterrows() pega a tabela inteira e devolve linha por linha
        for index, linha in tabela_vagas.iterrows():
            
            #separa os dados para o loop, e variáveis para usar no pacote json que ser enviado ao n8n
            nome_vaga_atual = linha["nome_vaga"] 
            requisitos_atual = linha["descricao"] 

            st.write(f"🔄 Analisando: **{nome_vaga_atual}**...")

            # Pacote para o n8n, no formato dicionário pois a API não entende a coluna pandas
            pacote_dados = {
                "curriculo": cv_input,
                "nome_vaga": nome_vaga_atual, # Certifique-se do nome correto das colunas 
                "descricao": requisitos_atual
            }

            # Envio para o n8n
            try:
                # O requests.post envia o pacote_dados como JSON
                resposta = requests.post(url_n8n, json=pacote_dados)

                if resposta.status_code == 200:
                    dados_recebidos = resposta.json()
                    analise = dados_recebidos["analise"] # Pega o texto que está dentro da chave "analise"
                    # Mostra o resultado específico desta vaga
                    st.info(f"Resultado para {nome_vaga_atual}: {analise}")
                else:
                    st.error(f"Erro no n8n para a vaga {nome_vaga_atual}. Status: {resposta.status_code}")

            except Exception as e:
                st.error(f"Erro de conexão: {e}")
    
    else:
        # Esse else pertence ao 'if cv_input'
        st.warning("⚠️ Cole seu currículo antes de processar.")

