import pandas as pd
from pathlib import Path

from rich import print

def load_books():
    filepath = Path(__file__).parent.joinpath('app').joinpath('data').joinpath('Books.csv')
    books = pd.read_csv(filepath)
    return books

def load_ratings():
    filepath = Path(__file__).parent.joinpath('app').joinpath('data').joinpath('Ratings.csv')
    return pd.read_csv(filepath)

def load_users():
    filepath = Path(__file__).parent.joinpath('app').joinpath('data').joinpath('Users.csv')
    return pd.read_csv(filepath)

def main():
    books = load_books()
    users = load_users()
    ratings = load_ratings()
    print("Books")
    print(f" Columns: {", ".join(books.columns)}")
    print(f" book dataframe shape: {books.shape}")
    print('')

    print("Users")
    print(f" Columns: {", ".join(users.columns)}")
    print(f" User dataframe shape: {users.shape}")
    print('')

    print("Ratings")
    print(f" Columns: {", ".join(ratings.columns)}")
    print(f" Rating dataframe shape: {ratings.shape}")
    print('')


if __name__ == '__main__':
    main()





