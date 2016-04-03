import urllib

#-------------------------------------------------------------------------------
# Setup options
#-------------------------------------------------------------------------------
# Image folders
day_imgs = "/Users/themapsmith/Documents/GitHub/firef.ly-maps/images/day/"
night_imgs = "/Users/themapsmith/Documents/GitHub/firef.ly-maps/images/night/"

# Static API settings
account = "https://api.mapbox.com/styles/v1/fireflyexperience/"
day = "cim27fdrx007g9jkpxusgx7r1/static/"
night = "cim2js1e5009w9jm0ie7wgg3r/static/"
resolution = "100x100@2x"
token = "?access_token=pk.eyJ1IjoiZmlyZWZseWV4cGVyaWVuY2UiLCJhIjoiY2lta2p0YnRiMDEycHUxa3Framc4ZHg2ZyJ9.2AMqMUQxPWtnqXrh-U8hxg"
# This is a public token that only has static:fetch scope
options = "&attribution=false&logo=false"
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Start fetching images
#-------------------------------------------------------------------------------

# Country
country = "9.971556,51.341059,4.00,0.00,0.00/"
urllib.urlretrieve(account + day + country + resolution + token + options, day_imgs + "country.png")
urllib.urlretrieve(account + night + country + resolution + token + options, night_imgs + "country.png")
print "Country images retrieved"

# States
state = "-120.174354,43.818989,4.00,0.00,0.00/"
urllib.urlretrieve(account + day + state + resolution + token + options, day_imgs + "state.png")
urllib.urlretrieve(account + night + state + resolution + token + options, night_imgs + "state.png")
print "State images retrieved"

# Cities - Large
city_lg = "151.272174,-34.079067,5.00,0.00,0.00/"
urllib.urlretrieve(account + day + city_lg + resolution + token + options, day_imgs + "city-lg.png")
urllib.urlretrieve(account + night + city_lg + resolution + token + options, night_imgs + "city-lg.png")
print "Large city images retrieved"

# Cities - Small
city_sm = "42.623828,11.877477,5.00,0.00,0.00/"
urllib.urlretrieve(account + day + city_sm + resolution + token + options, day_imgs + "city-sm.png")
urllib.urlretrieve(account + night + city_sm + resolution + token + options, night_imgs + "city-sm.png")
print "Small city images retrieved"

# Town
town = "-90.150851,38.625037,11.00,0.00,0.00/"
urllib.urlretrieve(account + day + town + resolution + token + options, day_imgs + "town.png")
urllib.urlretrieve(account + night + town + resolution + token + options, night_imgs + "town.png")
print "Town images retrieved"

# Village
village = "101.744348,3.101172,12.00,0.00,0.00/"
urllib.urlretrieve(account + day + village + resolution + token + options, day_imgs + "village.png")
urllib.urlretrieve(account + night + village + resolution + token + options, night_imgs + "village.png")
print "Village images retrieved"

# Hamlet
hamlet = "-74.173392,4.712831,12.00,0.00,0.00/"
urllib.urlretrieve(account + day + hamlet + resolution + token + options, day_imgs + "hamlet.png")
urllib.urlretrieve(account + night + hamlet + resolution + token + options, night_imgs + "hamlet.png")
print "Hamlet images retrieved"

# Suburb
suburb = "-73.948659,40.652251,10.00,0.00,0.00/"
urllib.urlretrieve(account + day + suburb + resolution + token + options, day_imgs + "suburb.png")
urllib.urlretrieve(account + night + suburb + resolution + token + options, night_imgs + "suburb.png")
print "Suburb images retrieved"

# Neighborhood
neighborhood = "80.291387,13.118309,13.00,0.00,0.00/"
urllib.urlretrieve(account + day + neighborhood + resolution + token + options, day_imgs + "neighborhood.png")
urllib.urlretrieve(account + night + neighborhood + resolution + token + options, night_imgs + "neighborhood.png")
print "Neighborhood images retrieved"

# Road
road = "-97.729313,30.287957,14.00,0.00,0.00/"
urllib.urlretrieve(account + day + road + resolution + token + options, day_imgs + "road.png")
urllib.urlretrieve(account + night + road + resolution + token + options, night_imgs + "road.png")
print "Road images retrieved"

# Shields
shields = "-96.640450,33.173372,12.00,0.00,0.00/"
urllib.urlretrieve(account + day + shields + resolution + token + options, day_imgs + "shields.png")
urllib.urlretrieve(account + night + shields + resolution + token + options, night_imgs + "shields.png")
print "Shield images retrieved"

# Shields
water = "-0.078383,51.506421,15.00,0.00,0.00/"
urllib.urlretrieve(account + day + water + resolution + token + options, day_imgs + "water.png")
urllib.urlretrieve(account + night + water + resolution + token + options, night_imgs + "water.png")
print "Water images retrieved"
