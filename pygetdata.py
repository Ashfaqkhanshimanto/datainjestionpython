import requests
import json


response = requests.get("https://restcountries.com/v3.1/all")

if response.status_code == 200:
    countries_data = response.json()
else:
    print("Failed to retrieve data")


countries_list = []

for country in countries_data:
    country_info = {
        "name": country.get("name", {}).get("common", ""),
        "capital": country.get("capital", [""])[0],
        "region": country.get("region", ""),
        "subregion": country.get("subregion", "")
    }
    countries_list.append(country_info)


with open("countries.json", "w") as json_file:
    json.dump(countries_list, json_file, indent=4)
