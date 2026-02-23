from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from books.services.book_service import BookService
from books.services.enums import ListName
from .serializers import BookSerializer, ListSerializer, BookByListNameSerializer, BookByListNameAndDateSerializer
from books.services.exceptions import ExternalApiFormatError
from rest_framework.exceptions import APIException


class UpstreamApiError(APIException):
    status_code = 502
    default_detail = 'Upstream service returned invalid data.'

class GetBooksView(APIView):
    def get(self, request):
        service = BookService()

        try:
            books = service.get_books()
        except ExternalApiFormatError:
            raise UpstreamApiError()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=200)
    
class ListsView(APIView):
    def get(self, request) -> Response|None:
        service = BookService()

        try:
            lists = service.get_lists()
        except ExternalApiFormatError:
            raise UpstreamApiError()

        serializer = ListSerializer(lists, many = True)

        return Response(serializer.data, status = status.HTTP_200_OK)
    
class GetBooksByListNameView(APIView):
    def get(self, request, list_name):
        request_serializer = BookByListNameSerializer(data={'list_name': list_name})
        request_serializer.is_valid(raise_exception=True)

        service = BookService()
        list_name = ListName(list_name)

        try:
            books = service.get_books_by_list_name(list_name)
        except ExternalApiFormatError:
            raise UpstreamApiError()

        book_serializer = BookSerializer(books, many = True)

        return Response(book_serializer.data, status = status.HTTP_200_OK)
    
class GetBooksByListNameAndDateView(APIView):
    def get(self, request, list_name, date):
        request_serializer = BookByListNameAndDateSerializer(data={'list_name': list_name, 'date': date})
        request_serializer.is_valid(raise_exception=True)

        service = BookService()
        list_name = ListName(list_name)

        try:
            books = service.get_books_by_list_name_and_date(list_name, date)
        except ExternalApiFormatError:
            raise UpstreamApiError()

        book_serializer = BookSerializer(books, many = True)

        return Response(book_serializer.data, status = status.HTTP_200_OK)
