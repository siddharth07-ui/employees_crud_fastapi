from sqlalchemy import Column, Integer, String
from database import Base

class Employee(Base):
    __tablename__ = 'employeedetails'

    employee_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    address = Column(String)
    salary = Column(Integer)
    department = Column(String)
    bank_name = Column(String)
    nominee_name = Column(String)
