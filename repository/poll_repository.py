from typing import Optional

from model.poll_question import PollQuestion
from repository.database import database


async def get_question_by_id(question_id: int) -> Optional[PollQuestion]:
    query = "SELECT * FROM question WHERE q_id=:question_id"
    return await database.fetch_one(query, values={"question_id": question_id})

