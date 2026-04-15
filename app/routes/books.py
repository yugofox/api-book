from fastapi import APIRouter
router = APIRouter()

books = [{"id": 1, "title": "Fooled by Randomness", "author": "Nassim Nicholas Taleb", "year": 2001},
         {"id": 2, "title": "Hunger Games",
             "author": "Suzanne Collins", "year": 2008},
         {"id": 3, "title": "The Great Gatsby",
             "author": "F. Scott Fitzgerald", "year": 1925},
         {"id": 4, "title": "The Wave", "author": "Todd Strasser", "year": 1981},
         {"id": 5, "title": "Warrior Cats", "author": "Erin Hunter", "year": 2003},
         {"id": 6, "title": "Wings of Fire", "author": "Tui T. Sutherland", "year": 2012}]


@router.get("/books")
def read_books():
    return books


@router.post("/books")
def add_book(book: dict):
    books.append(book)
    return {"message": "book added successfully 𐔌*ˊᵕˋ*𐦯"}


@router.put("/books/{book_id}")
def update_book(book_id: int, book: dict):
    for i, b in enumerate(books):
        if b["id"] == book_id:
            books[i] = book
            return {"message": "book updated successfully 𐔌*ˊᵕˋ*𐦯"}
    return {"message": "book not found (ㅠ﹏ㅠ)"}


@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, b in enumerate(books):
        if b["id"] == book_id:
            del books[i]
            return {"message": "book deleted successfully 𐔌*ˊᵕˋ*𐦯"}
    return {"message": "book not found (ㅠ﹏ㅠ)"}
