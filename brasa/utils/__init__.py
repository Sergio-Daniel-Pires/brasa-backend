from typing import cast

import pymongo
import pymongo.collection

from brasa import config


def find_collection(collection: str) -> pymongo.collection.Collection:
    client = pymongo.MongoClient(config.MONGO_CONN)
    coll = client[config.MONGO_DATABASE][collection]

    coll = cast(pymongo.collection.Collection, coll)

    return coll
