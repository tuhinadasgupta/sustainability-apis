# API: https://www.notion.so/Trip-to-Carbon-API-REFERENCE-a68cfb4e0dcc41f9826cba1f3e4af5ac
import requests
import json
# input: number of miles
#USA
def carbon_slc_nyc(activity, mode, fuel):
    type_ = 'miles'
    country = 'usa'
    url = f'https://api.triptocarbon.xyz/v1/footprint?activity={activity}&activityType={type_}&country={country}&mode={mode}&fueltype={fuel}'
    response = requests.get(url)
    info = response.json()
    carbon = str(list(info.values()))
    return carbon

def main():
    distance = 50
    mode = 'petrolCar'
    fuel = 'motorGasoline'
    carbon_footprint = carbon_slc_nyc(distance, mode, fuel)
    print(carbon_footprint)

if __name__ == "__main__":
    main()
