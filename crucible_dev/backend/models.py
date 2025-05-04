from pydantic import BaseModel

class User(BaseModel):
    id: str
    xp: int = 0
    level: int = 1
    streak_days: int = 0