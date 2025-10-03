import requests
from model.flight_model import Flight

class FlightChecker:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = "https://api.flightapi.io/onewaytrip"
        
    def check_flight_availability(self, flight: Flight):
        response = requests.get(
            f"{self.url}/{self.api_key}/"
            f"{flight.departure_airport_code}/"
            f"{flight.arrival_airport_code}/"
            f"{flight.departure_date}/"
            f"{flight.number_of_adults}/"
            f"{flight.number_of_children}/0/"
            f"{flight.cabin_class}/USD"
        )

        if response.status_code != 200:
            return {"error": f"API request failed with status {response.status_code}"}

        data = response.json()
        flights_data = []

        # Optional carriers mapping
        carriers_map = {}
        if "carriers" in data:
            for carrier in data["carriers"]:
                carriers_map[carrier["id"]] = carrier.get("name", "")

        # Extract itineraries
        for itinerary in data.get("itineraries", []):
            cheapest_price = itinerary.get("cheapest_price", {}).get("amount", None)

            for option in itinerary.get("pricing_options", []):
                for item in option.get("items", []):
                    url = item.get("url", "")
                    if "flight|" in url:
                        parts = url.split("flight|")[1:]
                        for p in parts:
                            flight_info = p.split("|")
                            if len(flight_info) >= 7:
                                carrier_id = flight_info[0]
                                flight_number = flight_info[1]
                                origin = flight_info[2]
                                departure = flight_info[3]
                                destination = flight_info[4]
                                arrival = flight_info[5]

                                flights_data.append({
                                    "price": cheapest_price,
                                    "carrier_id": carrier_id,
                                    "carrier_name": carriers_map.get(int(carrier_id), "Unknown"),
                                    "flight_number": flight_number,
                                    "origin": origin,
                                    "departure": departure,
                                    "destination": destination,
                                    "arrival": arrival
                                })
                                

        if not flights_data:
            return []
        
        # Sort by price and return top 5
        sorted_flights = sorted(flights_data, key=lambda x: x["price"] if x["price"] else float('inf'))
        return sorted_flights[:5]
