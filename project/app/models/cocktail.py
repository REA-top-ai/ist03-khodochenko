from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class CocktailRecord(Base):
    __tablename__ = "cocktails"

    cocktail_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    cocktail_name: Mapped[str] = mapped_column(String(255), nullable=False)
