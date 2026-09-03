from pydantic import BaseModel,Field,UUID4,EmailStr,field_validator,model_validator
from typing import Optional
from datetime import datetime
from enum import Enum
import re

class Role(str,Enum):
    super_admin="SUPER_ADMIN"
    prison_admin="PRISON_ADMIN"
    customer="CUSTOMER"

class UserBase(BaseModel):
    email:EmailStr
    full_name:str
    role:Role

    @field_validator("full_name")
    @classmethod
    def name(cls,value:str)->str:
        value=" ".join(value.split())
        if len(value) <3 or len(value) > 100:
            raise ValueError("Full name must be between 3 to 100 characters")
        parts=value.split()
        if len(parts) < 2:
            raise ValueError("Please provide both  first an last name")

        if not re.match(r"^[A-Za-z\s'-]+$", value):
            raise ValueError("Full name can only contain letters,spaces,hypness,and all unnessary attributes")

        return value.title()

        
class UserCreate(UserBase):
    password:str
    confirm_password:str

    @model_validator(mode="after")
    def pass_val(self)->"UserCreate":
        if self.password != self.confirm_password:
            raise ValueError("pasword and conform password doesnot match")
        return self
        
   







    



