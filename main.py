from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get("/test")
def test():
    return "hello"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", prot=8000, reload=True)