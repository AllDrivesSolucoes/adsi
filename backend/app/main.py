from fastapi import FastAPI

app = FastAPI(
    title="ADSI API",
    description="All Drives Sales Intelligence Platform",
    version="0.1.0",
)


@app.get("/")
def home() -> dict[str, str]:
    return {
        "status": "online",
        "sistema": "ADSI",
        "versao": "0.1.0",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}