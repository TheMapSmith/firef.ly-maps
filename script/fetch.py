import urllib

#-------------------------------------------------------------------------------
# Setup options
#-------------------------------------------------------------------------------

# Directory
dir_root = "/Users/themapsmith/Documents/GitHub/firef.ly-maps/images/"
day_imgs = dir_root + "day/"
night_imgs = dir_root + "night/"

# Static API settings
account = "https://api.mapbox.com/styles/v1/fireflyexperience/"
day = "cim27fdrx007g9jkpxusgx7r1/static/"
night = "cim2js1e5009w9jm0ie7wgg3r/static/"
lc_res = "100x200@2x"
token = "?access_token=pk.eyJ1IjoiZmlyZWZseWV4cGVyaWVuY2UiLCJhIjoiY2lta2p0YnRiMDEycHUxa3Framc4ZHg2ZyJ9.2AMqMUQxPWtnqXrh-U8hxg"
# This is a public token that only has static:fetch scope
options = "&attribution=false&logo=false"

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Set image location variables
#-------------------------------------------------------------------------------

combos = {
"country" : "9.971556,51.341059,4.00,0.00,0.00/" ,
"state" : "-120.174354,43.818989,4.00,0.00,0.00/",
"city_lg" : "151.272174,-34.079067,5.00,0.00,0.00/",
"city_sm" : "42.623828,11.877477,5.00,0.00,0.00/",
"town" : "-90.150851,38.625037,11.00,0.00,0.00/",
"village" : "101.744348,3.101172,12.00,0.00,0.00/",
"hamlet" : "-74.173392,4.712831,12.00,0.00,0.00/",
"suburb" : "-73.948659,40.652251,10.00,0.00,0.00/",
"neighborhood" : "80.291387,13.118309,13.00,0.00,0.00/",
"road-typ" : "-97.729313,30.287957,14.00,0.00,0.00/",
"shields" : "-96.640450,33.173372,12.00,0.00,0.00/",
"waterway" : "-97.751371,30.264367,14.38,0.00,0.00/",
"background" : "-0.979244,26.096768,5.00,0.00,0.00/",
"water" : "-9.285127,37.592827,5.00,0.00,0.00/",
"landcover" : "16.556014,10.655762,4.00,0.00,0.00/",
"ice" : "-52.097740,66.131574,5.00,0.00,0.00/",
"park" : "-73.971931,40.770522,11.00,0.00,0.00/",
"school" : "-71.116669,42.378373,12.87,0.00,0.00/",
"airport" : "-73.785338,40.642930,12.00,0.00,0.00/",
"inst-tex" : "-118.416585,33.970035,14.00,0.00,0.00/",
"park-tex" : "-118.411778,33.958147,14.00,0.00,0.00/",
"bldg-tex" : "-118.243239,34.049500,16.35,0.00,0.00/",
"water-tex" : "0.000000,0.000000,14.00,0.00,0.00/",
"road" : "-77.028336,38.884040,12.80,0.00,0.00/",
"bldg" : "-73.990076,40.743810,16.10,0.00,0.00/"
}

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Start fetching images
#-------------------------------------------------------------------------------

for key,value in combos.iteritems():
    if key == "landcover":
        resolution = "100x200@2x"
    elif "tex" in key:
        resolution = "50x50@2x"
    else:
        resolution = "100x100@2x"

    urllib.urlretrieve(account + day + value + resolution + token + options, day_imgs + key + ".png")
    urllib.urlretrieve(account + night + value + resolution + token + options, night_imgs + key + ".png")
