from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.models.empresa import Empresa
from backend.app.schemas.empresa import EmpresaAtualizar, EmpresaCriar


def criar_empresa(db: Session, dados: EmpresaCriar) -> Empresa:
    empresa = Empresa(**dados.model_dump())

    db.add(empresa)
    db.commit()
    db.refresh(empresa)

    return empresa


def listar_empresas(db: Session) -> list[Empresa]:
    consulta = select(Empresa).order_by(Empresa.razao_social)
    return list(db.scalars(consulta).all())


def buscar_empresa(db: Session, empresa_id: int) -> Empresa | None:
    return db.get(Empresa, empresa_id)


def atualizar_empresa(
    db: Session,
    empresa: Empresa,
    dados: EmpresaAtualizar,
) -> Empresa:
    campos = dados.model_dump(exclude_unset=True)

    for campo, valor in campos.items():
        setattr(empresa, campo, valor)

    db.commit()
    db.refresh(empresa)

    return empresa


def excluir_empresa(db: Session, empresa: Empresa) -> None:
    db.delete(empresa)
    db.commit()