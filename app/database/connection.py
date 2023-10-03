from app.database.base import session_factory

def select_one(query):
    try:
        return query.one_or_none()
    except:
        return None


def select_all(query):
    try:
        return query.all()
    except:
        return None


def select_from_db(obj, session = None):
    if session is None:
        session = session_factory()
    result = session.query(obj)
    try:
        result = select_all(result)
    except:
        result = None
    session.close()
    return result
