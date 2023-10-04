from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = "sqlite:///my_database.db"  
engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="John", age=30)
session.add(new_user)
session.commit()

users = session.query(User).all()
for user in users:
    print(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}")

session.close()
