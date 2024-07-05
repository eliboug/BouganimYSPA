from datetime import datetime, timedelta

# date to Julian Day 
def jdn(date):
    # Convert a date to Julian Day Number
    a = (14 - date.month) // 12
    y = date.year + 4800 - a
    m = date.month + 12 * a - 3
    jdn = date.day + ((153 * m + 2) // 5) + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    return jdn + (date.hour - 12) / 24.0 + date.minute / 1440.0 + date.second / 86400.0

# implemented from problem 3
def julian_day_to_gmst(jdn):
    # 2451545 is the Julian day number of 2000 at midnight, so subtract to figure out the number of days since then
    d = jdn - 2451545
    # current gmst in hours
    gmst_hours = 18.697374558 + (366.244/365.244 * 24) * d
    # where we are in the cycle
    gmst_hours = gmst_hours % 24
    return gmst_hours

# simple time zone conversion
def lst_from_gmst(gmst, longitude):
    # Longitude in degrees
    lst = gmst + (longitude / 15.0)
    lst = lst % 24
    return lst

# finding transit time 
def find_transit_time(date, longitude, ra):
    julianday = jdn(date)
    gmst = julian_day_to_gmst(julianday)
    lst = lst_from_gmst(gmst, longitude)
    # Calculate the local sidereal time at midnight
    gmst_midnight = julian_day_to_gmst(int(julianday))
    lst_midnight = lst_from_gmst(gmst_midnight, longitude)
    
    # hour angle logic
    hour_angle = (ra - lst_midnight) % 24
    # Convert transit time to datetime
    transit_datetime = datetime(date.year, date.month, date.day) + timedelta(hours=hour_angle)
    return transit_datetime

# Plug in data for given problem 
longitude = 149.0685 # longitude of Siding Springs corrected for true longitude
ra = 11.30614  # Right Ascension of 2024ggi
date = datetime(2024, 7, 5, 0, 0, 0)  # today's date (as of completion of PSet)

transit_time = find_transit_time(date, longitude, ra)
print("The object transits the local meridian at:", transit_time)
