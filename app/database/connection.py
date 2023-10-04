from app.database.base import session_factory

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


def insert_into_db(obj, session = None):
    if session is None:
        session = session_factory()
    session.add(obj)
    session.commit()
    session.close()


def update_db(obj, attrs_to_update, session = None):
    if session is None:
        session = session_factory()
    for key in attrs_to_update:
        setattr(obj, key, attrs_to_update[key])
    session.commit()
    session.close()


def delete_from_db(obj, session = None):
    if session is None:
        session = session_factory()
    session.delete(obj)
    session.commit()
    session.close()