from fastapi import APIRouter
router = APIRouter()


@router.get("/books")
def read_books():
    return books


books = [{"title": "Fooled by Randomness", "author": "Nassim Nicholas Taleb", "year": 2001},
         {"title": "Hunger Games", "author": "Suzanne Collins", "year": 2008},
         {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
         {"title": "The Wave", "author": "Todd Strasser", "year": 1981},
         {"title": "Warrior Cats", "author": "Erin Hunter", "year": 2003},
         {"title": "Wings of Fire", "author": "Tui T. Sutherland", "year": 2012}]
