import streamlit as st
from PIL import Image

def certificados():
    st.header('Certificados 📃')
    st.write('Estou sempre em busca de construir novos métodos que facilitem nosso dia-a-dia, tanto para empresas quanto para uso pessoal. Confira meus projetos no github (link na aba lateral).')
    st.write('Agora, para que meus principais certificados possam ser vistos, há alguns botões referentes aos certificados com imagens que podem ser expandidas para facilitar a visualização. Sempre estou em busca de me manter atualizado, portanto, haverá um link com meus certificados, no qual estará em constante atualização!')
    url_certificados = "https://drive.google.com/drive/folders/1jwOozs2G5rkWRYNifckZIb-g8UxVrT6e?usp=sharing"
    st.write("📜-[Alguns dos meus certificados](%s)" % url_certificados)
    col6, col7, col8 = st.columns(3)
    with col6:
        if st.button('Fundamentos Linux') == True:
            image1 = Image.open('arquivos/FundamentosLinuxCertificate1.jpg')
            st.image(image1)
    with col7:
        if st.button('Cybersecurity Cisco'):
            image2 = Image.open('arquivos/CyberSecurityCertificate1.jpg')
            st.image(image2)
    with col8:
        if st.button('Programming Essentials in C'):
            image3 = Image.open('arquivos/ProgrammingC_Certificate1.jpg')
            st.image(image3)