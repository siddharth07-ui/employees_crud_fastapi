from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int
    gender: str
    address: str
    salary: int
    department: str
    bank_name: str
    nominee_name: str