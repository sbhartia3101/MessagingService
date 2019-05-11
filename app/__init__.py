from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
# db = SQLAlchemy()

db = SQLAlchemy(app)
db.init_app(app)



from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app import routes, models

