from pydantic import BaseModel, Field
from typing import Optional, List

class BuildingState(BaseModel):
    """Building-level state including load, PV, and grid capacity."""

    id: str = Field(
        ...,
        description="Unique identifier of the building (e.g., depot_1, HQ)."
    )

    load: Optional[List[float]] = Field(
        None,
        description="Building load profile [kW]. Could be current value or lookahead series."
    )

    pv: Optional[List[float]] = Field(
        None,
        description="PV generation profile [kW]. Could be current value or lookahead series."
    )

    grid_connection: Optional[float] = Field(
        None,
        gt=0.0,
        description="Maximum grid connection capacity [kW]."
    )
