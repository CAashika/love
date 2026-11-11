from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker
DATABASE_URL="sqlite:///lovetable.db"
engine=create_engine(DATABASE_URL)
engine.connect()
Base=declarative_base()
class Love_table(Base):
    __tablename__="lovecal"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name1=Column(String)
    name2=Column(String)
    perc=Column(Integer)
Base.metadata.create_all(bind=engine)
SessionLocal=sessionmaker(bind=engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
