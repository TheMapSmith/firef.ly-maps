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
country = "-120.174354,43.818989,4.00,0.00,0.00/"
urllib.urlretrieve(account + day + country + resolution + token + options, day_imgs + "state.png")
urllib.urlretrieve(account + night + country + resolution + token + options, night_imgs + "state.png")
print "State images retrieved"
