from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.database.connection import get_db
from backend.app.schemas.empresa import (
    EmpresaAtualizar,
    EmpresaCriar,
    EmpresaResposta,
)
from backend.app.services.empresa_service import (
    atualizar_empresa,
    buscar_empresa,
    criar_empresa,
    excluir_empresa,
    listar_empresas,
)

router = APIRouter(
    prefix="/empresas",
    tags=["Empresas"],
)


@router.post(
    "",
    response_model=EmpresaResposta,
    status_code=status.HTTP_201_CREATED,
)
def cadastrar_empresa(
    dados: EmpresaCriar,
    db: Session = Depends(get_db),
):
    try:
        return criar_empresa(db, dados)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe uma empresa cadastrada com este CNPJ.",
        )


@router.get("", response_model=list[EmpresaResposta])
def consultar_empresas(
    db: Session = Depends(get_db),
):
    return listar_empresas(db)


@router.get("/{empresa_id}", response_model=EmpresaResposta)
def consultar_empresa(
    empresa_id: int,
    db: Session = Depends(get_db),
):
    empresa = buscar_empresa(db, empresa_id)

    if empresa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empresa não localizada.",
        )

    return empresa


@router.patch("/{empresa_id}", response_model=EmpresaResposta)
def editar_empresa(
    empresa_id: int,
    dados: EmpresaAtualizar,
    db: Session = Depends(get_db),
):
    empresa = buscar_empresa(db, empresa_id)

    if empresa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empresa não localizada.",
        )

    return atualizar_empresa(db, empresa, dados)


@router.delete(
    "/{empresa_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def remover_empresa(
    empresa_id: int,
    db: Session = Depends(get_db),
):
    empresa = buscar_empresa(db, empresa_id)

    if empresa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empresa não localizada.",
        )

    excluir_empresa(db, empresa)

    return Response(status_code=status.HTTP_204_NO_CONTENT)