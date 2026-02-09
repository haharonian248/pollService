from typing import Optional, List

from fastapi import APIRouter, HTTPException
from starlette import status

from model.question_answer_user_count_response import QuestionAnswerUserCountResponse
from model.question_user_count_response import QuestionUserCountResponse
from model.user_answer_request import UserAnswerRequest
from model.user_answer_response import UserAnswerResponse
from service import question_answer_service

router = APIRouter(
    prefix="/question",
    tags=["question"]
)

@router.get("/userCountPerAnswer/{question_id}", response_model=List[QuestionAnswerUserCountResponse])
async def get_user_count_per_answer_by_question_id(question_id: int) -> Optional[List[QuestionAnswerUserCountResponse]]:
    results = await question_answer_service.get_user_count_per_answer_by_question_id(question_id)
    if results:
        return results
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Question with question id {question_id} hasn't been answered by any user")

@router.get("/userCountPerQuestion/{question_id}", response_model=QuestionUserCountResponse)
async def get_user_count_by_question_id(question_id: int) -> Optional[QuestionUserCountResponse]:
    result = await question_answer_service.get_user_count_by_question_id(question_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Question with question id {question_id} hasn't been answered by any user")

@router.get("/getUserAnswers/{user_id}", response_model=List[UserAnswerResponse])
async def get_user_answers_by_user_id(user_id: int) -> Optional[List[UserAnswerResponse]]:
    results = await question_answer_service.get_user_answers_by_user_id(user_id)
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with user id {user_id} not found")
    else:
        return results

@router.get("/numberOfAnsweredQuestions/{user_id}", response_model=int)
async def get_count_answers_by_user_id(user_id: int) -> int:
    result = await question_answer_service.get_count_answers_by_user_id(user_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with user id {user_id} not found")

@router.get("/totalCountUsersAnsweredEachOption", response_model= List[QuestionAnswerUserCountResponse])
async def get_total_users_answered_each_option() -> List[QuestionAnswerUserCountResponse]:
    results = await question_answer_service.get_total_users_answered_each_option()
    if results:
        return results
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@router.delete("/deleteUserAnswers/{user_id}", response_model=dict)
async def delete_user_answers_by_user_id(user_id: int):
    await question_answer_service.delete_user_answers_by_user_id(user_id)
    return {"message": "User answers deleted successfully"}

@router.post("/insertUserAnswer")
async def insert_user_answer(user_answer_request: UserAnswerRequest):
    await question_answer_service.insert_user_answer(user_answer_request)
    return {"message": "User answer created successfully"}

@router.post("/updateUserAnswer")
async def update_user_answer(user_answer_request: UserAnswerRequest):
    result = await question_answer_service.update_user_answer(user_answer_request)
    if result == 0:
        return {"message": "User has already put this answer for this question"}
    if result == 1:
        return {"message": "User has already answered this question, but now updated"}
    return {"message": "User answer updated successfully"}