import json
from pprint import pprint
# from pydantic import BaseModel
from typing import Optional, List
import pydantic

class ISBN10FormatError(Exception):

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

    '''validating isbn_10'''
    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value) -> None:
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        if sum((10 - i) * char_to_int(x) for i, x in enumerate(chars)) % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible by 11."
            )
        return value

def main() -> None:
    with open("data/book_data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        # print(books[0])
        # print(books[0].dict(exclude={"isbn_10"}))
        pprint(books)

        # print(data[0].title)

if __name__ == "__main__":
    main()