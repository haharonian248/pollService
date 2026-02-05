from typing import List, Optional

from model.question_answer_user_count_response import QuestionAnswerUserCountResponse
from model.question_user_count_response import QuestionUserCountResponse
from model.user_answer_request import UserAnswerRequest
from model.user_answer_response import UserAnswerResponse
from repository.database import database


async def number_of_users_per_answer_per_question(q_id: int) -> Optional[List[QuestionAnswerUserCountResponse]]:
    query = """
        SELECT q.q_id, q.q_text, a.a_id, a.a_text, COUNT(uqa.user_id) AS user_count
        FROM user_question_answer AS uqa
        JOIN question AS q 
        ON uqa.q_id = q.q_id
        JOIN answer_to_question AS a 
        ON uqa.a_id = a.a_id
        AND uqa.q_id=:q_id
        GROUP BY q.q_id, q.q_text, a.a_id, a.a_text
        ORDER BY q.q_id, a.a_id;
    """
    rows = await database.fetch_all(query, values={"q_id": q_id})

    if rows:
        return [QuestionAnswerUserCountResponse(**row) for row in rows]
    else:
        return None


async def numbers_of_users_answered_by_question_id(q_id: int) -> Optional[QuestionUserCountResponse]:
    query = """
        SELECT q.q_id, q.q_text, COUNT(uqa.user_id) AS user_count
        FROM user_question_answer AS uqa
        JOIN question AS q 
        ON uqa.q_id = q.q_id
        AND uqa.q_id=:q_id
        GROUP BY q.q_id, q.q_text
        ORDER BY q.q_id;
    """

    result = await database.fetch_one(query, values={"q_id": q_id})

    if result:
        return QuestionUserCountResponse(**result)
    else:
        return None

async def answers_by_user_id(user_id: int) -> Optional[List[UserAnswerResponse]]:
    query = """
        select uqa.user_id, q.q_id, q.q_text, uqa.a_id, aq.a_text
        from user_question_answer as uqa
        join question as q on q.q_id = uqa.q_id
        join answer_to_question as aq on aq.a_id=uqa.a_id
        where user_id=:user_id
    """

    results = await database.fetch_all(query, values={"user_id": user_id})
    return [UserAnswerResponse(**result) for result in results]

async def number_of_questions_answered_by_user_id(user_id: int) -> int:
    query= """
        SELECT COUNT(*) AS answered_count
        FROM user_question_answer
        WHERE user_id=:user_id;
    """
    result = await database.fetch_one(query, values={"user_id": user_id})
    return int(result["answered_count"])

async def total_users_answered_each_option() -> Optional[List[QuestionAnswerUserCountResponse]]:
    query = """
        SELECT q.q_id, q.q_text, a.a_id, a.a_text, COUNT(uqa.a_id) AS user_count
        FROM question q
        JOIN answer_to_question a ON a.q_id = q.q_id
        LEFT JOIN user_question_answer uqa ON uqa.a_id = a.a_id
        GROUP BY q.q_id, q.q_text, a.a_id, a.a_text
        ORDER BY q.q_id, a.a_id;
    """

    results = await database.fetch_all(query)
    return [QuestionAnswerUserCountResponse(**result) for result in results]

async def delete_user_answers(user_id: int):
    query = "DELETE FROM user_question_answer WHERE user_id =:user_id"
    return await database.execute(query, values={"user_id": user_id})

async def insert_user_answer(user_answers_request: UserAnswerRequest):
    query = """
        INSERT INTO user_question_answer (user_id, q_id, a_id) 
        VALUES (:user_id, :q_id, :a_id);
    """
    values={"user_id": user_answers_request.user_id,
            "q_id":user_answers_request.q_id,
            "a_id":user_answers_request.a_id
    }
    await database.execute(query, values=values)

async def update_user_answer(user_answers_request: UserAnswerRequest):
    query = """
        UPDATE user_question_answer
        SET a_id=:a_id
        WHERE user_id=:user_id
        and q_id=:q_id
    """
    values={
        "user_id": user_answers_request.user_id,
        "q_id": user_answers_request.q_id,
        "a_id": user_answers_request.a_id
    }
    await database.execute(query, values=values)