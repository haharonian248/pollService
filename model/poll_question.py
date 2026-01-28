from typing import List

from pydantic import BaseModel, Field

from model.answer import Answer


class PollQuestion(BaseModel):
    q_id: int
    q_text: str = Field(alias="question")
    answers: List[Answer]