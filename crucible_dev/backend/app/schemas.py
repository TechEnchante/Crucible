from pydantic import BaseModel
from typing  import Literal

#Shared fields for a commit
class CommitBase(BaseModel):
    user_id:   str
    message:   str
    timestamp: float

#Payload sent by the client when creating a commit
class CommitCreate(CommitBase):
    pass

#What we return after successfully storing a commit
class Commit(CommitBase):
    point_id: str
    status:   Literal["ok"]

    class Config:
        orm_mode = True