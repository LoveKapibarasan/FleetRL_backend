from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    """Definition of a system user."""

    id: str = Field(
        ...,
        description="Unique identifier for the user (primary key or external reference)."
    )

    name: str = Field(
        ...,
        description="Full name of the user."
    )

    email: Optional[EmailStr] = Field(
        None,
        description="Contact email address of the user."
    )

    role: str = Field(
        ...,
        description="Role of the user (e.g., driver, operator, admin)."
    )

    organization_id: Optional[str] = Field(
        None,
        description="External key linking the user to an organization or company."
    )