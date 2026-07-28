from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class EmpresaBase(BaseModel):
    razao_social: str = Field(min_length=2, max_length=200)
    nome_fantasia: str | None = Field(default=None, max_length=200)
    cnpj: str = Field(min_length=14, max_length=14)
    cidade: str = Field(min_length=2, max_length=100)
    estado: str = Field(min_length=2, max_length=2)
    segmento: str | None = Field(default=None, max_length=100)
    site: str | None = Field(default=None, max_length=255)
    telefone: str | None = Field(default=None, max_length=30)
    score_adsi: int = Field(default=0, ge=0, le=100)
    status: str = Field(default="prospecção", max_length=50)
    observacoes: str | None = None


class EmpresaCriar(EmpresaBase):
    pass


class EmpresaAtualizar(BaseModel):
    razao_social: str | None = Field(default=None, min_length=2, max_length=200)
    nome_fantasia: str | None = Field(default=None, max_length=200)
    cidade: str | None = Field(default=None, min_length=2, max_length=100)
    estado: str | None = Field(default=None, min_length=2, max_length=2)
    segmento: str | None = Field(default=None, max_length=100)
    site: str | None = Field(default=None, max_length=255)
    telefone: str | None = Field(default=None, max_length=30)
    score_adsi: int | None = Field(default=None, ge=0, le=100)
    status: str | None = Field(default=None, max_length=50)
    observacoes: str | None = None


class EmpresaResposta(EmpresaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    criado_em: datetime
    atualizado_em: datetime