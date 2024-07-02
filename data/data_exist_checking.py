import os
import pandas as pd
from pymongo import MongoClient
# from dotenv import load_dotenv

def data_checker():
    # load_dotenv()

    MONGO_URL = os.getenv('MONGO_URL_ID')
    DB_NAME = os.getenv('DB_NAME_ID')
    COLLECTION_NAME = os.getenv('COLLECTION_NAME_ID')

    client=MongoClient(MONGO_URL)
    db=client[DB_NAME]
    collection=db[COLLECTION_NAME]
    
    query={}
    count = collection.count_documents(query)
    client.close()
    return count