# 1) import the necessary libraries:

# 1a) Importing 'argparse' for parsing command-line arguments. Allows to run the script from the command line.
import argparse

# 1b) Importing 'requests' for making HTTP requests and calling the Open-Meteo API.
import requests

# 1c) Importing 'datetime' function from the 'datetime' library. It will be used to validate date formats. Ensures consistency of input dates.
from datetime import datetime

# 2) Defines the Open-Meteo API URL as a constant. It is easier to replace later, avoids duplication and improves readibility.
OPEN_METEO_BASE_URL = "https://api.open-meteo.com/v1/forecast"

# 3) Function to validate date input has the correct format.
def validate_date(date_str: str) -> str:
    """
    Validate date format YYYY-MM-DD.
    Returns the same string if valid, raises error otherwise.
    """
    try:
    #3a) 'datetime.strptime()' checks that the input given has the correct format "%Y-%m-%-d".
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    #3b) If error, it returns a text error.
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

def build_api_params(latitude, longitude, start_date, end_date):
    """
    Build query parameters for Open-Meteo API
    """

    return {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "windspeed_10m_max"
        ],
        "timezone": "UTC"
    }

def fetch_weather_data(params: dict) -> dict:
    """
    Call Open-Meteo API and return JSON response.
    """

    response = requests.get(OPEN_METEO_BASE_URL, params=params)

    if response.status_code() != 200:
        raise RuntimeError(
            f"Open-Meteo API request failed "
            f"with status {response.status_code}: {response.text}"
        )
    
    return response.json()

def main():
    args = parse_arguments()

    print("Starting weather ingesttion with parameters:")
    print(vars(args))

    params = build_api_params(
        latitude = args.latitude,
        longitude = args.longitude,
        start_date = args.start_date,
        end_date = args.end_date
    )

    weather_json = fetch_weather_data(params)

    print("API call successful.")
    print("Top-level keys in response:", weather_json.keys())

if __name__ == "__main__":
    main()