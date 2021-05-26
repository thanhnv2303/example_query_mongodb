from pymongo import MongoClient


class MongoDBConfig:
    # NAME = "ReadUser"
    # PASSWORD = "bkc_123"
    # HOST = "25.19.185.225"
    PORT = "27027"
    NAME = "just_for_dev"
    PASSWORD = "password_for_dev"
    HOST = "localhost"
    # PORT = "27027"
    DATABASE = "EXTRACT_DATA_KNOWLEDGE_GRAPH"
    TRANSACTIONS = "TRANSACTIONS"
    TRANSACTIONS_TRANSFER = "TRANSACTIONS_TRANSFER"
    WALLET = "WALLET"
    POOL = "POOL"
    BLOCKS = "BLOCKS"
    TOKENS = "TOKENS"


class Database(object):
    """Manages connection to  database and makes async queries
    """

    def __init__(self):
        self._conn = None
        url = f"mongodb://{MongoDBConfig.NAME}:{MongoDBConfig.PASSWORD}@{MongoDBConfig.HOST}:{MongoDBConfig.PORT}"
        self.mongo = MongoClient(url)
        self.mongo_db = self.mongo[MongoDBConfig.DATABASE]
        self.mongo_transactions = self.mongo_db[MongoDBConfig.TRANSACTIONS]
        self.mongo_transactions_transfer = self.mongo_db[MongoDBConfig.TRANSACTIONS_TRANSFER]
        self.mongo_wallet = self.mongo_db[MongoDBConfig.WALLET]
        self.mongo_tokens = self.mongo_db[MongoDBConfig.TOKENS]
        self.mongo_blocks = self.mongo_db[MongoDBConfig.BLOCKS]
        self.mongo_token_collection_dict = {}

    def get_transaction_transfer(self, txId):
        key = {'transaction_hash': txId}
        return self.mongo_transactions_transfer.find_one(key)

    def get_transactions_transfer_in_block(self, block_num):
        key = {'block_number': block_num}
        return self.mongo_transactions_transfer.find(key)

    def get_transactions_transfer_from(self, from_address):
        key = {'from_address': from_address}
        return self.mongo_transactions_transfer.find(key)

    def get_wallet(self, address):
        key = {"address": address}

        return self.mongo_wallet.find_one(key)

    def update_event(self, collection, event):
        key = {'_id': event.get('_id')}
        data = {"$set": event}
        return self.mongo_db[collection].update_one(key, data, upsert=True)

    def get_event(self, collection, type_):
        key = {'type': type_}
        return self.mongo_db[collection].find(key)
