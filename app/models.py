from bson.objectid import ObjectId
from app import mongo

class User:
    collection = mongo.db.users

    @staticmethod
    def to_json(data):
        return {
            "id": str(data["_id"]),
            "name": data["name"],
            "email": data["email"]
        }

    @staticmethod
    def find_all():
        return [User.to_json(user) for user in User.collection.find()]

    @staticmethod
    def find_one(user_id):
        return User.to_json(User.collection.find_one({"_id": ObjectId(user_id)}))

    @staticmethod
    def insert(data):
        return User.collection.insert_one(data).inserted_id

    @staticmethod
    def update(user_id, data):
        User.collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    @staticmethod
    def delete(user_id):
        User.collection.delete_one({"_id": ObjectId(user_id)})
