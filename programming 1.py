import json
from datetime import datetime
import psycopg2
from flask import Flask
from flask_restful import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(database_url, echo=True, poolclass=NullPool)
Session = sessionmaker(bind=engine)
session = Session()
class sasidhar_company(Base):
    __tablename__ = 'sasidhar_company'
    Name = Column("name", String)
    age = Column("age", Integer)
    emailId = Column("emailid", String, primary_key=True)
    address = Column("address", String)
    salary = Column("salary", Integer)
@app.route('/sasi-company-list', methods=['GET'])
def home():
    results = session.query(sasidhar_company).all()
    for item in results:
        results_1=[item.__dict__ for item in results]
    for item in results_1:
        del item['_sa_instance_state']
    return json.dumps(results_1)
app.run(debug=True)