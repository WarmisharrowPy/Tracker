import phonenumbers

number = #Number you want to search with the pincode.

Key = #get your key

from phonenumbers import geocoder
samNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)