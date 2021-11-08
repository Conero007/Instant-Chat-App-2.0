from .user import User
from pymongo import MongoClient
from werkzeug.security import generate_password_hash

password = 'test'
database = 'ChatDB'
client = MongoClient(f"mongodb+srv://test:{password}@chatdb.xjlro.mongodb.net/{database}?retryWrites=true&w=majority")

chat_db = client.get_database("ChatDB")
users_collection = chat_db.get_collection("users")


def save_user(email, password):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({'_id': email, 'password': password_hash})
    return User(email, password_hash)
    
def get_user(email):
    info = users_collection.find_one({"_id": email})
    if info is not None:
        return User(email=info["_id"], password=info["password"])
    return None
    

if __name__ == '__main__':
    # save_user(email="test_user@test.com", password="12345678")
    # print(get_user("test_user@test.com"))
    print("database.py end!")