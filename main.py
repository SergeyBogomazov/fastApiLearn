from fastapi import FastAPI, Query
from schemas import Book

app = FastAPI()

users = []
books = []


@app.get('/')
def root():
    return {"key": "Im root"}


@app.get('/users')
def get_users():
    return {
        "users": " ".join(users)
    }


@app.get('/user/{user_id}/items/{item_id}/')
def get_user_item(user_id: int, item_id: int):
    return {
        "user": user_id, "item": item_id
    }


@app.get('/books')
def get_books():
    return books


@app.post('/books')
def create_book(book: Book):
    books.append(book)
    return {
        "result": "ok"
    }


@app.get('/book')
def get_book(keywords: list[str] = Query([], description="return book that most suitable for keywords")):
    return keywords
