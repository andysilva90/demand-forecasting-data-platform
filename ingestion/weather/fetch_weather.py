import argparse
import requests
from datetime import datetime

OPEN_METEO_BASE_URL = "https://api.open-meteo.com/v1/forecast"

def validate_date(date_str: str) -> str:
    """
    Validate date format YYYY-MM-DD.
    Returns the same string if valid, raises error otherwise.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}. Expected YYYY-MM-DD")
    
def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Fetch daily weather data from Open-Meteo")

    parser.add_argument("--latitude", type=float, required=True, help="Latitude of the location")
    parser.add_argument("--longitude", type=float, required=True, help="Longitude of the location")
    parser.add_argument("--start-date", type=validate_date, required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", type=validate_date, required=True, help="End date (YYYY-MM-DD)")

    return parser.parse_args()