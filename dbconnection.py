from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"
#  Engine is the connection manager to the database
#  It handles communication between sqlite and python 
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# this creates a session factory 
#  a session is temporary connection to talk with the Db
