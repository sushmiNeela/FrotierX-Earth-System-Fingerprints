from pathlib import Path
import rasterio
def load_geotiff(path: str):
    """Load the first band of a GeoTIFF and return data + metadata."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    with rasterio.open(file_path) as src:
        data = src.read(1)
        metadata = {
            "crs": str(src.crs),
            "width": src.width,
            "height": src.height,
            "resolution": src.res,
            "dtype": src.dtypes[0],
            "nodata": src.nodata,
        }
    return data, metadata
