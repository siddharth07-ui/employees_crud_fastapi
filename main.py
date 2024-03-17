import uvicorn
from fastapi import FastAPI, Depends, Request
import schemas
import models
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session


Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


app = FastAPI()

@app.get("/")
def root(session: Session = Depends(get_session)):
    employees = session.query(models.Employee).all()
    return employees

@app.get('/{employee_id}')
def get_item_id(employee_id: int, session: Session = Depends(get_session)):
    employee = session.query(models.Employee).get(employee_id)
    return employee

@app.post('/')
def add_item(employee: schemas.Employee, session: Session = Depends(get_session)):
    employee = models.Employee(
        name=employee.name, 
        age=employee.age, 
        gender=employee.gender, 
        address=employee.address, 
        salary=employee.salary, 
        department=employee.department, 
        bank_name=employee.bank_name, 
        nominee_name=employee.nominee_name)
    session.add(employee)
    session.commit()
    session.refresh(employee)

    return employee

@app.put('/{employee_id}')
def update_item(employee_id: int, employee: schemas.Employee, session: Session=Depends(get_session)):
    employee_obj = session.query(models.Item).get(employee_id)
    employee_obj.name = employee.name
    employee_obj.age = employee.age
    employee_obj.gender = employee.gender
    employee_obj.address = employee.address
    employee_obj.salary = employee.salary
    employee_obj.department = employee.department
    employee_obj.bank_name = employee.bank_name
    employee_obj.nominee_name = employee.nominee_name

    session.commit()
    session.refresh(employee_obj)

    return employee_obj

@app.delete('/{employee_id}')
def delete_item(employee_id: int, session: Session = Depends(get_session)):
    employee = session.query(models.Employee).get(employee_id)
    session.delete(employee)
    session.commit()
    session.close()
    return {'message': 'Item deleted successfully'}


 # at last, the bottom of the file/module
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")