from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


posts: list[dict] = [
    {
        "id":1,
        "author":"kritika",
        "title":"fast api",
        "content":"this is the details of fast api",
        "date_posted":"july 19,2026",
    },
    {
        "id":2,
        "author":"ipshita",
        "title":"fast api",
        "content":"this is the details of fast api",
        "date_posted":"july 20,2026",
    },
]


@app.get("/",response_class=HTMLResponse)
@app.get("/posts",response_class=HTMLResponse)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts