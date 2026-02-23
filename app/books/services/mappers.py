from .dtos import Book, List

class BookMapper:
    def _map(payload: dict) -> Book:
        return Book(
            title = payload.get('title'),
            author = payload.get('author'),
            publisher = payload.get('publisher'),
            description = payload.get('description'),
            rank = payload.get('rank'),
            weeks_on_list = payload.get('weeks_on_list'),
            isbns = payload.get('isbns')
        )
    
class ListMapper:
    def _map(payload: dict) -> List:
        return List(
            id = payload.get('list_id'),
            name = payload.get('list_name'),
            encoding = payload.get('list_name_encoded')
        )
