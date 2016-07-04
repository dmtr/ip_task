import logging
import logging.config
import os
import sys

import click
import psycopg2
import ip_task.db as db

from flask import Flask


def get_config():
    settings = os.getenv('IP_TASK_SETTINGS', 'development')
    config = None
    if settings == 'development':
        from ip_task.etc.config import DevelopmentConfig as config
    elif settings == 'production':
        from ip_task.etc.config import ProductionConfig as config

    return config


def create_app():
    """Create Flask application"""
    app = Flask(__name__)

    config = get_config()
    if config:
        app.config.from_object(config)
    else:
        print('wrong IP_TASK_SETTINGS value')
        sys.exit(1)

    app.logger.handlers = []
    logging.config.dictConfig(app.config.get('LOGGING', {}))

    app.db_connection = psycopg2.connect(host=config.DB_HOST, user=config.DB_USER, database=config.DB_NAME)

    from ip_task import views
    app.add_url_rule('/users_relation', 'users_relation', views.get_users_relation, methods=['GET'])

    return app


app = create_app()


@app.cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')
    db.init(app.db_connection)
    click.echo('done')
