from pymongo import MongoClient

# Establish connection to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["iot_data_db"]
collection = db["iot"]

# Define schema validation rules
schema = {
    "bsonType": "object",
    "required": ["message"],
    "properties": {
        "message": {
            "bsonType": "string"
        }
    }
}

# Apply schema validation to the collection
db.command({
    "collMod": "iot",
    "validator": {
        "$jsonSchema": schema
    }
})
