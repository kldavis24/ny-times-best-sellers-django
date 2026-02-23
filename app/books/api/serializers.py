from rest_framework import serializers
from books.services.enums import ListName

class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()
    publisher = serializers.CharField()
    description = serializers.CharField()
    rank = serializers.IntegerField()
    weeks_on_list = serializers.IntegerField()
    isbns = serializers.ListField(
        child = serializers.DictField(
            child = serializers.CharField()
        )
    )

class ListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    encoding = serializers.CharField()

class BookByListNameSerializer(serializers.Serializer):
    list_name = serializers.ChoiceField(
        choices=[list.value for list in ListName],
        required=True,
        error_messages={'invalid_choice': 'Invalid list name - accepted values: ' + ', '.join([list.value for list in ListName])}
    )

class BookByListNameAndDateSerializer(serializers.Serializer):
    list_name = serializers.ChoiceField(
        choices=[list.value for list in ListName],
        required=True,
        error_messages={'invalid_choice': 'Invalid list name - accepted values: ' + ', '.join([list.value for list in ListName])}
    )
    date = serializers.DateField(required=True)