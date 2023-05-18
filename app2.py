from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'Teachers'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    rating = Column("rating", Integer, nullable=False)
    description = Column("desc", String)

    def __init__(self, name, rating, description = None):
        self.name = name
        self.rating = rating
        self.description = description

    def __repr__(self):
        return f"{self.id}: {self.name}({self.rating}) - {self.description}"
    

engine = create_engine("sqlite:///mydb.db") #, echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

t1 = Teacher(name="Sidhant", rating=1600, description="Googooooogaagaa")
t2 = Teacher(name="Tony Stark", rating=1500, description="Iron Man")
t3 = Teacher(name="Dude", rating=1300, description="Wtf am I doing")
session.add_all([t1, t2, t3])
session.commit()

t4 = Teacher(name=input("Name: "), rating=input("Rating: "), description=input("Description: "))
session.add(t4)
session.commit()

print("------ALL'-------")
results = session.query(Teacher).all()
for r in results:
    print(r)


print("-------Rating>1400-----")
results = session.query(Teacher).filter(Teacher.rating>1400).all()
for r in results:
    print(r)

print("-------Update---------")
n = input("Enter id to be changed: ")
r = int(input("Enter new rating: "))
results = session.query(Teacher).filter(Teacher.id == n).first()
results.rating = r
session.commit()

print("--------ALL--------")
for r in session.query(Teacher).all():
    print(r)

print("--------Delete------")
n = input("Enter id to delete: ")
results = session.query(Teacher).filter(Teacher.id == n).first()
session.delete(results)
session.commit()

print("---------ALL-----------")
for r in session.query(Teacher).all():
    print(r)
