from datetime import datetime, timedelta

def insert_url(db, original_url, short_code, expires_in=None):
    doc = {
        "original_url": original_url,
        "short_code": short_code,
        "created_at": datetime.utcnow(),
        "clicks": 0
    }
    if expires_in:
        doc["expires_at"] = datetime.utcnow() + timedelta(hours=expires_in)
    db.urls.insert_one(doc)

def find_original_url(db, short_code):
    url = db.urls.find_one({"short_code": short_code})
    if not url:
        return None
    # Check for expiration
    if "expires_at" in url and datetime.utcnow() > url["expires_at"]:
        db.urls.delete_one({"short_code": short_code})
        return None
    return url["original_url"]

def increment_clicks(db, short_code):
    db.urls.update_one({"short_code": short_code}, {"$inc": {"clicks": 1}})

def find_existing_short_code(db, original_url):
    return db.urls.find_one({"original_url": original_url})

def is_short_code_taken(db, code):
    return db.urls.find_one({"short_code": code}) is not None

def get_clicks(db, short_code):
    url = db.urls.find_one({"short_code": short_code})
    return url["clicks"] if url else 0
