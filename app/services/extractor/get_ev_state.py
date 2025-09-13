import numpy as np
from typing import Dict, Any, Tuple


def get_ev_state(payload: Dict[str, Any]) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    ev_states = payload.get("evs", [])
    soc = np.array([ev["soc"] for ev in ev_states], dtype=np.float32)
    target_soc = np.array([ev["target_soc"] for ev in ev_states], dtype=np.float32)
    battery_cap = np.array([ev["battery_cap"] for ev in ev_states], dtype=np.float32)
    obc_max_power = np.array([ev["obc_max_power"] for ev in ev_states], dtype=np.float32)
    return soc, target_soc, battery_cap, obc_max_power







def get_misc(payload: Dict[str, Any]) -> np.ndarray:
    misc = payload.get("misc", {})
    return np.array([misc.get("ambient_temp", 20.0)], dtype=np.float32)
