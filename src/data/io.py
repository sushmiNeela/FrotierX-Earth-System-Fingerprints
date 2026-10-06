from pathlib import Path
from typing import Tuple

import numpy as np
import rasterio


def load_geotiff(path: str) -> Tuple[np.ndarray, dict]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with rasterio.open(file_path) as src:
        data = src.read(1)
        profile = src.profile.copy()

    return data, profile
