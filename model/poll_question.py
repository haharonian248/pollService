from typing import List

from pydantic import BaseModel

from model.answer import Answer


class QuestionAnswer(BaseModel):
    q_id: int
    q_text: str
    answers: List[Answer]
