import os

import requests
from dotenv import load_dotenv


# NASA AppEEARS API endpoint
API_URL = "https://appeears.earthdatacloud.nasa.gov/api/"


def login_to_appeears():
    """
    Authenticate with NASA AppEEARS and return a Bearer token.
    """

    load_dotenv()

    username = os.getenv("APPEEARS_USERNAME")
    password = os.getenv("APPEEARS_PASSWORD")

    if not username or not password:
        raise RuntimeError(
            "NASA Earthdata credentials not found. "
            "Check your local .env file."
        )

    response = requests.post(
        f"{API_URL}login",
        auth=(username, password),
        data={"grant_type": "client_credentials"},
        timeout=60,
    )

    response.raise_for_status()

    token = response.json().get("token")

    if not token:
        raise RuntimeError("AppEEARS did not return an authentication token.")

    return token


def get_available_products(token):
    """
    Get the list of products available through AppEEARS.
    """

    response = requests.get(
        f"{API_URL}product",
        headers={
            "Authorization": f"Bearer {token}"
        },
        timeout=60,
    )

    response.raise_for_status()

    return response.json()


def show_project_products(products):
    """
    Show the NASA products used by Earth System Fingerprints.
    """

    target_products = {
        "MOD11A1.061",
        "MOD13A3.061",
        "SPL3SMP_E.006",
    }

    print("\n=== Earth System Fingerprints: NASA Products ===")

    for product in products:
        product_id = product.get("ProductAndVersion")

        if product_id in target_products:
            print(f"\nProduct: {product_id}")
            print(f"Description: {product.get('Description')}")
            print(f"Resolution: {product.get('Resolution')}")
            print(f"Source: {product.get('Source')}")


def main():
    print("Connecting to NASA AppEEARS...")

    token = login_to_appeears()

    print("Authentication successful.")

    products = get_available_products(token)

    show_project_products(products)

    print("\nPrototype completed successfully.")


if __name__ == "__main__":
    main()
