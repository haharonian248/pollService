from typing import Optional

from model.poll_question import QuestionAnswer
from repository import poll_repository


async def get_question_by_id(question_id: int) -> Optional[QuestionAnswer]:
    return await poll_repository.get_question_by_id(question_id)