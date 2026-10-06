import argparse

import numpy as np
import rasterio


NDVI_SCALE_FACTOR = 0.0001


def main():
    parser = argparse.ArgumentParser(
        description="Inspect a NASA MOD13A3 NDVI GeoTIFF."
    )

    parser.add_argument(
        "file",
        help="Path to the NDVI GeoTIFF file"
    )

    args = parser.parse_args()

    with rasterio.open(args.file) as src:
        data = src.read(1)

        nodata = src.nodata

        # Remove NoData pixels
        if nodata is not None:
            valid = data[data != nodata]
        else:
            valid = data

        # Convert raw NDVI to physical NDVI values
        ndvi = valid.astype(np.float32) * NDVI_SCALE_FACTOR

        print("=== NASA MOD13A3 NDVI ===")
        print("CRS:", src.crs)
        print("Resolution:", src.res)
        print("Width:", src.width)
        print("Height:", src.height)
        print("Data type:", src.dtypes[0])
        print("NoData:", nodata)

        print("\n=== Valid NDVI Statistics ===")
        print("Valid pixels:", valid.size)
        print("Raw minimum:", valid.min())
        print("Raw maximum:", valid.max())

        print("\n=== Scaled NDVI ===")
        print("NDVI minimum:", ndvi.min())
        print("NDVI maximum:", ndvi.max())
        print("NDVI mean:", ndvi.mean())


if __name__ == "__main__":
    main()
