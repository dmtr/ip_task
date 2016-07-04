import logging
from . import queries

logger = logging.getLogger(__name__)


def init(connection):
    c = connection.cursor()
    try:
        c.execute(queries.CREATE_TABLE)
        c.execute(queries.CREATE_FUNC)
        c.execute(queries.CREATE_VIEW)
        c.execute(queries.CREATE_INDEX)
        connection.commit()
    except Exception as e:
        logger.exception('Error while init db %s', e)
    finally:
        c.close()


def refresh_view(connection):
    c = connection.cursor()
    c.execute(queries.REFRESH_VIEW)


def check_users(user1, user2, connection):
    c = connection.cursor()
    c.execute("SELECT count(*) FROM user_ip WHERE user1 = (%s) AND user2 = (%s)", (user1, user2))
    r = c.fetchone()
    return r[0]
