from fastapi import FastAPI
import app.routes.books as book_router
app = FastAPI()
app.include_router(book_router.router)


@app.get("/")
def read_root():
    return {"message": "shinx was here ≽^•⩊•^≼"}
