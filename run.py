

from app import app
from app.models import db, User, Post

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User, 'Post' : Post}