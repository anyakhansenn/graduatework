from db.users import get_user_by_id
from db.chat import create_new_message_history, update_message_history, write_sensor_value
from db.message_get import message_get

from machine.call_machine import get_prediction

from endpoints.classes import VariantMessage, UserMessage

async def init_chat(user_id: str) -> None:
    user_info = await get_user_by_id(user_id)
    if user_info.get('chat') is None:
        #STARTING CHAT WITH NEW USER
        #QUERY first_messages
        first_messages = message_get('start', user_info['name'])
        await create_new_message_history(first_messages['messages'], user_id, first_messages['variants'])
        return first_messages
    messages = {
        'messages':user_info['chat'],
        'variants':user_info['last_variants']
    }
    
    return messages

async def upd_conversation(message:UserMessage):
    #GET RESPONSE FROM BOT WITH USER_MESSAGE
    user_info = await get_user_by_id(message.id)
    if len(message.variants) == 1 and message.variants[0].variant[0] == '#':
        variant = message.variants[0]
        print('sensor')
        bot_response = message_get(variant.direction, user_info['name'])
        update = user_info['chat'] + ([{'sender':'user', 'message': message.message}]) + (bot_response['messages'])
        await write_sensor_value(variant.variant, message.message, message.id)
        await update_message_history(update, message.id, bot_response['variants'])
        return {
            'messages': update,
            'variants': bot_response['variants']
        }
    elif len(message.variants) == 1 and message.variants[0].variant[0] == '%':
        pass
        #setup_list()
        #get_prediction()


    #bot_response = 'bot_response'
    
   
    #await update_message_history(update, user_id)
    #chat_now = await get_user_by_id(user_id)
    #return chat_now['chat']

async def upd_conversation_variant(message: VariantMessage):
    user_info = await get_user_by_id(message.id)
    if message.variant.find('#')!=-1:
        variant, sensor = message.variant.split('#')
        print(variant, sensor)
        await write_sensor_value(sensor, 1, message.id)
    else:
        variant = message.variant
    bot_response = message_get(variant, user_info['name'])
    update = user_info['chat'] + ([{'sender':'user', 'message': message.message}]) + (bot_response['messages'])
    print(update)
    await update_message_history(update, message.id, bot_response['variants'])
    return {
        'messages': update,
        'variants': bot_response['variants']
    }
