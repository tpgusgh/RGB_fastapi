from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

current_color = {"red": 0, "green": 0, "blue": 0}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/color")
def get_color(red: int = None, green: int = None, blue: int = None):
    global current_color
    if red is not None:
        current_color["red"] = red
    if green is not None:
        current_color["green"] = green
    if blue is not None:
        current_color["blue"] = blue
    return current_color
