from COVIDAwayDistance.DistanceComparison import *
from COVIDAwayDistance.ParseSQLite import *

# Convert any coords to places
# Sample performed with Washington DC, the coordinates of the place would be here in terms of LAT, LONG
coordinates = (38.89511, -77.03637)
originName = reverseGeocode(coordinates)
destinationName = "San Francisco, CA"

# Takes State, Country as input
# Takes State, Country for destination (retrieved from DB)
res = distance(originName, destinationName)
print(res['distance in kilometers'])

#----------------------------------#

# Parse SQLite DB



