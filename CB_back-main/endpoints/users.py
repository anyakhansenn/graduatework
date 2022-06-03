from fastapi import HTTPException, status

from db.users import create_user, check_user



async def create_new_user(login: str) -> None:
    is_usable = await check_user(login)
    if is_usable:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='login already in use'
        )
    await create_user(login)
    user_info = await check_user(login)
    return user_info

async def authentificate_user(login: str) -> str:
    user_info = await check_user(login)
    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='user not exists'
        )
    return user_info