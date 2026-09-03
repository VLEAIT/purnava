from sqlalchemy import CheckConstraint,DateTime,ForeignKey,String,Text,Boolean
from datetime import datetime
from typing import TYPE_CHECKING,List,Optional
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base,CreateAtMixin,TimeStampMixin
import uuid

if TYPE_CHECKING:
    from app.models.facility import Facaility


class User(Base,TimeStampMixin,kw_only=True):
    __tablename__="users"

    id:Mapped[uuid.UUID]=mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        doc="Primary key UUID for user refrenecing internally"
        )

    facility_id:Mapped[uuid.UUID]=mapped_column(
        UUID(as_uuid=True),
        ForeignKey("facilities.id",ondelete="CASCADE"),
        nullable=False,
        index=True,
        doc="Foreign ket pointing to the managing correctional facility",
        )
    email:Mapped[str]=mapped_column(
        String(255),
        nullable=False,
        index=True,
        doc="User email",
        )
    hashed_password:Mapped[str]=mapped_column(
        String(255),
        nullable=False,
    )
    full_name:Mapped[str]=mapped_column(
        String(255),
        nullable=False,
    )
    is_active:Mapped[bool]=mapped_column(
        Boolean,
        default=True,
    )


    

  