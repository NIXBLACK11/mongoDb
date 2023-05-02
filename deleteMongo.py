import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb+srv://NIXBLACK:nixblack11@cluster0.tk5azpj.mongodb.net/test")
    db = client["bank"]
    collection = db['users']
    
    # to delete single
    before = {"name": "Alice"}
    after ={'$set':{"password": "alice123"}}
    collection.delete_one(before, after)
    
    # to delete many delete_many
    before = {"name": "Alice"}
    after ={'$set':{"password": "alice123"}}
    up = collection.delete_many(before, after)
    print(up.modified_count)