import uuid
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import ARRAY, CheckConstraint, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base, TimeStampMixin

if TYPE_CHECKING:
    from app.models.facility import Facility
    from app.models.payout import PayoutLedger
    from app.models.product import Product


class Prisoner(Base, TimeStampMixin, kw_only=True):
    __tablename__ = "prisoners"

    __table_args__ = (
        CheckConstraint(
            "length(trim(display_code)) > 0",
            name="check_prisoner_display_code_not_empty",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        doc="Primary key UUID for internal referencing",
    )
    facility_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("facilities.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        doc="Foreign key pointing to the managing correctional facility",
    )
    display_code: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        doc="Public anonymized code or approved name (e.g., 'Artisan #402')",
    )
    skill_tags: Mapped[Optional[List[str]]] = mapped_column(
        ARRAY(String(50)),
        nullable=True,
        doc="Array of artisan skills (e.g., ['Woodworking', 'Weaving'])",
    )
    impact_story: Mapped[Optional["ImpactStory"]] = relationship(
        "ImpactStory",
        back_populates="prisoner",
        uselist=False,
        cascade="all, delete-orphan",
    )

    facility: Mapped["Facility"] = relationship(
        "Facility",
        back_populates="prisoners",
    )

    products: Mapped[List["Product"]] = relationship(
        "Product",
        back_populates="prisoner",
        cascade="all, delete-orphan",
    )

    payout_ledgers: Mapped[List["PayoutLedger"]] = relationship(
        "PayoutLedger",
        back_populates="prisoner",
    )