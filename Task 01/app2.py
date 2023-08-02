import streamlit as st
import requests


def get_movie_details(movie_name, api_key):
    base_url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": api_key,
        "query": movie_name
    }
    response = requests.get(base_url, params=params)
    return response.json()

def get_movie_reviews(movie_id, api_key):
    base_url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"
    params = {
        "api_key": api_key,
    }
    response = requests.get(base_url, params=params)
    return response.json()

def main():

    st.title("Movie Review App")
    st.write("Enter the name of a movie to see its reviews.")

    # Get user input for movie name
    movie_name = st.text_input("Movie Name:")

    # Check if the user has entered a movie name
    if movie_name:
        # Get the API key from TMDb
        api_key = "c63d102859ab1933c74e4dfeff7850d8"  # Replace with your actual API key

        # Get the movie details from TMDb API
        movie_details = get_movie_details(movie_name, api_key)

        if movie_details.get("results"):
            movie_info = movie_details["results"][0]
            movie_id = movie_info["id"]
            movie_title = movie_info["title"]
            poster_path = movie_info["poster_path"]
            movie_synopsis = movie_info["overview"]
            # Get the movie reviews from TMDb API
            movie_reviews = get_movie_reviews(movie_id, api_key)

            if movie_reviews.get("results"):
                # Display cover photo of the movie
                poster_url = f"https://image.tmdb.org/t/p/w200{poster_path}"
                st.image(poster_url, use_column_width=True)
                st.markdown("<h4 style='text-align: center;'>" + movie_title + "</h4>", unsafe_allow_html=True)

                st.subheader("Synopsis:")
                st.write(movie_synopsis)
                st.write("----")
                st.subheader(f"Reviews for {movie_title}:")
                for review in movie_reviews["results"]:
                    author = review["author"]
                    content = review["content"]
                    st.markdown(f"**Author: {author}**")
                    st.write(content)
                    st.write("----")
            else:
                st.write("No reviews found for this movie.")
        else:
            st.write("Movie not found. Please check the movie name.")

if __name__ == "__main__":
    main()
