import streamlit as st
from PIL import Image

def explicacao():
    with st.expander('Ver detalhes Python:'):
        st.text('Utilizo python para analise de dados utilizando pandas, e até para criação de games como mostra o vídeo abaixo: ')
        video_file = open('arquivos/pygame.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    with st.expander('Ver detalhes HTML5 e CSS3:'):
        st.text('Utilizando HTML para a edição de textos e o CSS para a estilização, desenvolvo alguns sites simples, no projeto abaixo construi em conjunto com a ROCKETSEAT: ')
        video_file = open('arquivos/NLW.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    with st.expander('Ver detalhes javascript:'):
        st.text('Utilizando javascript, typescript, react e o CSS para a estilização, desenvolvi um site para encontrar duo em jogos online, no projeto abaixo também construi em conjunto com a ROCKETSEAT, porém dessa vez construí também um servidor para cadastrar os anúncios: ')
        video_file = open('arquivos/js.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    with st.expander('Ver detalhes Matlab:'):
        st.text('Para verificar a tensão e corrente em um sistema trifásico, foi plotado um gráfico das grandezas em função do tempo, como mostra abaixo: ')
        imagem_mat = Image.open('arquivos/matlab.jpg')
        st.image(imagem_mat)