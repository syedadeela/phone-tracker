import phonenumbers
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

from myphone import number  # Assuming this file contains the phone number

# Parse the phone number
parsed_number = phonenumbers.parse(number, "IN")

# Get country name and code
country_name = geocoder.country_name_for_number(parsed_number, "en")
country_code = phonenumbers.region_code_for_number(parsed_number)

# Print country information
print("Country Name:", country_name)
print("Country Code:", country_code)

# Get location
location = geocoder.description_for_number(parsed_number, "en")
print("Location:", location)

# Get service provider
service_provider = carrier.name_for_number(parsed_number, "en")
print("Service Provider:", service_provider)

# Initialize OpenCageGeocode with API key
api_key = '4966a1a0c0b343b7a288e9ca87b19c3f'
geocoder = OpenCageGeocode(api_key)

# Geocode the location
results = geocoder.geocode(location)

# Filter out locations not matching the country of interest
filtered_results = [result for result in results if result.get('components', {}).get('country_code') == country_code]

# Print geocoded locations
for result in filtered_results:
    # Extract relevant location information
    city = result.get('city', '')
    state = result.get('state', '')
    country = result['components']['country']
    formatted_address = result['formatted']

    # Print exact location including city and state
    print("Geocoded Location:", f"{city}, {state}, {country} - {formatted_address}")

lat = results[0] ['geometry']['lat']
lng = results [0]['geometry']['lng']
print (lat,lng)
myMap = folium.Map(location =[lat,lng], zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("Mylocation.html")
