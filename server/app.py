#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
'''
configure database
similar to alembic.ini
Handled by Flask-Migrate
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# We're getting a warning to change app/migrations/alembic.ini
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# handling migrations
migrate = Migrate(app, db)

# initialize app
db.init_app(app)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
