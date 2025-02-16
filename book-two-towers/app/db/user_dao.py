import csv
from pathlib import Path

from app.db.types import User
from app.db.utils import convert_str_to_int


class UserDAO:
    def __init__(self):
        filepath = (
            Path(__file__)
            .parent.parent.joinpath("data")
            .joinpath("Users.csv")
            .resolve()
        )
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            self.data = [
                User(
                    user_id=str(row.get("User-ID")),
                    location=str(row.get("Location")),
                    age=convert_str_to_int(row.get("Age")),
                )
                for row in reader
            ]

    def get_user_count(self) -> int:
        return len(self.data)
