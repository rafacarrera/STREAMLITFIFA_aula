import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime


if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    
    st.session_state["data"] = df_data

st.markdown("# FIFA23 OFFICIAL DATASET! ⚽️")
st.sidebar.markdown("Desenvolvido por: Rafael Carrera & Asimov Academy")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.google.com/webhp?hl=pt-BR&ictx=2&sa=X&ved=0ahUKEwjT59Go1J2KAxUsFLkGHfP3KFwQPQgI")

st.markdown(
    "Esse é um projeto teste de aprendizado para alunos intermdiários em python, com foco na utilização do Streamlit."
)

