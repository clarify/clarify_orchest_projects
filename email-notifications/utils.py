import os
from sqlitedict import SqliteDict

def get_shared_dict():
    sqlite_dict_path = os.environ.get("SQLITE_LOCATION", "/data/global-key-values.sqlite")
    return SqliteDict(sqlite_dict_path, autocommit=True)
