import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    # connect to mongoDb
    client = pymongo.MongoClient("mongodb+srv://NIXBLACK:nixblack11@cluster0.tk5azpj.mongodb.net/test")
    # to check if connected to mongoDb
    # print(client)
    # to make a database
    db = client["bank"]
    # making collection is necessary to make database same is with inserting a document
    collection = db['users']
    dictionary = {
        'name':'test',
        'password':'test@123',
        'loginId':0,
        'accountNumber':1,
        'accountBalance':80000000
        }
    collection.insert_one(dictionary)    
    # multipleDictionaries = [
    #     {        
    #         'name':'test',
    #         'password':'test@123',
    #         'loginId':0,
    #         'accountNumber':1,
    #         'accountBalance':80000000
    #     },
    #     {
    #         'name':'test',
    #         'password':'test@123',
    #         'loginId':0,
    #         'accountNumber':1,
    #         'accountBalance':80000000
    #     }
    # ]
    # collection.insert_many(multipleDictionaries)
    # dictionary2 = {
    # 'name': 'Alice',
    # 'password': 'alice123',
    # 'loginId': 2,
    # 'accountNumber': 3,
    # 'accountBalance': 500000
    #     }

    # dictionary3 = {
    #     'name': 'Bob',
    #     'password': 'bob456',
    #     'loginId': 3,
    #     'accountNumber': 4,
    #     'accountBalance': 1000000
    # }

    # dictionary4 = {
    #     'name': 'Charlie',
    #     'password': 'charlie789',
    #     'loginId': 4,
    #     'accountNumber': 5,
    #     'accountBalance': 250000
    # }

    # dictionary5 = {
    #     'name': 'Dave',
    #     'password': 'dave000',
    #     'loginId': 5,
    #     'accountNumber': 6,
    #     'accountBalance': 1500000
    # }

    # dictionary6 = {
    #     'name': 'Emily',
    #     'password': 'emily111',
    #     'loginId': 6,
    #     'accountNumber': 7,
    #     'accountBalance': 750000
    # }

    # dictionary7 = {
    #     'name': 'Frank',
    #     'password': 'frank222',
    #     'loginId': 7,
    #     'accountNumber': 8,
    #     'accountBalance':344444
    # }
    # collection.insert_many([dictionary2, dictionary3, dictionary4, dictionary5, dictionary6, dictionary7])