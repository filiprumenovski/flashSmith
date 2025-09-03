import hashlib

def stable_guid(*fields: str) -> int:
    base = "\x1f".join([f or "" for f in fields])
    h = hashlib.sha1(base.encode("utf-8")).hexdigest()
    # shrink to 60 bits for SQLite
    return int(h[:15], 16)
