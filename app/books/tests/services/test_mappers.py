from books.services.mappers import BookMapper, ListMapper
from books.services.dtos import Book, List

def test_book_mapper_maps_payload_correctly():
    payload = {
        'title': 'Test',
        'author': 'Author',
        'publisher': 'Pub',
        'description': 'Desc',
        'rank': 1,
        'weeks_on_list': 5,
        'isbns': [{'isbn10': '', 'isbn13': '123'}],
    }

    book = BookMapper._map(payload)

    assert isinstance(book, Book)
    assert book.title == 'Test'
    assert book.rank == 1
    assert book.isbns == [{'isbn10': '', 'isbn13': '123'}]


def test_list_mapper_maps_payload_correctly():
    payload = {
        'list_id': 704,
        'list_name': 'Combined Print & E-Book Fiction',
        'list_name_encoded': 'combined-print-and-e-book-fiction',
    }

    lst = ListMapper._map(payload)

    assert isinstance(lst, List)
    assert lst.id == 704
    assert lst.encoding == 'combined-print-and-e-book-fiction'