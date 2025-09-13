import numpy as np
from typing import Dict, Any, Tuple

def get_user_inputs(payload: Dict[str, Any]) -> np.ndarray:
    user_inputs = payload.get("user_inputs", [])
    return np.array([ui["hours_left"] for ui in user_inputs], dtype=np.float32)