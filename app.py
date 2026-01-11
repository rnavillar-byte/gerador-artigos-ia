import streamlit as st
from services.wordpress_service import get_wordpress_posts

st.set_page_config(page_title='Gerador de Artigos IA - Melivo', layout='wide')

st.markdown("""
# 🧠 Gerador de Artigos com IA – Melivo  
Crie artigos sobre ferramentas de Inteligência Artificial seguindo o padrão editorial do seu site.
""")
st.divider()

with st.container():
    st.subheader('🔗 Conectar ao seu WordPress')
    col1, col2 = st.columns([3,1])
    with col1:
        site_url = st.text_input('URL do seu site WordPress', placeholder='https://melivo.com.br')
    with col2:
        qtd = st.number_input('Quantos artigos buscar?', min_value=1, max_value=50, value=10)
    buscar = st.button('📥 Buscar artigos publicados')

if buscar:
    if not site_url:
        st.error('Informe a URL do seu site.')
    else:
        with st.spinner('Buscando artigos no WordPress...'):
            posts, error = get_wordpress_posts(site_url, qtd)
        if error:
            st.error(f'Erro ao buscar artigos: {error}')
        else:
            st.success(f'{len(posts)} artigos encontrados!')
            st.subheader('📚 Artigos já publicados')
            for i, post in enumerate(posts, start=1):
                st.markdown(f"""
**{i}. {post['title']}**  
Slug: `{post['slug']}`  
Data: {post['date']}
---
""")

st.divider()
st.caption('Projeto: Gerador de Artigos IA para Melivo • Fase 1')
