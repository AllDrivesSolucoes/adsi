from fastapi import FastAPI

from backend.app.api.empresas import router as empresas_router


app = FastAPI(
    title="ADSI API",
    description="All Drives Sales Intelligence Platform",
    version="0.2.0",
)

app.include_router(empresas_router)


@app.get("/")
def home() -> dict[str, str]:
    return {
        "status": "online",
        "sistema": "ADSI",
        "versao": "0.2.0",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}