import json
from datetime import datetime
import psycopg2
from flask import Flask, request
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


class tsr(Base):
    __tablename__ = "tsr"
    Name = Column("name", String)
    Age = Column("age", Integer)
    Mobile = Column("mobile", Integer, primary_key=True)
    Address = Column("address", String)


@app.route('/create-record/tsr/post', methods=['POST'])
def insert_records():
    # Read the request body!
    try:
        request_body = request.get_json(force=True)
        for item in request_body:
            record = tsr(Name=item.get("name"),
                         Mobile=item.get("mobile"),
                         Address=item.get("address"),
                         Age=item.get("age"))
            session.add_all([record])
        session.commit()

        return {"status": "Success"}
    except Exception as err:
        session.rollback()
        return {"status": "Failed", "msg": str(err)}

app.run(debug=False)

