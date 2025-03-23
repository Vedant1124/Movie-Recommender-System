# Movie Recommendation System (NLP-Powered)

This project develops a content-based movie recommendation system utilizing Natural Language Processing (NLP) techniques. It leverages a Kaggle dataset, performs data preprocessing, and employs Count Vectorizer and cosine similarity to generate recommendations. A user-friendly web interface is provided through Streamlit.

## Project Overview

The system aims to provide users with relevant movie suggestions based on their selected movie. It processes textual movie data, extracts meaningful features, and calculates similarity scores to deliver personalized recommendations.

## Installation

1.  Clone the repository:

    ```bash
    git clone [your-repo-url]
    cd Movie-Recommender-System
    ```

2.  Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

## Usage

1.  Open the Streamlit application in your web browser.
2.  Select a movie from the dropdown menu.
3.  Click the "Recommend" button to generate a list of 5 similar movie recommendations, including movie posters.

## Dependencies

-   streamlit
-   pandas
-   scikit-learn (CountVectorizer)
-   requests
-   Pillow

## Data Source and Preprocessing

The movie dataset was sourced from [Kaggle Dataset Link]. Data preprocessing involved cleaning and combining relevant textual features (overview, genres, keywords, cast) to enhance NLP analysis.

## Project Structure
