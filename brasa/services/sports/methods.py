from brasa.utils import find_collection


def retrieve_sports ():
    mdb_conn = find_collection("sports")

    return [ sport["name"] for sport in mdb_conn.find({}) ]