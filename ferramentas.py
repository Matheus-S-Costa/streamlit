import streamlit as st

def ferramenta():

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
    with col4:
        st.button('SQLite')
    with col5:
        st.button('Cloud Fundations Google e AWS')
    with col5:
        st.button('VSCode')
    with col5:
        st.button('Pycharm')
    with col5:
        st.button('MatLab')

# todas habilidades em colunas