import pandas as pd
import streamlit as st
from movies.service import MovieService
from reviews.service import ReviewsService
from st_aggrid import AgGrid


def show_reviews():
    review_service = ReviewsService()
    reviews = review_service.get_reviews()

    if reviews:
        st.write('Lista de Avaliações: ')

        reviews_df = pd.json_normalize(reviews)

        AgGrid(
            data=pd.DataFrame(reviews_df),
            reload_data=True,
            key='reviews_grid',
        )
    else:
        st.warning('Nenhuma avaliação encontrada.')

    st.title('Cadastrar uma nova avaliação')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movies_titles = {movie['title']: movie['id'] for movie in movies}
    select_movie_title = st.selectbox('filme', list(movies_titles.keys()))

    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )

    comment = st.text_area('Comentario')

    if st.button('Cadastar'):
        new_review = review_service.create_review(
            movie=movies_titles[select_movie_title],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar a avaliação. Verifque os campos')
