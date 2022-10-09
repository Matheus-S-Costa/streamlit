import streamlit as st
from PIL import Image
from ferramentas import *
from exp import *
from education import *
from sumary import *
from habilities import *
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Portfolio Matheus Costa' ,layout="wide",page_icon='💻')

st.markdown('---')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.sidebar.title('Portfólio pessoal')
imagem_perfil = Image.open('arquivos/perfil1.png')
st.sidebar.image(imagem_perfil)
with st.sidebar:
    selected = option_menu("Menu de opções", ['Home',"Carreira", 'Habilidades/Experiências'], 
    icons=['house','clipboard-data','code'], menu_icon="cast")
if selected == 'Home':
    sumary()
elif selected == 'Carreira':
    edu() 
elif selected == 'Habilidades/Experiências':
    hab()

st.sidebar.markdown('***')
st.sidebar.subheader('Vamos trabalhar juntos?')
st.sidebar.caption('Contate-me: ')
st.sidebar.info('''
📧  : matheusilva334@gmail.com\n
🖥\t-\t[GitHub](https://github.com/Matheus-S-Costa)\n
📱\t-\t[LinkedIn](https://www.linkedin.com/in/matheus-s-costaa/)\n
📃\t-\t[Meu currículo](https://drive.google.com/drive/folders/1YjqPgTkX0X51XKj8plJrlPF6yiWzjYyu)\n
'''
)
st.sidebar.markdown('***')