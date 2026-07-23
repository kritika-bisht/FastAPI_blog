from fastapi import FastAPI,Request
#from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")  

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


@app.get("/",include_in_schema=False,name="home")
@app.get("/posts",include_in_schema=False,name="posts")
def home(request: Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts,"title":"home page"})

@app.get("/api/posts")
def get_posts():
    return posts