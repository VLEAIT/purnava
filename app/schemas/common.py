from enum import Enum
from typing import TypeVar,Optional,Generic
from pydantic import BaseModel,Field
from datetime import datetime


T=TypeVar("T")


class Role(str,Enum):
    super_admin="SUPER_ADMIN"
    prison_admin="PRISON_ADMIN"
    customer="CUSTOMER"

class APIResponse(BaseModel, Generic[T]):
    success: bool = Field(..., description="Indicates whether the API request was successful or not.")
    data: Optional[T] = Field(None, description="The data returned by the API request, if any.")
    error: Optional[str] = Field(None, description="An error message, if the API request was not successful.")
    timestamp: datetime = Field(default_factory=datetime.now)
    model_config = {"from_attributes": True}