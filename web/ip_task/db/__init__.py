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
