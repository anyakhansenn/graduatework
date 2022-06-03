from firebase_admin import db

def message_get(mid: str, user: str):
    ref = db.reference(f"/phrases/{mid}")
    phrases = ref.get()
    #print(phrases)
    bot_messages = None
    awaited_messages = None
    response_destination = dict()
    for key, value in phrases.items():
        if key == 'data':
            bot_messages = value
        elif key == 'await':
            awaited_messages = value
        else:
            response_destination[key] = value

    bm_res = list()
    resp_res = list()

    for msg in bot_messages:
        buf = msg.replace('{user}', user)
        bm_res.append({
            'sender':'bot',
            'message':buf
        })

    for (i, msg) in enumerate(awaited_messages):
        resp_res.append({
            'variant':msg,
            'direction': response_destination[str(i)]
        })

    print(bm_res, resp_res)

    return {
        'messages':bm_res,
        'variants':resp_res
    }
