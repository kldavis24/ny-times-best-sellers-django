from django.urls import path
from .views import GetBooksView, ListsView, GetBooksByListNameView, GetBooksByListNameAndDateView

urlpatterns = [
    path('books/', GetBooksView.as_view()),
    path('lists/', ListsView.as_view()),
    path('books/list/<str:list_name>/', GetBooksByListNameView.as_view()),
    path('books/list/<str:list_name>/date/<str:date>/', GetBooksByListNameAndDateView.as_view()),
]
