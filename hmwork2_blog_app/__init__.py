from flask import Flask

# Import the config Object
from config import Config

# Import forthe SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

# Import ehr Migrate Object
from flask_migrate import Migrate

app = Flask(__name__)
# this completes the config cycle for our Flask App
#And give access to our Database (when we have one)
# along with our Secret Key
app.config.from_object(Config)

# Init our database (db)
db = SQLAlchemy(app)

# Init the migrator
migrate = Migrate(app,db)

from hmwork2_blog_app import routes,models