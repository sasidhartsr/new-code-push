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

class WatchInformation(Base):
    __tablename__ = "fossil"
    bandcolour = Column("bandcolour", String)
    bandmaterial = Column("bandmaterial", String)
    bandwidth = Column("bandwidth", String)
    bezelfunction = Column("bezelfunction", String)
    brand = Column("brand", String)
    calendartype = Column("calendartype", String)
    casediameter = Column("casediameter", String)
    casematerial = Column("casematerial", String)
    casethickness = Column("casethickness", String)
    displaytype = Column("displaytype", String)
    caseshape = Column("caseshape", String)
    itemweight = Column("itemweight", String)
    modelnumber = Column("modelnumber", String)
    partnumber = Column("partnumber", String)
    specialfeatures = Column("specialfeatures", String)
    warrantytype = Column("warrantytype", String)
    movement = Column("movement", String)
    waterresistancedepth = Column("waterresistancedepth", String)
    bandsize = Column("bandsize", String)
    mobilenumber = Column("mobilenumber", Integer,primary_key=True)

# http://127.0.0.1:5000/watch-information/and-method/Fossil?mobile=88888&bandcolour=Black
@app.route('/watch-information/and-method/Fossil', methods=['GET'])
def home():
    mobileNumber = request.args.get('mobile')
    bandcolourNameFull = request.args.get('bandcolour')
    results = session.query(WatchInformation).filter(and_(WatchInformation.mobilenumber == mobileNumber,WatchInformation.bandcolour == bandcolourNameFull)).all()
    results_1 = [item.__dict__ for item in results]
    for item in results_1:
        del item['_sa_instance_state']
    return json.dumps(results_1)

app.run(debug=True)
