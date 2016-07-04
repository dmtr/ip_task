import logging

import ip_task.db as db

from flask import request
from flask import current_app

logger = logging.getLogger(__name__)


def get_users_relation():
    user1 = request.args.get('user1', None)
    user2 = request.args.get('user2', None)
    if not (user1 and user2):
        return '', 400
    if db.check_users(user1, user2, current_app.db_connection):
        return '', 200
    else:
        return '', 404
