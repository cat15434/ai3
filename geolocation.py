import geocoder

g = geocoder.ip('me')

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="http")
location = geolocator.reverse(g.latlng)
address = location.raw['address']
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
current_city=city
current_state=state
current_country=country



location_text="You are currently in",city,state,country
