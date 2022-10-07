import streamlit as st
from PIL import Image
import pandas as pd
from exp import explicacao
from ferramentas import *
from certificate import *
from exp import *
from education import *
from sumary import *

st.set_page_config(page_title='Portfolio Matheus Costa' ,layout="wide",page_icon='💻')

st.markdown('---')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.sidebar.title('Portfólio pessoal')
imagem_perfil = Image.open('arquivos/perfil1.png')
st.sidebar.image(imagem_perfil)
visual = st.sidebar.selectbox('O que você deseja saber?',
                              ('Sobre mim', 'Carreira', 'Habilidades/Experiências'))
if visual == 'Sobre mim':
    st.write(sumary())
elif visual == 'Carreira':
    st.write(edu())  
else:
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
    st.write(explicacao())
    st.markdown('---')
    st.subheader('Ferramentas e experiências ⚒️')
    fr = ferramenta()

st.sidebar.title('Vamos trabalhar juntos?')
st.sidebar.subheader('Contate-me: ')
st.sidebar.write('📧: matheusilva334@gmail.com')
url_git = 'https://github.com/Matheus-S-Costa'
st.sidebar.write("🖥-[GitHub](%s)" % url_git)
url_linkedin = 'https://www.linkedin.com/in/matheus-s-costaa/'
st.sidebar.write('📱-[LinkedIn](%s)' % url_linkedin)
url_curriculo = 'https://drive.google.com/drive/folders/1YjqPgTkX0X51XKj8plJrlPF6yiWzjYyu'
st.sidebar.write("📃-[Meu curículo](%s)" % url_curriculo)

st.markdown(f'''
    <style>
        section[data-testid="stSidebar"] .css-ng1t4o {{width: 16rem;}}
        section[data-testid="stSidebar"] .css-1d391kg {{width: 16rem;}}
    </style>
''',unsafe_allow_html=True)