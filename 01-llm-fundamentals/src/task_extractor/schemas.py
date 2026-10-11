
from typing import Literal

from pydantic import BaseModel, Field


class Task(BaseModel):
    description: str = Field(min_length=1)
    owner: str | None = None
    deadline: str | None = None
    priority: Literal["low", "medium", "high"] = "medium"


class TaskExtraction(BaseModel):
    tasks: list[Task]
