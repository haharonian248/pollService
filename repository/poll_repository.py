from typing import Optional

from model.poll_question import QuestionAnswer
from repository.database import database


async def get_question_by_id(question_id: int) -> Optional[QuestionAnswer]:
    query = """
        SELECT q.q_id, q.q_text, a.a_id, a.a_text 
        FROM question q
        JOIN answer_to_question a
        WHERE q.q_id = a.q_id
        AND q.q_id=:question_id
    """
    return await database.fetch_one(query, values={"question_id": question_id})