from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, UUID4


class ImpactStoryBase(BaseModel):
    headline: str = Field(..., max_length=255)
    narrative: str
    family_background: str
    rehabilitation_goal: str


class ImpactStoryCreate(ImpactStoryBase): 
    pass


class ImapctStoryResponse(ImpactStoryBase):
    id: UUID4
    prisoner_id: UUID4
    updated_at: datetime

    model_config = {"from_attributes": True}


class PrisonerBase(BaseModel):
    display_code: str = Field(..., max_length=100)
    skill_tags: Optional[list[str]] = []


class PrisonerCreate(PrisonerBase):
    facility_id: UUID4
    impact_story: Optional[ImapctStoryResponse] = None
    created_at: datetime

    model_config = {"from_attributes": True}