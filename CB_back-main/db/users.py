from firebase_admin import db

async def check_user(login: str) -> bool:
    ref = db.reference("/users")
    users = ref.get()
    print(users)
    for key, value in users.items():
        if(value["name"] == login):
            value['id'] = key
            return value
    return False

async def get_user_by_id(id: str):
    ref = db.reference('/users')
    users = ref.get()
    for key, value in users.items():
        if key == id:
            return value

async def create_user(login: str) -> None:
    ref = db.reference('/users')
    ref.push().set({
        'name': login
    })