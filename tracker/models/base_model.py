from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseModel:
    created_when: datetime
    modified_when: datetime

    def __post_init__(self):
        self.created_when = datetime.utcnow()
        self.modified_when = datetime.utcnow()