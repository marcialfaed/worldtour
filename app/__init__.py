from flask import Flask
from app.database import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///worldtour.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

from app.routes import *  # Use absolute import instead of relative

if __name__ == '__main__':
    app.run(debug=True)
