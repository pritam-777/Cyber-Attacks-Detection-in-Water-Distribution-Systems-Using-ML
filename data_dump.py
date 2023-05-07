import pandas as pd
import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://pritam97:pritam123@pritam.1dl9xyw.mongodb.net/?retryWrites=true&w=majority")


DATA_FILE_PATH = "D:\Project\BATADAL Cyber Attacks Detection in Water System\water distribution data.csv"

DATABASE_NAME = "WATER_SYSTEM_DATA"
COLLECTION_NAME = "WATER_DISTRIBUTION"


if __name__ =="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Row and columns:{df.shape}")
    #convert dataframe to json formate 
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
