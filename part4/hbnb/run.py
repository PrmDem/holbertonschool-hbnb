from app import create_app
from app.extensions import db
import os

app = create_app()

if __name__ == '__main__':
    print(os.path.abspath('development.db'))
    with app.app_context():
        # affiche le chemin exact que SQLAlchemy utilise
        print("SQLAlchemy is using:", db.engine.url)
    app.run(debug=True)
