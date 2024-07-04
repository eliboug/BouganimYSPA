def julian_day_to_gmst(jdn):
    # 2451545 is the Julian day number of 2000 at midnight, so subtract to figure out the number of days since then
    d = jdn - 2451545
    # current gmst in hours
    gmst_hours = 18.697374558 + 24.06570982441908 * d
    # where we are in the cycle
    gmst_hours = gmst_hours % 24
    return gmst_hours


def gmst_to_lst(gmst_hours, longitude):
    # convert time zones
    lst_hours = gmst_hours + (longitude/15)
    # define lst with a range of (0,24 hrs)
    lst_hours = lst_hours % 24
    return lst_hours

# sexagesimal conversion implemented from first PSet
def hours_to_hms(hrs):
        final_hr = int(hrs)
        final_min = (hrs % 1) * 60
        final_sec = (final_min) % 1 * 60
        final_min = int(final_min)
        final_sec = int(final_sec)
        return final_hr, final_min, final_sec

# user inputs: 
longitude = float(input("Enter the longitude of the location in decimal degrees (be sure to include negative sign for western longitudes): "))
jdn = float(input("Enter the Julian Day Number: "))

gmst_hours = julian_day_to_gmst(jdn)
lst_hours = gmst_to_lst(gmst_hours, longitude)
lst_h, lst_m, lst_s = hours_to_hms(lst_hours)
print(f"LST: {lst_h}h {lst_m}m {lst_s:.2f}s")
