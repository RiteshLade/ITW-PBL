import requests

from flight_data import FlightData

TEQUILA_API_KEY = "v4D5pzWoXtoDoKkALKkH4ucN2PufPor8"
TEQUILA_END_POINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        headers = {
            "apikey": TEQUILA_API_KEY,
            "term": city_name,
        }
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_END_POINT}/locations/query", headers=headers, params=query)
        code = response.json()["locations"][0]["code"]
        return code

    def search_for_flights(self, fly_from, fly_to, date_from, date_to, return_from, return_to,):
        headers = {
            "apikey": TEQUILA_API_KEY,
        }
        query = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "return_from": return_from,
            "return_to": return_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=f"{TEQUILA_END_POINT}/v2/search", headers=headers, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {fly_to}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            stop_over=1,
            via_city=data["route"][0]["cityTo"]
        )
        print(f"{flight_data.destination_city}: ₹{flight_data.price * 97.61}")
        return flight_data
