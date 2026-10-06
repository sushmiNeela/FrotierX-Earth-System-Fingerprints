import argparse
import rasterio
def main():
    parser = argparse.ArgumentParser(
        description="Inspect a NASA GeoTIFF dataset"
    )
    parser.add_argument("file", help="Path to the GeoTIFF file")
    args = parser.parse_args()

    with rasterio.open(args.file) as src:
        data = src.read(1)

        print("=== NASA GeoTIFF Information ===")
        print("CRS:", src.crs)
        print("Resolution:", src.res)
        print("Width:", src.width)
        print("Height:", src.height)
        print("Data type:", src.dtypes[0])
        print("NoData:", src.nodata)
        print("Raw minimum:", data.min())
        print("Raw maximum:", data.max())
      
if __name__ == "__main__":
    main()
