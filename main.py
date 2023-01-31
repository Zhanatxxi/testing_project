import uvicorn

from fastapi import FastAPI




from collections_core.apps.service.views import api


app = FastAPI(
    title="Testing project",
    description="""this is project for testing compnay""",
    version="0.1.0"
)

app.include_router(
    api.router
)


def main():
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True, workers=2)

if __name__ == "__main__":
   main()



