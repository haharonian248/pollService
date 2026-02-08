from typing import Optional, List

from model.question_answer_user_count_response import QuestionAnswerUserCountResponse
from model.question_user_count_response import QuestionUserCountResponse
from model.user_answer_request import UserAnswerRequest
from model.user_answer_response import UserAnswerResponse
from repository import question_answer_repository


async def get_user_count_per_answer_by_question_id(question_id: int) -> Optional[List[QuestionAnswerUserCountResponse]]:
    return await question_answer_repository.number_of_users_per_answer_per_question(question_id)

async def get_user_count_by_question_id(question_id: int) -> Optional[QuestionUserCountResponse]:
    return await question_answer_repository.numbers_of_users_answered_by_question_id(question_id)

async def get_user_answers_by_user_id(user_id: int) -> Optional[List[UserAnswerResponse]]:
    return await question_answer_repository.answers_by_user_id(user_id)

async def get_count_answers_by_user_id(user_id: int) -> Optional[int]:
    return await question_answer_repository.number_of_questions_answered_by_user_id(user_id)

async def get_total_users_answered_each_option() -> Optional[List[QuestionAnswerUserCountResponse]]:
    return await question_answer_repository.total_users_answered_each_option()

async def delete_user_answers_by_user_id(user_id: int):
    return await question_answer_repository.delete_user_answers(user_id)

async def insert_user_answer(user_answer_request: UserAnswerRequest):
    await question_answer_repository.insert_user_answer(user_answer_request)

async def update_user_answer(user_answer_request: UserAnswerRequest):
    # If the question and answer already exists then no need to update:
    user_answer_responses = await get_user_answers_by_user_id(user_answer_request.user_id)
    if any(user_answer_response.q_id == user_answer_request.q_id for user_answer_response in user_answer_responses):
        return None
    else:
        return await question_answer_repository.update_user_answer(user_answer_request)