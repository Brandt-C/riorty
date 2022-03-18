from flask import Flask

from config import Config
from flask_cors import CORS


from .user.routes import user 
from .models import db, login
from flask_migrate import Migrate
from .blog.routes import blog

app = Flask(__name__)

CORS(app, origins=["*"])

app.config.from_object(Config)

app.register_blueprint(user)
app.register_blueprint(blog)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)


from . import routes
from . import models