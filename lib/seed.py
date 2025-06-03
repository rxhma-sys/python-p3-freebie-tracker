#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebie_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()
session.commit()

c1 = Company(name="TechCity", founding_year=2005)
c2 = Company(name="FreebieCo", founding_year=1995)

d1 = Dev(name="Eugene")
d2 = Dev(name="Kelly")

session.add_all([c1, c2, d1, d2])
session.commit()

# Create freebies
f1 = Freebie(item_name="Sticker Pack", value=5, company=c1, dev=d1)
f2 = Freebie(item_name="T-Shirt", value=20, company=c1, dev=d2)
f3 = Freebie(item_name="Mug", value=10, company=c2, dev=d1)

session.add_all([f1, f2, f3])
session.commit()
