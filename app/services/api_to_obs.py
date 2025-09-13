iimport numpy as np
from typing import Dict, Any

from app.api_schema import (
    EVState,
    UserInput,
    BuildingState,
    TariffAdjustment,
    Miscellaneous,
)


def api_to_obs(payload: Dict[str, Any]) -> Dict[str, np.ndarray]:
    """
    Convert API payload into FleetEnv-compatible observation dict.
    """

    # --- EV state ---
    ev_states = payload.get("evs", [])
    soc = np.array([ev["soc"] for ev in ev_states], dtype=np.float32)
    target_soc = np.array([ev["target_soc"] for ev in ev_states], dtype=np.float32)
    battery_cap = np.array([ev["battery_cap"] for ev in ev_states], dtype=np.float32)
    obc_max_power = np.array([ev["obc_max_power"] for ev in ev_states], dtype=np.float32)

    # --- User inputs ---
    user_inputs = payload.get("user_inputs", [])
    hours_left = np.array([ui["hours_left"] for ui in user_inputs], dtype=np.float32)

    # --- Building state ---
    building = payload.get("building")
    load = np.array([building["load"]], dtype=np.float32) if building else np.zeros(1)
    pv = np.array([building["pv"]], dtype=np.float32) if building else np.zeros(1)
    grid_connection = (
        np.array([building["grid_connection"]], dtype=np.float32) if building else np.zeros(1)
    )

    # --- Tariff / Price ---
    tariff = payload.get("tariff", {})
    price = np.array([tariff.get("spot_price", 0.0)], dtype=np.float32)
    tariff_val = np.array([tariff.get("tariff_price", 0.0)], dtype=np.float32)

    # --- Misc features ---
    misc = payload.get("misc", {})
    ambient_temp = np.array([misc.get("ambient_temp", 20.0)], dtype=np.float32)

    # --- obs dict for FleetEnv ---
    obs = {
        "soc": soc,
        "target_soc": target_soc,
        "battery_cap": battery_cap,
        "obc_max_power": obc_max_power,
        "hours_left": hours_left,
        "price": price,
        "tariff": tariff_val,
        "load": load,
        "pv": pv,
        "grid_connection": grid_connection,
        "ambient_temp": ambient_temp,
    }

    return obs
