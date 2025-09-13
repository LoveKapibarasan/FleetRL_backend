from pydantic import BaseModel, Field
from typing import Optional

class TimeFeatures(BaseModel):
    month_sin: float
    month_cos: float
    week_sin: float
    week_cos: float
    hour_sin: float
    hour_cos: float

class Miscellaneous(BaseModel):
    """Miscellaneous features that can be added to observations."""

    time: Optional[TimeFeatures] = None
    ambient_temp: Optional[float] = Field(
        None,
        description="Ambient temperature in Celsius."
    )
    events_count: Optional[int] = Field(
        0,
        description="Number of events detected in current timestep."
    )
    last_event_type: Optional[str] = Field(
        None,
        description="Type of last detected event (e.g., arrival, departure, overload)."
    )
