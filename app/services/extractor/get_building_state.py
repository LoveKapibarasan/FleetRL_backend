import numpy as np
from typing import Dict, Any, Tuple

def get_building_state(payload: Dict[str, Any]) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    building = payload.get("building")
    if building:
        load = np.array([building["load"]], dtype=np.float32)
        pv = np.array([building["pv"]], dtype=np.float32)
        grid_connection = np.array([building["grid_connection"]], dtype=np.float32)
    else:
        load, pv, grid_connection = np.zeros(1), np.zeros(1), np.zeros(1)
    return load, pv, grid_connection