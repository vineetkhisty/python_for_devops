from fastapi import FastAPI # Importing fastapi class
from router import routes

app = FastAPI(
    title="Internal Devops Utilities API",
    description="This is used for Monitoring metrics, aws usage",
    version="1.0.0",
    doc_url="/docs",
    redoc_url = "/reload"
)

@app.get("/")
def hello():
    return {"message":"Hello Dosto"}

app.include_router(routes.router)