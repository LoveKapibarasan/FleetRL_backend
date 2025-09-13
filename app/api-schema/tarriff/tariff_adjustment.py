class TariffAdjustment(BaseModel):
    spot_markup: Optional[float] = Field(
        None, description="Fixed markup on spot price [€/kWh]"
        )
    spot_mul: Optional[float] = Field(
        None, description="Multiplier on spot price (1+X)"
        )
    feed_in_ded: Optional[float] = Field(
        None, ge=0.0, le=1.0,
        description="Deduction rate on feed-in tariff (0-1)"
        )
