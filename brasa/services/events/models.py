import dataclasses as dc
import datetime as dt

from dataclasses_json import dataclass_json


@dataclass_json
@dc.dataclass
class SportEvent:
    sport_name: str = dc.field(default=None)
    title: str = dc.field(default=None)
    extra_info: str = dc.field(default=None)
    start_date: int = dc.field(default=None)
    end_date: int = dc.field(default=None)
    mtime: int = dc.field(default=None)
    ctime: int = dc.field(default=None)

    def to_human (self):
        return {
            "sport_name": self.sport_name,
            "title": self.title,
            "extra_info": self.extra_info,
            "start_date": dt.datetime.fromtimestamp(self.start_date // 1000).strftime("%m-%d %H:%M"),
            "end_date": dt.datetime.fromtimestamp(self.end_date // 1000).strftime("%m-%d %H:%M"),
        }
