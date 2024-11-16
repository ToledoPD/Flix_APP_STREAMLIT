import streamlit as st
from movies.respository import MovieRepository


class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.movie_repository.get_movies()
        st.session_state.movies = movies
        return movies

    def create_movie(self, title, genre, realease_date, actors, resume):
        movie = dict(
            title=title,
            genre=genre,
            realease_date=realease_date,
            actors=actors,
            resume=resume,
        )
        new_movie = st.session_state.create_movie(movie)
        st.session_state.movies.append(new_movie)
        return new_movie

    def get_movie_stats(self):
        return self.movie_repository.get_movies_stats()
