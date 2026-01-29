
from typing import Optional

from fastapi import APIRouter, HTTPException
from starlette import status

from model.poll_question import PollQuestion
from service import poll_service

router = APIRouter(
    prefix="/poll",
    tags=["poll"]
)

@router.get("/question/{question_id}", response_model=PollQuestion)
async def get_question_by_id(question_id: int) -> Optional[PollQuestion]:
    poll_question = await poll_service.get_question_by_id(question_id)
    if not poll_question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Question with question id {question_id} not found")
    return poll_question