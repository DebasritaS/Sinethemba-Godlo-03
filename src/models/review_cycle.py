from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class ReviewCycle:
    def __init__(self, name: str, start_date: datetime, end_date: datetime, status: str = "Active"):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.tasks: List = []

    def add_task(self, task):
        self.tasks.append(task)


class ReviewCycleCreateRequest(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime
    description: Optional[str] = None

class ReviewCycleResponse(BaseModel):
    id: int
    name: str
    start_date: datetime
    end_date: datetime
    description: Optional[str] = None
