import numpy as np

def variable_raster(data,metadata):
  """ Validate basic properties of a raster dataset."""
  nodata = metadata.get("no data")
  if nodata is not None:
    valid = data[data != nodata]
    else:
        valid = data
    valid = valid[np.isfinite(valid)]
    if valid.size == 0:
        raise ValueError("No valid raster values found.")
    return {
        "crs": metadata["crs"],
        "width": metadata["width"],
        "height": metadata["height"],
        "resolution": metadata["resolution"],
        "dtype": metadata["dtype"],
        "nodata": nodata,
        "min": float(valid.min()),
        "max": float(valid.max()),
        "mean": float(valid.mean()),
        "valid_pixels": int(valid.size),
    }
