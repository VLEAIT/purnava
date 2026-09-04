from pydantic import BaseModel,Field,UUID4
from typing import Optional

class FacalityBase(BaseModel):
    name:str
    location:str
    welfare_officer_number:Optional[str]


class FacalityCreate(FacalityBase):
    pass

class FacalityResponse(FacalityBase):
    id:UUID4
    is_active:bool

    model_config={"from_attributes":True}


