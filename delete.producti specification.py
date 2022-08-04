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
from sqlalchemy import and_, or_

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

#http://127.0.0.1:5000/watch-information/delete-record/Fossil?mobilenumber=77777777
@app.route('/watch-information/delete-record/Fossil', methods=['DELETE'])
def tsr_delete_records():
        mobileNumber = int(request.args.get('mobilenumber'))
        session.query(WatchInformation).filter(WatchInformation.mobilenumber == mobileNumber).delete()
        session.commit()
        return "Customer record with {} number has been deleted".format(mobileNumber)
app.run(debug=True)
