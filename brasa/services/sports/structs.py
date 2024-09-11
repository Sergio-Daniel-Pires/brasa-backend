import dataclasses as dc
import time
from typing import Literal

from dataclasses_json import dataclass_json

from .models import SportScrapper


@dataclass_json
@dc.dataclass
class CreateSportScrapper:
    name: str = dc.field()
    state: Literal["TO_SCRAP", "FINISHED", "ERROR"] = dc.field()
    last_scrap: int = dc.field(default=0)

    def to_insert (self):
        return SportScrapper.from_dict({
            **self.__dict__,
            "ctime":int(time.time() * 1000),
            "mtime":int(time.time() * 1000)
        })
