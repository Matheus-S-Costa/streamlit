    
from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd

def sumary():
    col1, col2 = st.columns(2)
    col1.title('Matheus Costa')
    col2.write('- Nascimento: 04/05/2002')
    col2.write('- Formação: Técnico eletrônica')
    col2.write('- Estudante: Engenharia de Computação (6º período)')
    st.markdown('---')
    st.header('Sumario 📝')
    st.write('Técnico em eletrônica com mais de 2 anos de experiência profissional em macOS e iOS, atualmente procurando resolver problemas complexos de negócios usando IA e programação; Estudando desenvolvimento de soluções orientadas a dados para automatizar a digitalização de documentos para reduzir os esforços manuais; Amor para aprender coisas novas. ')
    st.markdown('---')
    st.write('- A framework de SCRUM é a que utilizo para gerenciar a maioria dos meus projetos, para que com as sprints, haja um melhor acompanhamento do desenvolvimento. ')
    imagem_scrum = Image.open('arquivos/scrum2.png')
    st.image(imagem_scrum)
