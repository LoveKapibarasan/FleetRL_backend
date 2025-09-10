from pydantic import BaseModel, Field
from typing import Optional

class Building(BaseModel):
    """Definition of a building/depot (static metadata)."""

    id: str = Field(
        ...,
        description="Unique identifier for the building (UUID or external key)."
    )

    name: Optional[str] = Field(
        None,
        description="Human-readable name of the building (e.g., Depot A, HQ)."
    )

    address: Optional[str] = Field(
        None,
        description="Physical address of the building."
    )

    latitude: Optional[float] = Field(
        None,
        description="Geographic latitude of the building location."
    )

    longitude: Optional[float] = Field(
        None,
        description="Geographic longitude of the building location."
    )

    grid_connection: Optional[float] = Field(
        None,
        gt=0.0,
        description="Maximum grid connection capacity [kW]."
    )

    owner_id: Optional[str] = Field(
        None,
        description="Identifier of the owning organization or user."
    )
