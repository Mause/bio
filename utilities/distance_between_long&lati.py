#!/usr/bin/env python
import math


def GetLatitudeLongitudeProximity(fromlati, fromlong, tolati, tolong):
    """finds the approximate distance in miles between
    the given pair of latititude and longitude values"""

    # The approximate number of miles per degree of latitude.
    # Once we have the difference in degrees, we will use this
    # to find an approximate horizontal distance.
    MilesPerLatitude = 69.09

    # Calculate the distance in degrees between the two
    # different latitude / longitude locations.
    DegreeDistance = math.degrees(
        math.acos((
            math.sin(math.radians(fromlati)) *
            math.sin(math.radians(tolati))
            )
        +
        (
            math.cos(math.radians(fromlati)) *
            math.cos(math.radians(tolati)) *
            math.cos(math.radians(tolong - fromlong))
            )
        ))
    # Given the difference in degrees, return the approximate
    # distance in miles. Round
    return (DegreeDistance * MilesPerLatitude)

x = GetLatitudeLongitudeProximity(
    -33.955463, 115.07271,
    -33.958469, 115.07094)

print (x * 1609.344) - 372.10456273584219


# >>> 0.3721045627358422*1000
# 372.10456273584219



# <cffunction
#     name="DegreesToRadians"
#     access="public"
#     returntype="numeric"
#     output="false"
#     hint="I convert degrees to radians.">
 
#     <!--- Define arguments. --->
#     <cfargument
#         name="Degrees"
#         type="numeric"
#         required="true"
#         hint="I am the degree value to be converted to radians."
#         />
 
#     <!--- Return converted value. --->
#     <cfreturn (ARGUMENTS.Degrees * Pi() / 180) />
# </cffunction>
 
 
# <cffunction
#     name="RadiansToDegrees"
#     access="public"
#     returntype="numeric"
#     output="false"
#     hint="I convert radians to degrees.">
 
#     <!--- Define arguments. --->
#     <cfargument
#         name="Radians"
#         type="numeric"
#         required="true"
#         hint="I am the radian value to be converted to degrees."
#         />
 
#     <!--- Return converted value. --->
#     <cfreturn (ARGUMENTS.Radians * 180 / Pi()) />
# </cffunction>
# For Cut-and-Paste

