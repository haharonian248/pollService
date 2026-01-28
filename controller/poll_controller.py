from typing import Optional

from fastapi import APIRouter

from model.poll_question import PollQuestion

router = APIRouter(
    prefix="/poll",
    tags=["poll"]
)

@router.get("/question/{question_id}", response_model=PollQuestion)
async def get_user_by_id(question_id: int) -> Optional[PollQuestion]:

    return PollQuestion