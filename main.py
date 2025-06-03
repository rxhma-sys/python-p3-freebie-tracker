from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib.models import Base, Company, Dev, Freebie

# Connect to the database
engine = create_engine("sqlite:///freebies.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

company1 = Company(name="Moringa", founding_year=2015)
company2 = Company(name="Zee Gen", founding_year=2019)

dev1 = Dev(name="Rahma")
dev2 = Dev(name="Zahra")

# Create freebies
freebie1 = company1.give_freebie(dev1, "T-shirt", 20)
freebie2 = company2.give_freebie(dev2, "Notebook", 10)
freebie3 = company1.give_freebie(dev2, "Pen", 5)

session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
session.commit()

print("🔹 Freebie Details:")
for freebie in session.query(Freebie).all():
    print(freebie.print_details())

print("\n🔹 Has Rahma received a T-shirt?")
print(dev1.received_one("T-shirt")) 

print("\n🔹 Giving away the 'Pen' from Sarah to Rahma:")
success = dev2.give_away(dev1, freebie3)
print("Give away successful:", success)
print(freebie3.print_details())

print("\n🔹 Oldest Company:")
oldest = Company.oldest_company(session)
print(f"{oldest.name} founded in {oldest.founding_year}")
