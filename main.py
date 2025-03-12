from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

api = FastAPI(
    title="Hello Fast API",
    description="My own API powered by FastAPI.",
    version="1.0.1")

class User(BaseModel):
    userid: Optional[int]
    name: str
    subscription: str

class Computer(BaseModel):
    """a computer that is available in the store
    """
    computerid: int
    cpu: Optional[str]
    gpu: Optional[str]
    price: float

class Owner(BaseModel):
    name: str
    address: str

class Item(BaseModel):
    itemid: int
    description: str
    owner: Optional[Owner] = None
    ratings: List[float]
    available: bool

users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]

@api.get('/', name="Hello world " )
def get_index():
    """Returns greetings
    """
    return {'greetings': 'welcome'}

@api.put('/users')
def put_users(user: User):
    new_id = max(users_db, key=lambda u: u.get('user_id'))['user_id']
    new_user = {
        'user_id': new_id + 1,
        'name': user.name,
        'subscription': user.subscription
    }
    users_db.append(new_user)
    return new_user

@api.post('/users/{userid:int}')
def post_users(user: User, userid):
    try:
        old_user = list(
            filter(lambda x: x.get('user_id') == userid, users_db)
            )[0]

        users_db.remove(old_user)

        old_user['name'] = user.name
        old_user['subscription'] = user.subscription

        users_db.append(old_user)
        return old_user

    except IndexError:
        return {}

@api.delete('/users/{userid:int}')
def delete_users(userid):
    try:
        old_user = list(
            filter(lambda x: x.get('user_id') == userid, users_db)
            )[0]

        users_db.remove(old_user)
        return {
            'userid': userid,
            'deleted': True
            }
    except IndexError:
        return {}


@api.get('/users')
def get_users():
    return users_db

@api.get('/users/{userid:int}')
def get_user(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return user
    except IndexError:
        return {}

@api.get('/users/{userid:int}/name')
def get_user_name(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return {'name': user['name']}
    except IndexError:
        return {}

@api.get('/users/{userid:int}/subscription')
def get_user_suscription(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return {'subscription': user['subscription']}
    except IndexError:
        return {}
    

@api.put('/computer', name='Create a new computer')
def get_computer(computer: Computer):
    """Creates a new computer within the database
    """
    return computer


@api.post('/item')
def post_item(item: Item):
    return item

responses = {
    200: {"description": "OK"},
    404: {"description": "Item not found"},
    302: {"description": "The item was moved"},
    403: {"description": "Not enough privileges"},
}

@api.get('/thing', responses=responses)
def get_thing():
    return {
        'data': 'hello world'
    }



  


 

 