from sqlalchemy import select
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.cocktail import CocktailRecord


class CocktailRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list_all(self) -> list[CocktailRecord]:
        result = await self.session.execute(
            select(CocktailRecord).order_by(CocktailRecord.cocktail_name)
        )
        return list(result.scalars().all())

    async def count(self) -> int:
        result = await self.session.execute(select(CocktailRecord.cocktail_id))
        return len(result.scalars().all())

    async def upsert_many(self, items: list[tuple[str, str]]) -> int:
        if not items:
            return 0
        rows = [
            {"cocktail_id": cocktail_id, "cocktail_name": cocktail_name}
            for cocktail_id, cocktail_name in items
        ]
        stmt = insert(CocktailRecord).values(rows)
        stmt = stmt.on_conflict_do_update(
            index_elements=[CocktailRecord.cocktail_id],
            set_={"cocktail_name": stmt.excluded.cocktail_name},
        )
        await self.session.execute(stmt)
        await self.session.commit()
        return len(rows)
