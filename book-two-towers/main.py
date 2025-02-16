from app.db.bookDAO import BookDAO
from app.db.ratings_dao import RatingDAO
from app.db.user_dao import UserDAO


def main():
    book_dao = BookDAO()
    print(f"Number of books: {book_dao.get_number_of_books():,.0f}")
    user_dao = UserDAO()
    print(f"Number of users: {user_dao.get_user_count():,.0f}")
    rating_dao = RatingDAO()
    print(f"Number of ratings: {rating_dao.get_rating_count():,.0f}")


if __name__ == "__main__":
    main()
