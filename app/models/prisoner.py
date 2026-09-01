import uuid
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import ARRAY, CheckConstraint, DateTime, ForeignKey, String, Text
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

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        doc="Primary key UUID for internal referencing",
    )


class ImpactStory(Base):
    __tablename__ = "impact_stories"

    __table_args__ = (
        CheckConstraint(
            "length(trim(headline)) >= 5",
            name="check_impact_story_headline_length",
        ),
        CheckConstraint(
            "length(trim(narrative)) >= 20",
            name="check_impact_story_narrative_length",
        ),
        CheckConstraint(
            "length(trim(rehabilitation_goal)) >= 10",
            name="check_impact_story_goal_length",
        ),
    )

    prisoner_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("prisoners.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        index=True,
        doc="Strict 1:1 link to the Prisoner model",
    )
    prisoner: Mapped[Prisoner] = relationship(
        "Prisoner",
        back_populates="impact_story",
    )
    headline: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="Headline displayed on the story card",
    )

    narrative: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        doc="The artisan's reflections and crafting background",
    )

    rehabilitation_goal: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        doc="Specific plans for product sales earnings post-release",
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )


