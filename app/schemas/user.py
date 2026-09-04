from pydantic import BaseModel,Field,UUID4,EmailStr,field_validator,model_validator
from typing import Optional
from datetime import datetime
import re
from app.schemas.common import Role


class UserBase(BaseModel):
    id:UUID4
    email:EmailStr
    full_name:str
    role:Role
    facility_id:UUID4
   

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

class UserResponse(UserBase):
    is_active:bool
    model_config={"from_attributes":True}
    
    
    

        
   







    



