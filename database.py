import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod # we are not using "self" method!
    def initialize():
        client = pymongo.MongoClient(Database.URI) # give me the client with defined URI
        Database.DATABASE = client['fullstack_test'] # give me the defined database

    # inserting data into a collection
    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data) # give me the collection from the selected database and put some data in it

    # finding data in the collections
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    # finds the first element
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)