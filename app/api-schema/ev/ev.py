from pydantic import BaseModel, Field
from typing import Optional

class EV(BaseModel):
    """Definition of an Electric Vehicle (static metadata)."""

    id: str = Field(
        ...,
        description="Unique identifier of the EV (UUID or fleet-specific ID)."
    )

    vin: Optional[str] = Field(
        None,
        description="Vehicle Identification Number."
    )

    model: Optional[str] = Field(
        None,
        description="Vehicle model name or type."
    )

    make: Optional[str] = Field(
        None,
        description="Manufacturer of the EV."
    )

    battery_cap: float = Field(
        ...,
        gt=0.0,
        description="Nominal battery capacity in kWh."
    )

    obc_max_power: float = Field(
        ...,
        gt=0.0,
        description="On-board charger maximum power in kW."
    )

    building_id: Optional[str] = Field(
        None,
        description="Identifier of the building/depot where this EV is normally located."
    )

    owner_id: Optional[str] = Field(
        None,
        description="Identifier of the owning 2user."
    )
