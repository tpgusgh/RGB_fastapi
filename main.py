from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
)

current = "R"  # 초기 신호

@app.get("/signal")
def get_or_set_signal(set: str | None = Query(default=None, regex="^[RGB]$")):
    global current
    if set is not None:
        current = set
    return {"signal": current}
