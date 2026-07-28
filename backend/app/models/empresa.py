from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.connection import Base


class Empresa(Base):
    __tablename__ = "empresas"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    razao_social: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    nome_fantasia: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    cnpj: Mapped[str] = mapped_column(
        String(14),
        unique=True,
        index=True,
        nullable=False,
    )

    cidade: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    estado: Mapped[str] = mapped_column(
        String(2),
        nullable=False,
    )

    segmento: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    site: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    telefone: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    score_adsi: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="prospecção",
        nullable=False,
    )

    observacoes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    criado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )