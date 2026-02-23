from dataclasses import dataclass
from datetime import date

@dataclass
class Book:
    title: str
    author: str
    publisher: str
    description: str
    rank: int
    weeks_on_list: int
    isbns: list

@dataclass
class List:
    id: int
    name: str
    encoding: str
