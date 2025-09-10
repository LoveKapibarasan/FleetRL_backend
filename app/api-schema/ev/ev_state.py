from pydantic import BaseModel, Field
from typing import Optional

class EVState(BaseModel):
    """Single EV state description used in API requests/responses."""

    soc: float = Field(..., ge=0.0, le=1.0,
                       description="State of Charge (0.0 - 1.0)")
    target_soc: float = Field(..., ge=0.0, le=1.0,
                              description="Target State of Charge (0.0 - 1.0)")
    battery_cap: float = Field(..., gt=0.0,
                               description="Battery capacity in kWh")
    obc_max_power: Optional[float] = Field(None, gt=0.0,
                                           description="On-Board Charger maximum power in kW")
