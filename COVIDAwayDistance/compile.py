from COVIDAwayDistance.DistanceComparison import *
from COVIDAwayDistance.ParseSQLite import *

# Convert any coords to places
# Sample performed with Washington DC, the coordinates of the place would be here in terms of LAT, LONG
coordinates = (38.89511, -77.03637)
originName = reverseGeocode(coordinates)
destinationName = "San Francisco, CA"

# Takes State, Country as input
# Takes State, Country for destination (retrieved from DB)
#res = distance(originName, destinationName)
#print(res['distance in kilometers'])

#----------------------------------#

# Parse SQLite DB
# this is where the column for the destinations goes
destinationNames = ["Roseville, CA", "Sacramento, CA", "New York, NY"]

# Store all destinations in kilometers
destinationResults = []
for x in destinationNames:
    res = distance(originName, x)
    destinationResults.append([res['destination'], res['distance in kilometers']])

destinationResults = sorted(destinationResults, key=lambda x: x[1], reverse=False)

# This is the closest place
print(destinationResults[0])





