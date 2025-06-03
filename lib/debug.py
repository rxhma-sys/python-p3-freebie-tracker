#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebie_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

# Test oldest company
oldest = Company.oldest_company(session)
print(f"Oldest company: {oldest.name}, founded {oldest.founding_year}")

# Test freebies for dev Alice
alice = session.query(Dev).filter_by(name="Alice").one()
print(f"{alice.name}'s freebies:")
for f in alice.freebies:
    print(f"- {f.print_details()}")

# Test if Alice received a "Mug"
print(f"Alice received a Mug? {alice.received_one('Mug')}")

# Test give_freebie method
new_freebie = oldest.give_freebie(alice, "Keychain", 7)
session.add(new_freebie)
session.commit()
print(new_freebie.print_details())

# Test give_away method
bob = session.query(Dev).filter_by(name="Bob").one()
print(f"Before give_away, owner of T-Shirt: {f2.dev.name}")
result = d2.give_away(alice, f2)  # Bob tries to give T-Shirt to Alice
print(f"Give away success? {result}")
print(f"After give_away, owner of T-Shirt: {f2.dev.name}")

