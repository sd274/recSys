import csv
from pathlib import Path

from app.db.types import Book
from app.db.utils import convert_str_to_int


class BookDAO:
    def __init__(self):
        filepath = Path(__file__).parent.parent.joinpath('data').joinpath('Books.csv').resolve()
        with open(filepath, 'r') as file:
            reader  =csv.DictReader(file)
            self.data = [
                Book(
                    ISBN=str(row.get('ISBN')),
                    title=str(row.get('Book-Title')),
                    author=str(row.get('Book-Author')),
                    publisher=str(row.get('Publisher')),
                    published_year=convert_str_to_int(row.get('Year-Of-Publication'))
                )
                for row in reader
            ]

    def get_number_of_books(self)-> int:
        return len(self.data)


