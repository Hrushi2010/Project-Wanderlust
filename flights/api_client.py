# api_client.py
import requests
from django.conf import settings

def create_search_session(origin, destination, departure_date, return_date):
    url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'
    headers = {'x-api-key': settings.SKYSCANNER_API_KEY}
    data = {
        "query": {
            "market": "US",
            "locale": "en-US",
            "currency": "USD",
            "query_legs": [
                {
                    "origin_place_id": {"iata": origin},
                    "destination_place_id": {"iata": destination},
                    "date": {"year": int(departure_date[:4]), "month": int(departure_date[5:7]), "day": int(departure_date[8:10])}
                }
            ],
            "adults": 1,
            "cabin_class": "CABIN_CLASS_ECONOMY"
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json().get('sessionToken')

def poll_search_results(session_token):
    url = f'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/poll/{session_token}'
    headers = {'x-api-key': settings.SKYSCANNER_API_KEY}
    response = requests.post(url, headers=headers)
    return response.json()
