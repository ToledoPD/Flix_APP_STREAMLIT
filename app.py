import streamlit as st
from actors.page import show_actors
from genres.page import show_genres
from home.page import show_home
from login.page import show_login
from movies.page import show_movies
from reviews.page import show_reviews


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Flix App')

        menu_option = st.sidebar.selectbox(
            'Selecione uma opçao',
            ['Inicio', 'Generos', 'Atores/Atrizes', 'Filmes', 'Avaliaçoes']
        )

        if menu_option == 'Inicio':
            show_home()

        if menu_option == 'Generos':
            show_genres()

        if menu_option == 'Atores/Atrizes':
            show_actors()

        if menu_option == 'Filmes':
            show_movies()

        if menu_option == 'Avaliaçoes':
            show_reviews()


if __name__ == "__main__":
    main()
