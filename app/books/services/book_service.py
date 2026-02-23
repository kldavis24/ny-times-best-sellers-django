from .external_api_client import ExternalBookApiClient
from .dtos import Book, List
from datetime import datetime, date
from .contracts import externalService
from .enums import ExternalService, ListName
from .mappers import BookMapper, ListMapper
from .exceptions import ExternalApiFormatError


class BookService(externalService):
    def __init__(self):
        self.client = ExternalBookApiClient()

    def external_service(self) -> str:
        return ExternalService.NY_TIMES_BEST_SELLERS_BOOKS.name
    
    def external_service_id(self) -> int:
        return ExternalService.NY_TIMES_BEST_SELLERS_BOOKS.value

    def get_books(self) -> list[Book]:
        response = self.client.get('/svc/books/v3/lists/overview.json')

        try:
            lists = response['results']['lists']
            if not lists:
                return []  # or raise ExternalApiFormatError('No lists in response')

            books = lists[0]['books']
        except (KeyError, TypeError):
            raise ExternalApiFormatError('Invalid overview response format')

        return self._map_books(books)
    
    def get_lists(self) -> list[List]:
        response = self.client.get('/svc/books/v3/lists/overview.json')

        try:
            lists = response['results']['lists']
        except (KeyError, TypeError):
            raise ExternalApiFormatError('Invalid lists response format')

        return self._map_lists(lists)
    
    def get_books_by_list_name(self, list_name: str) -> list[Book]:
        response = self.client.get(f'/svc/books/v3/lists/current/{list_name}.json')

        try:
            books = response['results']['books']
        except (KeyError, TypeError):
            raise ExternalApiFormatError('Invalid books-by-list response format')

        return self._map_books(books)
    
    def get_books_by_list_name_and_date(self, list_name: str, date: str) -> list[Book]:
        if not self.is_valid_date_format(date):
            raise ValueError('Invalid date format')

        response = self.client.get(f'/svc/books/v3/lists/{date}/{list_name}.json')

        try:
            books = response['results']['books']
        except (KeyError, TypeError):
            raise ExternalApiFormatError('Invalid books-by-list-and-date response format')

        return self._map_books(books)
    
    def _map_books(self, books: list) -> list[Book]:
        return [
            BookMapper._map(book)
            for book in books
        ]
    
    def _map_lists(self, lists: list) -> list[List]:
        return [
            ListMapper._map(list)
            for list in lists
        ]
    
    def is_valid_date_format(self, date_string):
        try:
            datetime.strptime(date_string, '%Y-%m-%d')

            return True
        except ValueError:
            return False
