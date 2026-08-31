from sqlalchemy import CheckConstraint,String,Float,Boolean
from sqlalchemy.orm import relationship,Mapped,mapped_column
from app.db.database import Base, TimeStampMixin
import uuid
from sqlalchemy.dialects.postgresql import JSONB
from typing import Dict,Any,Optional
from sqlalchemy import Numeric,Float
from decimal import Decimal