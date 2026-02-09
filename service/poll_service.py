from typing import Optional

from model.answer import Answer
from model.poll_question import QuestionAnswer
from repository import poll_repository


async def get_question_by_id(question_id: int) -> Optional[QuestionAnswer]:
    rows = await poll_repository.get_question_by_id(question_id)
    if not rows:
        return None
    q_id = rows[0]["q_id"]
    q_text = rows[0]["q_text"]
    answers = [
        Answer(a_id=row["a_id"], answer=row["a_text"])
        for row in rows
    ]
    return QuestionAnswer(
        q_id=q_id,
        q_text=q_text,
        answers=answers
    )

