from sqlalchemy import Column,Integer,String, DateTime, func
from config import DB_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import extract

engine = create_engine(DB_URI,echo=True)
Session = sessionmaker(bind=engine)
session = Session()
# 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)

class Weather(Base):
    __tablename__ = "weather"

    date = Column(DateTime, unique = True, primary_key = True)
    max_t = Column(Integer)
    min_t = Column(Integer)
    status = Column(String(10))
    direction = Column(String(30))

    def __repr__(self):
        return "<Weather({} temperature:{}~{})>".format(self.date, self.min_t, self.max_t)

def insert_data(data):
    # data type : list
    new = Weather()
    new.date, new.max_t, new.min_t, new.status, new.direction = data
    temp = session.query(Weather).filter_by( date = new.date).all()
    if temp:
        if temp == new:
            return 
        temp = new
    else:
        session.add(new)
    session.commit()

def query_weather(date = '2012 3'):
    # date type : str
    # rtype : list
    if len(date) == 4:
        return session.query(Weather).filter(extract("year",Weather.date)==int(date) ).all()
    if len(date.split())!=2:
        return '格式不正确'
    year, month = date.split()
    temp = session.query(Weather).filter(extract("year",Weather.date)==int(year),extract("month",Weather.date)==int(month) ).all()
    if not temp:
        return "无数据或日期不正确"
    return temp

def Create_table():
    Base.metadata.create_all()
    print("table {} 创建成功".format(Weather.__tablename__))

if __name__ == "__main__":
    Create_table()
    

    