from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#ODHdongha0511 -> 본인의 비밀번호로 변경
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:ODHdongha0511@127.0.0.1:3306/mindbut"

engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding = "utf-8")

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()