"""Router for learner endpoints."""

from datetime import datetime

from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.learners import create_learner, read_learners
from app.models.learner import Learner, LearnerCreate

router = APIRouter()


@router.get("/learners", response_model=list[Learner])
async def get_learners(
    enrolled_after: datetime | None = None,
    session: AsyncSession = Depends(get_session),
):
    """Get all learners, optionally filtered by enrollment date."""
    return await read_learners(session, enrolled_after)


@router.post("/learners", response_model=Learner, status_code=201)
async def create_new_learner(
    learner: LearnerCreate,
    session: AsyncSession = Depends(get_session),
):
    """Create a new learner."""
    return await create_learner(session, name=learner.name, email=learner.email)
