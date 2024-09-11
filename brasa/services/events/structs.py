import dataclasses as dc
import time

from dataclasses_json import dataclass_json

from .models import SportEvent


@dataclass_json
@dc.dataclass
class CreateSportEvent:
    sport_name: int = dc.field()
    title: str = dc.field()
    extra_info = dc.field()
    start_date: int | str = dc.field()
    end_date: int | str = dc.field()
    extra_info: str = dc.field(default="")
    streamings: list[str] = dc.field(default_factory=list)

    def to_insert (self) -> SportEvent:
        return SportEvent.from_dict({
            **self.__dict__,
            "ctime": int(time.time() * 1000),
            "mtime": int(time.time() * 1000)
        })
