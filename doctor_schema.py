from pydantic import BaseModel,EmailStr

class create_doctor(BaseModel):
    name:str
    specialization:str
    email:EmailStr
    is_active:bool

class create_patient(BaseModel):
    name:str
    age:int
    phone:str