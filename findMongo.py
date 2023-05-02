import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    db = client["bank"]
    collection = db['users']
    
    # to find any random document
    one = collection.find_one()
    print(one)
    
    # to find according to value
    two = collection.find_one({'name':'test'})
    print(two)
    
    # to find all documents with a certain value
    allDocs = collection.find({'name':'test'}).limti(1) #to limit output to 1
    for item in allDocs:
        print(item)
     
    # to return only specified  even if one 1 all other 0 vice-versa
    three = collection.find_one({'name':'test'}, {'name':1})
    print(three)
    
    # according to some modifier lte less than equal to
    allDocs = collection.find({'name':'test', 'accountBalance':{'$lte':90}})
    print(collection.count_documents())
    for item in allDocs:
        print(item)
        
    # count documents
    print(collection.count_documents())
    print(collection.count_documents({'name':'test', 'accountBalance':{'$lte':90}}))
