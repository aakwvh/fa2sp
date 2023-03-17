import pymongo
import psycopg2

# MongoDB Connection
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["huwebshop"]
mongo_collection = mongo_db["products"]

# PostgreSQL Connection
pg_conn = psycopg2.connect(database="huwebshop", user="postgres", password="admin", host="localhost", port="5432")
pg_cursor = pg_conn.cursor()

# Get column names dynamically
columns = []
for document in mongo_collection.find():
    for key in document.keys():
        if key not in columns:
            columns.append(key)

print(columns)
# Loop through MongoDB collection and transfer data to PostgreSQL



        # Build insert statement dynamically



        # Map MongoDB document values to PostgreSQL query



# Commit changes and close connections
pg_conn.commit()
pg_cursor.close()
pg_conn.close()
mongo_client.close()