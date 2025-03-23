# Movie Recommender System

This project implements a movie recommendation system using Natural Language Processing (NLP) techniques. It utilizes a movie dataset from Kaggle, performs data cleaning and feature engineering, and applies Count Vectorizer and cosine similarity to recommend similar movies based on user selection. The system is deployed as an interactive web application using Streamlit.

## Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/Vedant1124/Movie-Recommender-System.git](https://www.google.com/search?q=https://github.com/YourGitHubUsername/Movie-Recommender-System.git)
   cd Movie-Recommender-System

Create a virtual environment (recommended):

Bash

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate # On macOS and Linux
Install dependencies:

Bash

pip install -r requirements.txt
Usage
Run the Streamlit application:

Bash

streamlit run app.py
Open the URL provided in the terminal in your web browser.

Select a movie from the dropdown menu and click "Recommend" to see 5 similar movie recommendations with their posters.

Dependencies
streamlit
pandas
scikit-learn (specifically CountVectorizer)
requests
Pillow
(Make sure you have a requirements.txt file in your project root with these dependencies.)

Data
The movie dataset was obtained from Kaggle. It was preprocessed by cleaning the data and combining relevant text features (e.g., overview, genres, keywords, cast) into a single text column for NLP analysis.

Project Structure
Movie-Recommender-System/
├── app.py           # Streamlit application
├── movies.pkl        # Movie data (DataFrame)
├── similarity.pkl    # Similarity matrix
├── requirements.txt  # Project dependencies
├── README.md         # Project documentation
└── .gitignore        # Files to ignore
How It Works
Data Preprocessing: The Kaggle dataset is cleaned and relevant textual data is combined.
Vectorization: Count Vectorizer is used to convert the text data into numerical vectors.
Similarity Calculation: Cosine similarity is calculated between movie vectors to determine movie similarity.
Recommendation: Based on the selected movie, the top 5 similar movies are recommended.
Streamlit App: An interactive web application is created using Streamlit to display movie recommendations.
