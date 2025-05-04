from datetime import datetime
from typing import Optional


class ReviewCycle:
    def __init__(
        self,
        id: int,
        name: str,
        start_date: datetime,
        end_date: datetime,
        status: str,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def update_status(self, new_status: str):
        self.status = new_status
        self.updated_at = datetime.utcnow()
