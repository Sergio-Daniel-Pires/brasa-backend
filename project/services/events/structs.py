from dataclasses_json import dataclass_json
import dataclasses as dc
from models import SportEvent
import time

@dataclass_json
@dc.dataclass
class CreateSportEvent:
    sport_name: int = dc.field()
    start_date: int = dc.field()
    end_date: int = dc.field()

    def to_insert (self):
        return SportEvent.from_dict(
            **self.__dict__,
            ctime = int(time.time() * 1000),
            mtime = int(time.time() * 1000)
        )
