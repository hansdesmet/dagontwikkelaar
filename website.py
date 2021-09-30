from starlette.applications import Starlette
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.routing import Route
from repository import read_votes, cat_voted, dog_voted

html ="""
    <html>
    <body>
        <div>cat: catVotes</div>
        <div>dog: dogVotes</div>
        <form method="post" action="cat">
            <button>i love cat</button>
        </form>
        <form method="post" action="dog">
            <button>i love dog</button>
        </form>
    </body>
    </html>
"""

def home_page(request):
    votes = read_votes()    
    return HTMLResponse(html.replace("catVotes", str(votes.cat))
        .replace("dogVotes", str(votes.dog)))

def love_cat(request):
    cat_voted()
    return RedirectResponse(url = "/", status_code=302)

def love_dog(request):
    dog_voted()
    return RedirectResponse(url = "/", status_code=302)


routes = [
    Route("/", home_page),
    Route("/cat", love_cat, methods=["POST"]),
    Route("/dog", love_dog, methods=["POST"])
]

app = Starlette(routes=routes)