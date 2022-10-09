import pandas as pd
import streamlit as st
from ferramentas import *
from exp import *

def hab():
    st.subheader('Habilidades/Projetos💻')
    def load_data():
        return pd.DataFrame(
            {
                'Linguagens/software': ['Python', 'html e css', 'javascript', 'matlab'],
                'Maiores utilidades': ['versatil, data science', 'Complemento desenvolvimento web', 'Desenvolvimento web', 'Calculos e plot de graficos']
            }
        )
    df = load_data()
    st.dataframe(df)
    st.write('''
         Cada linguagem tem seus pontos fortes e fracos, busco explorar os pontos fortes de cada uma, sempre pesquisando sobre e me atentando às novidades.
        ''')
    explicacao()
    st.markdown('---')
    st.subheader('Ferramentas e experiências ⚒️')
    ferramenta()