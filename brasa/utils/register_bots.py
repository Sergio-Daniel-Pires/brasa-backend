import asyncio
import logging
import traceback
from collections.abc import Callable

from brasa.scrapers.volei import main as volei
from brasa.services.events.structs import CreateSportEvent
from brasa.services.sports.structs import CreateSportScrapper
from brasa.utils import find_collection


async def register_bot_and_events(sport_name: str, bot_func: Callable) -> bool:
    sports_conn = find_collection("sports")
    events_conn = find_collection("sports_events")
    
    new_sport = CreateSportScrapper(sport_name, "TO_SCRAP")

    sports_conn.find_one_and_update(
        { "name": sport_name }, { "$setOnInsert": new_sport.to_insert().to_dict() }, upsert=True
    )

    try:
        results = await bot_func()
        for result in results:
            new_sport_event = CreateSportEvent(sport_name, **result).to_insert()

            events_conn.find_one_and_update(
                { "name": sport_name, "title": new_sport_event.title },
                { "$setOnInsert": new_sport_event.to_dict() }
            )

        sports_conn.update_one(
            {"name": sport_name}, {"$set": {"status": "FINISHED"}}
        )

    except:
        logging.error(traceback.format_exc())
        sports_conn.update_one(
            {"name": sport_name},
            {"$set": {"status": "FAILED"}}
        )

async def main():
    logging.info("Registering bots")

    for bot_name, bot_func in (
        ( "volei", volei ),
    ):
        try:
            await register_bot_and_events(bot_name, bot_func)
        
        except:
            logging.error(f"Failed to register bot {bot_name}")
            logging.error(traceback.format_exc())

    logging.info("Finished to register bot")

if __name__ == "__main__":
    asyncio.run(main())
