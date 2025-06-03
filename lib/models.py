# lib/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    founding_year = Column(Integer)

    freebies = relationship("Freebie", back_populates="company")
    devs = relationship("Dev", secondary="freebies", back_populates="companies", viewonly=True)

    def give_freebie(self, dev, item_name, value):
        return Freebie(item_name=item_name, value=value, company=self, dev=dev)

    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    freebies = relationship("Freebie", back_populates="dev")
    companies = relationship("Company", secondary="freebies", back_populates="devs", viewonly=True)

    def received_one(self, item_name):
        #Check if this dev has received a freebie with the givvenitem name
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, other_dev, freebie):
        
        # Returns True if successful, otherwise returns False.
    
        if freebie in self.freebies:
            freebie.dev = other_dev
            return True
        return False


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)

    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    dev_id = Column(Integer, ForeignKey('devs.id'), nullable=False)

    company = relationship("Company", back_populates="freebies")
    dev = relationship("Dev", back_populates="freebies")

    def print_details(self):
        """Return a string with formatted freebie details."""
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}."
