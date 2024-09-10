from dataclasses_json import dataclass_json
import dataclasses as dc
from typing import Literal

@dataclass_json
@dc.dataclass
class SportScrapper:
    name: str = dc.field(default=None)
    link: str = dc.field(default=None)
    state: Literal["TO_SCRAP", "FINISHED"] = dc.field(default=None)
    last_scrap: int = dc.field(default=None)
    mtime: int = dc.field(default=None)
    ctime: int = dc.field(default=None)
