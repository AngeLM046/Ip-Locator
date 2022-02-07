import requests
import json
import sys

if len(sys.argv) > 1:

    try:
        ip_addr = sys.argv[1]

        request_url = f"http://ip-api.com/json/{ip_addr}"

        response = requests.get(request_url)
        response = response.content.decode()

        result = json.loads(response)

        print(f"IP: {result['query']}\n\nCountry: {result['country']}\nCity: {result['city']}\nPostal Code: {result['zip']}\nTimezone: {result['timezone']}\nISP: {result['isp']}\nLatitude: {result['lat']}\nLongitude: {result['lon']}")

    except:
        print("Usage: python3 iplocator.py (ip)")
