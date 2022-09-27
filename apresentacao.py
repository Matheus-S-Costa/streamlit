import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title='Portfolio Matheus Costa' ,layout="wide",page_icon='💻')

st.markdown('---')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.sidebar.title('Portfólio pessoal')
imagem_perfil = Image.open('perfil1.png')
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
    imagem_scrum = Image.open('scrum2.png')
    st.image(imagem_scrum)
elif visual == 'Carreira':
    st.header('Linha do tempo carreira🥇')
    image = Image.open('timeline.png')
    st.image(image)
    st.markdown('---')
    st.header('Educação 📖')
    if st.button('Ensino Médio'):
        st.write('Em 2017 iniciei meus estudos no Colégio Técnico da UFMG, com o ensino médio e técnico integrado, tive meu primeiro contato com programação, tive contato com a linguagem C e com o software interativo matlab, foram desenvolvidos nesse tempo, projetos de contadores utilizando arduino, projetos que automatizam e facilitam tarefas do nosso cotidiano com C, além de projetos de eletrônica em geral, como um projeto de planta residencial.')

    if st.button('Graduação'):
        st.write('Após a conclusão do meu ensino médio escolhi ingressar na faculdade de engenharia de computação, principalmente por ter me interessado por ciência da computação. Aqui estou aprimorando meus conhecimentos em desenvolvimento de sistemas, estou utilizando softwares de computação em nuvem da AWS, python para elaborar jogos, sites e para análise de dados, estou utilizando também javascript, html e css para desenvolvimento web.')

    st.header('Certificados 📃')
    st.write('Estou sempre em busca de construir novos métodos que facilitem nosso dia-a-dia, tanto para empresas quanto para uso pessoal. Confira meus projetos no github (link na aba lateral).')
    st.write('Agora, para que meus principais certificados possam ser vistos, há alguns botões referentes aos certificados com imagens que podem ser expandidas para facilitar a visualização. Sempre estou em busca de me manter atualizado, portanto, haverá um link com meus certificados, no qual estará em constante atualização!')
    url_certificados = "https://drive.google.com/drive/folders/1jwOozs2G5rkWRYNifckZIb-g8UxVrT6e?usp=sharing"
    st.write("📜-[Alguns dos meus certificados](%s)" % url_certificados)
    col6, col7, col8 = st.columns(3)
    with col6:
        if st.button('Fundamentos Linux Cisco') == True:
            image1 = Image.open('FundamentosLinuxCertificate1.jpg')
            st.image(image1)
    with col7:
        if st.button('Cybersecurity Cisco'):
            image2 = Image.open('CyberSecurityCertificate1.jpg')
            st.image(image2)
    with col8:
        if st.button('Programming Essentials in C'):
            image3 = Image.open('ProgrammingC_Certificate1.jpg')
            st.image(image3)

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
    with st.expander('Ver detalhes Python:'):
        st.text('Utilizo python para analise de dados utilizando pandas, e até para criação de games como mostra o vídeo abaixo: ')
        video_file = open('pygame.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    with st.expander('Ver detalhes HTML5 e CSS3:'):
        st.text('Utilizando HTML para a edição de textos e o CSS para a estilização, desenvolvo alguns sites simples, no projeto abaixo construi em conjunto com a ROCKETSEAT: ')
        video_file = open('NLW.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    with st.expander('Ver detalhes javascript:'):
        st.text('Utilizando javascript, typescript, react e o CSS para a estilização, desenvolvi um site para encontrar duo em jogos online, no projeto abaixo também construi em conjunto com a ROCKETSEAT, porém dessa vez construí também um servidor para cadastrar os anúncios: ')
        video_file = open('js.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    with st.expander('Ver detalhes Matlab:'):
        st.text('Para verificar a tensão e corrente em um sistema trifásico, foi plotado um gráfico das grandezas em função do tempo, como mostra abaixo: ')
        imagem_mat = Image.open('matlab.jpg')
        st.image(imagem_mat)
    st.markdown('---')
    st.subheader('Ferramentas e experiências ⚒️')
    col3, col4, col5 = st.columns(3)
    with col3:
        st.button('Javascript')
    with col3:
        st.button('HTML5 e CSS3')
    with col3:
        st.button('Python')
    with col3:
        st.button('Streamlit')
    with col3:
        st.button('Pygame')
    with col4:
        st.button('Analise de dados')
    with col4:
        st.button('C')
    with col4:
        st.button('C++')
    with col4:
        st.button('AWS EC2')
    with col5:
        st.button('Cloud Fundations Google e AWS')
    with col5:
        st.button('VSCode')
    with col5:
        st.button('Pycharm')
    with col5:
        st.button('MatLab')


st.sidebar.title('Vamos trabalhar juntos?')
st.sidebar.subheader('Contate-me: ')
st.sidebar.write('📧: matheusilva334@gmail.com')
url_git = 'https://github.com/Matheus-S-Costa'
st.sidebar.write("🖥-[GitHub](%s)" % url_git)
url_linkedin = 'https://www.linkedin.com/in/matheus-s-costaa/'
st.sidebar.write('📱-[LinkedIn](%s)' % url_linkedin)
url_curriculo = 'https://drive.google.com/drive/folders/1YjqPgTkX0X51XKj8plJrlPF6yiWzjYyu'
st.sidebar.write("📃-[Meu curículo](%s)" % url_curriculo)

