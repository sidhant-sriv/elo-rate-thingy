from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Player(Base):
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
    
def displayAll() -> list[Player]:
    '''Displays all players
        returns:
            List of Player object
    '''
    results = session.query(Player).all()
    return results

def displayRating(rating: int) -> list[Player]:
    '''Displays player by rating
        parameters:
            id[int]: ID of the player
        returns:
            List of Player object
    '''
    results = session.query(Player).filter(Player.rating>rating).all()
    return results

def displayID(id: int) -> Player:
    '''Displays player by ID
        parameters:
            id[int]: ID of the player
        returns:
            Player object
    '''
    results = session.query(Player).filter(Player.id == id).first()
    return results

def addPlayer(name: String, rating: int, description: String | None = None):
    '''Adds a new player to the database
        Parameters:
            name[String]: Name of the player
            rating[int]: Rating of the player
            description[String]: Description of the player
    '''
    player = Player(name=name, rating=rating, description=description)
    session.add(player)
    session.commit()

def updatePlayer(id: int, rating_new: int):
    '''Updates rating of a player
        Parameters:
            id[int]: ID of the player to change
            rating_new[int]: The updated rating of the player
    '''
    result = session.query(Player).filter(Player.id == id).first()
    result.rating = rating_new
    session.commit()

def deletePlayer(id: int):
    '''Deletes a player from the database
        Parameters: 
            id[int]: ID of player to delete
    '''
    results = session.query(Player).filter(Player.id == n).first()
    session.delete(results)
    session.commit()

engine = create_engine("sqlite:///mydb.db") #, echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

'''
ALL FOR TESTING PURPOSES

addPlayer(name="Sidhant", rating=1600, description="Googooooogaagaa")
addPlayer(name="Tony Stark", rating=1500, description="Iron Man")
addPlayer(name="Dude", rating=1300, description="Wtf am I doing")
addPlayer(name=input("Name: "), rating=input("Rating: "), description=input("Description: "))

for r in displayAll():
    print(r)

for r in displayRating(1400):
    print(r)

print("-------Update---------")
n = input("Enter id to be changed: ")
r = int(input("Enter new rating: "))
updatePlayer(n, r)

for r in displayAll():
    print(r)

print("--------Delete------")
n = input("Enter id to delete: ")
deletePlayer(n)

for r in displayAll():
    print(r)
'''