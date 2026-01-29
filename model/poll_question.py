

from pydantic import BaseModel, Field


class PollQuestion(BaseModel):
    q_id: int
    q_text: str