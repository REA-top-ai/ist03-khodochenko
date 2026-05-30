"""One-off loader that fills the `cocktails` reference table from TheCocktailDB API.

Usage (from project root):
    python -m scripts.seed_cocktails
"""
import asyncio
import logging
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db import AsyncSessionLocal
from app.repositories.cocktail import CocktailRepository
from app.services import cache

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger("seed_cocktails")


async def main() -> None:
    cocktails = await cache.get_all()
    items = [(c.id, c.name) for c in cocktails if c.id and c.name]
    logger.info("Fetched %d cocktails from API", len(items))

    async with AsyncSessionLocal() as session:
        repo = CocktailRepository(session)
        written = await repo.upsert_many(items)
        total = await repo.count()

    logger.info("Upserted %d rows; table now holds %d cocktails", written, total)


if __name__ == "__main__":
    asyncio.run(main())
