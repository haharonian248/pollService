from pydantic import BaseModel, Field


class Answer(BaseModel):
    a_id: int
    a_text: str = Field(alias="answer")