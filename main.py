from fastapi import FastAPI,HTTPException
from app.schemas.doctor_schema import create_doctor,create_patient
import re
app=FastAPI()

doctor_list=[]
patient_list=[]

create_id=0
# doctor_dict={{id,name,specialization,email,active}}
@app.get("/")
def home():
    return {"message":"HI Welcome Site"}

@app.post("/doctor_create")

def create_doctor(input:create_doctor):
    global create_id
    create_name=r"^[a-zA-Z]+$"
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if not re.match(create_name,input.name):
        raise HTTPException(status_code=400,detail="Name Only Character")
    if not re.match(create_name,input.specialization):
        raise HTTPException(status_code=400,detail="specialization Only Character")
    if not re.match(email_pattern,input.email):
        raise HTTPException(status_code=400,detail="Enter email Format")
    create_id+=1
    doctor={"id":create_id,"name":input.name,"specialization":input.specialization,"email":input.email,"is_active":input.is_active}
    doctor_list.append(doctor)
    
    return {"message":"doctor created Successfully"}

@app.get("/list_doctor")
def get_doctor():
    return doctor_list

@app.get("/doctor/{doctor_id}")
def get_doctor_by_id(doctor_id:int):
    # if not doctor_list.pop(id)==doctor_id:
    #     raise HTTPException(status_code=400,detail="NO Id Matched") 
    # return doctor_list
    for doctor in doctor_list:
        if doctor["id"]==doctor_id:
            return doctor
    # print(doctor)
    return {"message":"Doctor not found"}

@app.post("/patient")

def create_patient(input:create_patient):
    create_name = r"^[a-zA-Z]+$"
    phone =r"^[6-9][0-9]{9}$"
    if not re.match(create_name,input.name):
        raise HTTPException(status_code=400,detail="Name Only Character")
    if not input.age > 0:
        raise HTTPException(status_code=400,detail="Only age above 0")
    print(input.phone)
    if not re.match(phone,input.phone):
        raise HTTPException(status_code=400,detail="Enter Only Number")
    patient_list.append(input)
    
    return{"message":"patient created successfully"}

@app.get("/get_patient")
def get_patient():
    return patient_list