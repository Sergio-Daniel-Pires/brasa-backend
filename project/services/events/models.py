from dataclasses_json import dataclass_json
import dataclasses as dc

@dataclass_json
@dc.dataclass
class SportEvent:
    sport_name: str = dc.field(default=None)
    title: str = dc.field(default=None)
    start_date: int = dc.field(default=None)
    end_date: int = dc.field(default=None)
    mtime: int = dc.field(default=None)
    ctime: int = dc.field(default=None)
