import asyncio
import json
from typing import Type, get_type_hints
from dotenv import load_dotenv
import os
from async_igdb import IGDBClient
from async_igdb.util import CharacterSpeciesEnum

load_dotenv()


async def main():
    client_id = os.getenv("IGDB_ID")
    client_secret = os.getenv("IGDB_SECRET")

    async with IGDBClient(client_id, client_secret=client_secret) as client:
        result = await client.games.find_one(ids=[60226])
        with open("test.json", "w") as f:
            f.write((await result.resolve_links(depth=5)).model_dump_json(indent=4))


asyncio.run(main())
