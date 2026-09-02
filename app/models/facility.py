import uuid
from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import String, Boolean, DateTime, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import CreateAtMixin

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.prisoner import Prisoner


class Facaility(Base, CreateAtMixin, kw_only=True):

    __tablename__ = "facilities"
    __table_args__ = (
        CheckConstraint(
            "length(trim(name)) >= 3",
            name="check_facility_name_length",
        ),
        CheckConstraint(
            "length(trim(location)) >= 2",
            name="check_facility_location_length",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        doc="Primary Key UUID for internal facility referencing",
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        doc="Name of the facility (e.g., 'Gulmi District Prison Workshop')",
    )

    location: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="City, District, or Region (e.g., 'Tamghas, Gulmi')",
    )

    welfare_officer_contact: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
        doc="Contact info/phone of the assigned prison welfare officer",
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        doc="Flag to indicate whether the facility is actively participating in Purnava",
    )
    admins: Mapped[List["User"]] = relationship(
        "User",
        back_populates="facility"
    )