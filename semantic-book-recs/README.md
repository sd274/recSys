# Semantic Book Recommendations

This is a simple app that can find book recommendations based on simanitic similarity to a given request. 

The semantic similarity is done using a `sentence-transformers/all-MiniLM-L6-v2` embedding model.

Similarity search is done using a greedy search using jax, as the number of books is very small this is efficitent. 


Requirements can be installed via poetry by running `poetry install --with dev` and then the app can be ran using `poetry run python run_app.py`
