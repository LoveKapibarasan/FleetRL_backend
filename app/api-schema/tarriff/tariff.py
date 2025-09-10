from pydantic import BaseModel, Field
from typing import Optional

class Tariff(BaseModel):
    """Definition of a tariff contract (static metadata)."""

    id: str = Field(
        ...,
        description="Unique identifier for the tariff."
    )

    name: Optional[str] = Field(
        None,
        description="Human-readable name of the tariff (e.g., Standard Plan A)."
    )

    provider: Optional[str] = Field(
        None,
        description="Electricity provider name."
    )

    currency: str = Field(
        default="EUR",
        description="Currency code, e.g., EUR, USD, JPY."
    )

    unit: str = Field(
        default="€/MWh",
        description="Unit of the tariff (€/MWh, €/kWh)."
    )

    owner_id: Optional[str] = Field(
        None,
        description="Organization or user owning this tariff contract."
    )
