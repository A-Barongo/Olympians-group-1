from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///many_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    fake = Faker()