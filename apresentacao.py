import streamlit as st
from PIL import Image
import pandas as pd
from exp import explicacao
from ferramentas import *
from certificate import *
from exp import *

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
elif visual == 'Carreira':
    st.header('Linha do tempo carreira🥇')    
    image = Image.open('arquivos/timeline.png')
    st.image(image)
    st.markdown('---')
    st.header('Educação 📖')
    if st.button('Ensino Médio'):
        st.write('Em 2017 iniciei meus estudos no Colégio Técnico da UFMG, com o ensino médio e técnico integrado, tive meu primeiro contato com programação, tive contato com a linguagem C e com o software interativo matlab, foram desenvolvidos nesse tempo, projetos de contadores utilizando arduino, projetos que automatizam e facilitam tarefas do nosso cotidiano com C, além de projetos de eletrônica em geral, como um projeto de planta residencial.')

    if st.button('Graduação'):
        st.write('Após a conclusão do meu ensino médio escolhi ingressar na faculdade de engenharia de computação, principalmente por ter me interessado por ciência da computação. Aqui estou aprimorando meus conhecimentos em desenvolvimento de sistemas, estou utilizando softwares de computação em nuvem da AWS, python para elaborar jogos, sites e para análise de dados, estou utilizando também javascript, html e css para desenvolvimento web.')

    cert = certificados()
    st.write(cert)

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