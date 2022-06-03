import firebase_admin
import uvicorn

from firebase_admin import credentials

from endpoints.classes import NewUser, AuthUser, UserMessage, VariantMessage
from endpoints.users import create_new_user, authentificate_user
from endpoints.chat import init_chat, upd_conversation, upd_conversation_variant


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app =FastAPI()

origins = ["*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
async def setup_db():
    cred = credentials.Certificate("secret/database_secret.json")
    firebase_admin.initialize_app(cred, 
        {'databaseURL':'https://chatbotdb-4342c-default-rtdb.europe-west1.firebasedatabase.app/'})

@app.get('/page')
async def return_page():
    return 'ok'

@app.post('/new_user')
async def new_user(user: NewUser):
    return await create_new_user(user.login)

@app.post('/login')
async def authentificate(user: NewUser):
    return await authentificate_user(user.login)

@app.post('/start_chat')
async def initialize_chat(user: AuthUser):
    return await init_chat(user.id)

@app.post('/user_message')
async def update_conversation(message: UserMessage):
    print(message)
    return await upd_conversation(message)

@app.post('/user_variant')
async def get_user_variant(message: VariantMessage):
    return await upd_conversation_variant(message)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=5000, reload=True)