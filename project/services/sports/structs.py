from dataclasses_json import dataclass_json
import dataclasses as dc
from models import SportScrapper
import time
from typing import Literal

@dataclass_json
@dc.dataclass
class CreateSportScrapper:
    name: str = dc.field()
    link: str = dc.field()
    state: Literal["TO_SCRAP", "FINISHED"] = dc.field()
    last_scrap: int = dc.field()

    def to_insert (self):
        return SportScrapper.from_dict(
            **self.__dict__,
            ctime = int(time.time() * 1000),
            mtime = int(time.time() * 1000)
        )
