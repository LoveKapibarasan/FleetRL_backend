from pydantic import BaseModel, Field
from typing import Optional

class UserInput(BaseModel):
    """User-provided constraints or control flags for an EV session."""

    id: str = Field(
        ...,
        description="Unique identifier for this input entry (external key)."
    )

    ev_id: str = Field(
        ...,
        description="Identifier of the EV to which this input applies."
    )

    user_id: str = Field(
        ...,
        description="Identifier of the user who submitted this input."
    )

    hours_left: float = Field(
        ...,
        ge=0.0,
        description="Remaining time plugged in (hours)."
    )

    abort_charge: bool = Field(
        default=False,
        description="Flag to abort charging immediately."
    )

    force_charge: bool = Field(
        default=False,
        description="Flag to force charging regardless of optimization."
    )

    priority_level: Optional[int] = Field(
        default=0,
        ge=0,
        description="Charging priority level (0=normal, higher=more priority)."
    )
