from enum import Enum, StrEnum, IntEnum

class ExternalService(IntEnum):
    NY_TIMES_BEST_SELLERS_BOOKS = 1


class ListName(StrEnum):
    COMBINED_PRINT_AND_EBOOK_FICTION = 'combined-print-and-e-book-fiction'
    COMBINED_PRINT_AND_EBOOK_NONFICTION = 'combined-print-and-e-book-nonfiction'
    HARDCOVER_FICTION = 'hardcover-fiction'
    HARDCOVER_NONFICTION = 'hardcover-nonfiction'
    TRADE_FICTION_PAPERBACK = 'trade-fiction-paperback'
    PAPERBACK_NONFICTION = 'paperback-nonfiction'
    ADVICE_HOW_TO_AND_MISC = 'advice-how-to-and-miscellaneous'
    CHILDRENS_MIDDLE_GRADE_HARDCOVER = 'childrens-middle-grade-hardcover'
    PICTURE_BOOKS = 'picture-books'
    SERIES_BOOKS = 'series-books'
    YOUNG_ADULT_HARDCOVER = 'young-adult-hardcover'
    AUDIO_FICTION = 'audio-fiction'
    AUDIO_NONFICTION = 'audio-nonfiction'
    BUSINESS_BOOKS = 'business-books'
    GRAPHIC_BOOKS_AND_MANGA = 'graphic-books-and-manga'
    MASS_MARKET_MONTHLY = 'mass-market-monthly'
    MIDDLE_GRADE_PAPERBACK_MONTHLY = 'middle-grade-paperback-monthly'
    YOUNG_ADULT_PAPERBACK_MONTHLY = 'young-adult-paperback-monthly'
