from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    
    if published:
        return {"data": f"{limit} published blogs from the db"}
    return {"data": f"{limit} blogs from the db"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "Show all unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"data": {"Comment 1", "Comment 2"}}


@app.post("/blog/save")
def create_blog(blog: Blog):
    return {'data': f"Blog is created with title as {blog.title}"}
