import uuid
import re
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

def generate_user_id():
    return str(uuid.uuid4())

def hash_password(password):
    return generate_password_hash(password)

def verify_password(plain_password, hashed_password):
    return check_password_hash(hashed_password, plain_password)

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_user_input(data, required_fields):
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing fields: {', '.join(missing_fields)}"
    return True, None

def format_mongo_id(document):
    if document and "_id" in document:
        document["_id"] = str(document["_id"])
    return document
