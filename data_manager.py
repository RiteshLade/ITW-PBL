
# FLIGHT DEAL FINDER

import requests
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/e629599160fc8fdcc5c5e66da4b778ae/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def dump_spreadsheet(self, call_sheety: bool = False) -> list:

        if call_sheety:
            # print("sheety call")
            url = SHEETY_PRICES_ENDPOINT
            response = requests.get(url=url)
            # print(response.text)
            response.raise_for_status()
            data = response.json()["prices"]
        else:
            data = [{"city": "Paris", "iataCode": "PAR", "lowestPrice": 1200, "id": 2},
                    {"city": "Berlin", "iataCode": "BER", "lowestPrice": 42, "id": 3},
                    {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 485, "id": 4},
                    {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 551, "id": 5},
                    {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 95, "id": 6},
                    {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 414, "id": 7},
                    {"city": "New York", "iataCode": "NYC", "lowestPrice": 240, "id": 8},
                    {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 260, "id": 9},
                    {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 378, "id": 10},
                    {"city": "Bali", "iataCode": "DPS", "lowestPrice": 501, "id": 11}]
        return data


    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )

            print(response.text)


