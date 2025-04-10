## MOVIE RECOMMENDATION SYSTEM 

Welcome to this movie recommendation system that combines machine learning and TMDB DATABASE

## Working princple 

1. **Data Loading**: The movie data and similarity matrix are loaded from pre-trained `.pkl` files.
2. **User Input**: The user selects a movie from the dropdown.
3. **Recommendation Logic**: The system calculates the similarity between the selected movie and others in the dataset and recommends the top 5 similar movies.
## cosine_similarity(A,B)= A.B/∥A∥∥B∥
where A .B is the dot vector of the vector A and B and ∥A∥∥B∥ are the magnitudes of the vector A and B respectively 
​here , it the unique words will be tokenized and will be stored in a matrix and be used to calculate the smiiarity between two movies

4. **Poster Display**: For each recommended movie, the corresponding poster image is fetched from the TMDb API using the movie ID.
5. **Display**: The recommended movies and their posters are displayed in a grid format on the Streamlit app.

## INSTALLATION
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your TMDb API key:
   - Use the  `.env` file  and add your API key like this:
     ```env
     TMDB_API_KEY=your_api_key_here
    
     ```
4. Use the movierecomm.ipynb file to create the pre-trained models     
## Usage

After installation, you can run the app by using Streamlit:

```bash
streamlit run app.py

## Future Improvements

- I'll add  more complex recommendation algorithms (e.g., collaborative filtering).
- Include movie ratings and reviews in the recommendations.
- Allow users to filter recommendations by genre or year.



    

