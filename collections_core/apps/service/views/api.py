from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks

from sqlalchemy.ext.asyncio import AsyncSession

from collections_core.apps.db.deps import get_db_session
from collections_core.apps.service.schemas import (
    MessageSchema, DispatchShema, MessageSchema,
    DispatchCreateSchema, DispatchOutSchema)
from collections_core.apps.service import selectors
from collections_core.apps.service import services
from collections_core.apps.clients.selectors import get_user_by_id
from collections_core.apps.service.selectors import get_dispatch_by_id
from collections_core.apps.service.tasks import test_task


router = APIRouter(prefix="/dispatch", tags=["Dispatch"])


@router.get("/all_dispathers", response_model=list[DispatchShema])
async def dispatchers(db: AsyncSession = Depends(get_db_session)):

    result = await selectors.get_all_dispatchers(db)

    return [DispatchShema(**dispatch) for dispatch in result]


@router.get("/all_messages", response_model=list[MessageSchema])
async def all_messages(db: AsyncSession = Depends(get_db_session)):
    
    result = await selectors.get_all_messages(db)

    return [MessageSchema(**message) for message in result]


@router.post("/create/message")
async def create_message(
    message: MessageSchema,
    db: AsyncSession = Depends(get_db_session)
    ):

    dispatch = await get_dispatch_by_id(db, dispatch_id=message.dispatch_id)
    user = await get_user_by_id(db, user_id=message.user_id)

    if (dispatch and user) is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="not found dispatch_id or user_id"
        )

    message.user_id, message.dispatch_id = user, dispatch

    isinstance_mes = await services.create_message(
        db=db,
        message=message
    )

    return isinstance_mes


@router.post("/create") # response_model=DispatchOutSchema
async def create_dispatcher(
    dispatch: DispatchCreateSchema,
    background_task: BackgroundTasks,
    db: AsyncSession = Depends(get_db_session),
    ):

    if await selectors.get_message_by_id(db, message_id=dispatch.message_id) is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="not found message id"
        )

    dispatcher = await services.create_dispatcher(db, dispatch)

    background_task.add_task(test_task, dispatch.message_id, dispatcher.message, db)


    return dispatcher


