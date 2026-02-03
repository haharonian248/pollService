from pydantic import BaseModel


class QuestionUserCountResponse(BaseModel):
    q_id: int
    q_text: str
    user_count: int