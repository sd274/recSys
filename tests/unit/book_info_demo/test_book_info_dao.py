import jax.numpy as jnp

from app.book_info_dao.book_info_dao import BookInfoDAO
from app.book_info_dao.types import Book


def test_compute_similarity():
    vector = jnp.array([1, 2, 3, 4])
    embeddings = [[1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 5.0, 5.0], [7.0, 7.0, 7.0, 7.0]]
    sims = BookInfoDAO._compute_similarity(vector, jnp.array(embeddings))
    assert jnp.round(sims[0], 2) == 1.00

    expected = (1 + 2 * 2 + 3 * 5 + 4 * 5) / (
        (1**2 + 2**2 + 3**2 + 4**2) ** 0.5 * (1**2 + 2**2 + 5**2 + 5**2) ** 0.5
    )
    assert jnp.round(sims[1], 5) == jnp.round(expected, 5)

    expected = (7 + 2 * 7 + 3 * 7 + 4 * 7) / (
        (1**2 + 2**2 + 3**2 + 4**2) ** 0.5 * (4 * 7**2) ** 0.5
    )
    assert jnp.round(sims[2], 5) == jnp.round(expected, 5)


def test_book_dao():
    embeddings = [[1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 5.0, 5.0], [7.0, 7.0, 7.0, 7.0]]
    items = [
        Book(title="stu", description="day"),
        Book(title="greg", description="rendle"),
        Book(title="chris", description="chadwick"),
    ]
    dao = BookInfoDAO(embeddings, items)
    res = dao.similarity_search([1, 2, 3, 4], n=1)
    assert res[0].title == "stu"

    res = dao.similarity_search([1, 2, 5, 4], n=1)
    assert res[0].title == "greg"

    res = dao.similarity_search([7, 7, 7, 6], n=1)
    assert res[0].title == "chris"
