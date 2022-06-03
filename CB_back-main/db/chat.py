
from firebase_admin import db

async def create_new_message_history(first_data: list, user_id: str, variants: list):
    ref = db.reference('/users')
    ref.child(user_id).update({'chat':first_data})
    ref.child(user_id).update({'last_variants':variants})

async def update_message_history(update: list, user_id: str, variants: list):
    ref = db.reference('/users')
    ref.child(user_id).update({'chat': update})
    ref.child(user_id).update({'last_variants':variants})

async def write_sensor_value(sensor_name: str, value: int, user_id: str):
    ref = db.reference('/users')
    name = sensor_name.replace('#','')
    ref.child(user_id).update({f'{name}': value})


    