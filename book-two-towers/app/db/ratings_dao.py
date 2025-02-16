import csv
from pathlib import Path

from app.db.types import BookRating
from app.db.utils import convert_str_to_int


class RatingDAO:
    def __init__(self):
        filepath = (
            Path(__file__)
            .parent.parent.joinpath("data")
            .joinpath("Ratings.csv")
            .resolve()
        )
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            self.data = [
                BookRating(
                    user_id=str(row.get("User-ID")),
                    ISBN=str(row.get("ISBN")),
                    rating=convert_str_to_int(row.get('rating'))
                )
                for row in reader
            ]

    def get_rating_count(self) -> int:
        return len(self.data)
