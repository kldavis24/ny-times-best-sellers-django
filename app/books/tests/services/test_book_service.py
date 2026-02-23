import pytest
from unittest.mock import patch

from books.services.book_service import BookService
from books.services.enums import ListName
from books.services.dtos import Book, List
from books.services.exceptions import ExternalApiFormatError


@patch('books.services.book_service.ExternalBookApiClient.get')
def test_get_books_returns_mapped_books(mock_get, load_fixture):
    mock_get.return_value = load_fixture('overview.json')

    service = BookService()
    books = service.get_books()

    assert len(books) == 1
    assert isinstance(books[0], Book)
    assert books[0].title == 'Test Book'


@patch('books.services.book_service.ExternalBookApiClient.get')
def test_get_lists_returns_mapped_lists(mock_get, load_fixture):
    mock_get.return_value = load_fixture('lists.json')

    service = BookService()
    lists = service.get_lists()

    assert len(lists) == 1
    assert isinstance(lists[0], List)
    assert lists[0].encoding == 'hardcover-fiction'


@patch('books.services.book_service.ExternalBookApiClient.get')
def test_get_books_by_list_name(mock_get, load_fixture):
    mock_get.return_value = load_fixture('books_by_list.json')

    service = BookService()
    books = service.get_books_by_list_name(ListName.HARDCOVER_FICTION)

    assert len(books) == 1
    assert books[0].title == 'List Book'


def test_get_books_by_list_name_and_date_invalid_date_raises():
    service = BookService()

    with pytest.raises(ValueError):
        service.get_books_by_list_name_and_date(
            ListName.HARDCOVER_FICTION,
            '2025-99-99',
        )


@patch('books.services.book_service.ExternalBookApiClient.get')
def test_get_books_by_list_name_and_date_valid(mock_get, load_fixture):
    mock_get.return_value = load_fixture('books_by_list.json')

    service = BookService()
    books = service.get_books_by_list_name_and_date(
        ListName.HARDCOVER_FICTION,
        '2025-01-01',
    )

    assert len(books) == 1


@patch('books.services.book_service.ExternalBookApiClient.get')
def test_get_books_empty_lists_returns_empty(mock_get, load_fixture):
    mock_get.return_value = load_fixture('overview_empty_lists.json')

    service = BookService()
    books = service.get_books()

    assert books == []


@patch('books.services.book_service.ExternalBookApiClient.get')
def test_get_books_missing_results_raises(mock_get, load_fixture):
    mock_get.return_value = load_fixture('overview_missing_results.json')

    service = BookService()

    with pytest.raises(ExternalApiFormatError):
        service.get_books()


@patch('books.services.book_service.ExternalBookApiClient.get')
def test_get_books_missing_books_key_raises(mock_get, load_fixture):
    mock_get.return_value = load_fixture('overview_missing_books.json')

    service = BookService()

    with pytest.raises(ExternalApiFormatError):
        service.get_books()


@patch('books.services.book_service.ExternalBookApiClient.get')
def test_get_books_by_list_empty_returns_empty(mock_get, load_fixture):
    mock_get.return_value = load_fixture('books_by_list_empty.json')

    service = BookService()
    books = service.get_books_by_list_name('hardcover-fiction')

    assert books == []