from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class TariffState(BaseModel):
    """Time-dependent tariff values."""

    tariff_id: str = Field(
        ...,
        description="Reference to Tariff.id."
    )

    timestamp: datetime = Field(
        ...,
        description="Start time of the tariff validity."
    )

    values: List[float] = Field(
        ...,
        description="Tariff values for the lookahead horizon."
    )
