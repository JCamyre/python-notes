from sqlalchemy import create_engine
engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')


app = Flask(__name__)
db = SQLAlchemy(app)


class Car(Base):
    make = db.Column(db.String(50))
    # model
    # year


db.session.add(Car(make='Toyota'))

db.session.commit()

