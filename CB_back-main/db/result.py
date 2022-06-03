from db.users import get_user_by_id

async def setup_list(user_id):
    user = await get_user_by_id(user_id)
    
