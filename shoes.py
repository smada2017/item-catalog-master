from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import ShoeStore, Base, Shoe, User

engine = create_engine('sqlite:///shoecatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="dummy", email="saivardhanmada@gmail.com")
session.add(User1)
session.commit()

#Nike Store
shoeStore1 = ShoeStore(name="Nike", user_id="1")

session.add(shoeStore1)
session.commit()

shoe1 = Shoe(name="Flynits",
              user_id=1, price="$89.99",
              description="running shoe",
              shoestore=shoeStore1)

session.add(shoe1)
session.commit()

shoe2 = Shoe(name="Nike React",
              user_id=1, price="$149.99",
              description="workout shoe",
              shoestore=shoeStore1)

session.add(shoe2)
session.commit()


shoe3 = Shoe(name="Nike Pegasus 33",
              user_id=1, price="$109.99",
              description="training shoe",
              shoestore=shoeStore1)

session.add(shoe3)
session.commit()


#Adidas Store
shoeStore2 = ShoeStore(name="Adidas", user_id="2")

session.add(shoeStore2)
session.commit()

shoe1 = Shoe(name="Adidas NMD",
              user_id=1, price="$129.99",
              description="lifestyle shoe",
              shoestore=shoeStore2)

session.add(shoe1)
session.commit()

shoe2 = Shoe(name="Adidas Ultraboost",
              user_id=1, price="$189.99",
              description="running shoe",
              shoestore=shoeStore2)

session.add(shoe2)
session.commit()


shoe3 = Shoe(name="Adidas Yeezys",
              user_id=1, price="$250.00",
              description="fashion shoe",
              shoestore=shoeStore2)

session.add(shoe3)
session.commit()


print "Added shoe inventory!"
