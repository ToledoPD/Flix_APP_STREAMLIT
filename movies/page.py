import pandas as pd
import streamlit as st
from movies.service import MovieService
from st_aggrid import AgGrid
from actors.service import ActorService
from genres.service import GenreService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Lista de Filmes: ')
        movies_df = pd.json_normalize(movies)
        print(movies_df.columns)
        movies_df = movies_df.drop(columns=['actors', 'genre'])
        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum filme cadastrado.')

    st.title('Cadastrar novo filme')

    title = st.text_input('Nome do filme')

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}
    select_genre_name = st.selectbox('Genero', list(genre_names.keys()))

    realease_date = st.date_input(
        label='Data de lançamento',
        format='DD/MM/YYYY',
    )

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    select_actors_names = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    select_actors_ids = [actor_names[name] for name in select_actors_names]

    resume = st.text_area('Resumo')

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            genre=genre_names[select_genre_name],
            realease_date=realease_date,
            actors=select_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error(f' Erro ao cadastrar filme "{title}')
