from pydantic import BaseModel
from typing import Optional, List

class Message(BaseModel):
    msg: str

class Course(BaseModel):
    title: str
    teacher: str
    students: Optional[List[str]] = None
    level: str