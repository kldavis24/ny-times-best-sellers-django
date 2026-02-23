import pytest
pytestmark = pytest.mark.django_db

from unittest.mock import patch
from rest_framework.test import APIClient
from rest_framework import status

from books.services.dtos import Book, List
from books.services.enums import ListName


@pytest.fixture
def client():
    return APIClient()


def fake_book():
    return Book(
        title='Test',
        author='A',
        publisher='P',
        description='D',
        rank=1,
        weeks_on_list=1,
        isbns=[],
    )


def fake_list():
    return List(
        id=1,
        name='Hardcover Fiction',
        encoding='hardcover-fiction',
    )


@patch('books.api.views.BookService.get_books')
def test_get_books_success(mock_get_books, client):
    mock_get_books.return_value = [fake_book()]

    resp = client.get('/api/books/')

    assert resp.status_code == status.HTTP_200_OK
    assert len(resp.json()) == 1
    assert resp.json()[0]['title'] == 'Test'


@patch('books.api.views.BookService.get_lists')
def test_get_lists_success(mock_get_lists, client):
    mock_get_lists.return_value = [fake_list()]

    resp = client.get('/api/lists/')

    assert resp.status_code == 200
    assert resp.json()[0]['encoding'] == 'hardcover-fiction'


def test_get_books_by_list_name_invalid_choice(client):
    resp = client.get('/api/books/list/not-a-real-list/')

    assert resp.status_code == 400
    assert 'list_name' in resp.json()


@patch('books.api.views.BookService.get_books_by_list_name')
def test_get_books_by_list_name_success(mock_method, client):
    mock_method.return_value = [fake_book()]

    resp = client.get(f'/api/books/list/{ListName.HARDCOVER_FICTION.value}/')

    assert resp.status_code == 200
    assert resp.json()[0]['title'] == 'Test'


def test_get_books_by_list_name_and_date_invalid_date(client):
    resp = client.get(
        f'/api/books/list/{ListName.HARDCOVER_FICTION.value}/date/2025-99-99/'
    )

    assert resp.status_code == 400
    assert 'date' in resp.json()


@patch('books.api.views.BookService.get_books_by_list_name_and_date')
def test_get_books_by_list_name_and_date_success(mock_method, client):
    mock_method.return_value = [fake_book()]

    resp = client.get(
        f'/api/books/list/{ListName.HARDCOVER_FICTION.value}/date/2025-01-01/'
    )

    assert resp.status_code == 200
    assert resp.json()[0]['title'] == 'Test'


@patch('books.api.views.BookService.get_books')
def test_api_returns_502_on_bad_upstream(mock_get, client):
    from books.services.exceptions import ExternalApiFormatError

    mock_get.side_effect = ExternalApiFormatError('bad format')

    resp = client.get('/api/books/')

    assert resp.status_code == 502