
import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl

st.set_page_config(
    page_title="Dashboard - Acidentes",
    page_icon="🏙️",
    layout="wide"
)


st.title("🏙️ Acidentes")

df_raw = pd.read_excel('acidentes.xlsx')

diaSemana= df_raw.groupby('dia_semana')

somaAcidentes = diaSemana['id_ocorrencia'].sum()

st.sidebar.header("🔍 Alternar")


modo_visualizacao = st.sidebar.selectbox(
    "Escolha o modo de visualização:",
    ["Tabela", "Gráfico"]
)

if modo_visualizacao == "Tabela":
    st.header(f"📍 Análise TABELA")
    st.dataframe(somaAcidentes)
else:
   st.header(f"📍 Análise GRÁFICO")

st.bar_chart(
    data=somaAcidentes,
      x='dia_semana',
        y='id_ocorrencia',
          x_label='Dia semana',
            y_label='Total acidente',
              color='#ffaa00',
                horizontal=False, 
                sort=True, stack=None,
                  width="stretch", height="content", 
                  use_container_width=None, alt=None)










   
#    fig_1 = px.bar(
#         somaAcidentes,
#         x="id_ocorrencia",
#         y="dia_semana",
#         color="",
#         barmode="group",
#         title=f"Acidentes totais_por dia da semana ",
#         text_auto='.1f'
#     ) 
# fig_1.update_layout(xaxis_tickangle=-25)
# st.plotly_chart(fig_1, use_container_width=True)