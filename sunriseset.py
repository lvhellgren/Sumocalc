
import calendar
import math
from datetime import datetime, date

#  https://edwilliams.org/sunrise_sunset_algorithm.htm

def log(s, v):
    # print(f'{s}:{v}')
    pass

def time_hh_mm(t) :
    if t < 0:
        t += 24
    elif t > 24:
        t -= 24
    log('time', t)
    hh = math.floor(t)
    mm = math.floor((t - hh) * 60)

    return f'{hh}:{mm}'

def sun_rise_set(date, lat, lon, sunrise):
    # zenith = 90.8333 # Compensated value for refraction at horizonzenith
    zenith = 90
    rad = math.pi / 180
    deg = 180 / math.pi

    date_obj = datetime.strptime(date, '%m/%d/%Y')
    log('date', date_obj)
    log('latitude', lat)
    log('longitude', lon)

    days_in_year = 365 + (1 if calendar.isleap(date_obj.year) else 0)
    log('days_in_year', days_in_year)

    day_of_year = date_obj.timetuple().tm_yday
    log('day_of_year', day_of_year)

    # Approximate times
    lon_hour = lon / 15
    log('lon_hour', lon_hour)
    time_offset = 6 if sunrise else 18
    time_est = day_of_year + (time_offset - lon_hour) / 24
    log('time_est', time_est)

    # Sun's mean anamoly
    m = 0.9856 * time_est - 3.289

    # Sun's true longitude
    sun_lon = m + (1.916 * math.sin(m * rad)) + (0.020 * math.sin(2 * m * rad)) + 282.634
    if sun_lon > 360:
        sun_lon -= 360
    elif sun_lon < 0:
        sun_lon += 360
    log('sun_lon', time_est)

    # Sun's right ascension
    r_ascension = math.atan(0.91764 * math.tan(sun_lon * rad)) * deg
    log('r_ascension', r_ascension)

    # Place r_ascension in the same quadrant as sun_lon
    sun_lon_quad = math.floor(sun_lon / 90) * 90
    r_a_quad = math.floor(r_ascension / 90) * 90
    r_ascension = r_ascension + sun_lon_quad - r_a_quad

    # Convert r_ascension into hours
    r_ascension /= 15
    log('r_ascension', r_ascension)

    # The sun's declination
    sin_dec = 0.39782 * math.sin(sun_lon * rad)
    cos_dec = math.cos(math.asin(sin_dec * rad))
    log('cos_dec', cos_dec)

    # The sun's local hour angle
    cos_h = (math.cos(zenith * rad) - (sin_dec * math.sin(lat * rad))) / (cos_dec * math.cos(lat * rad))
    # print(f'cos_h {cos_h}')
    log('cos_h', cos_h)

    hours = (360 - math.acos(cos_h) * deg) if sunrise else math.acos(cos_h) * deg
    hours /= 15
    # print(f'hours {hours}')
    log('hours', hours)

    # Local mean time
    m_time = hours + r_ascension - 0.06571 * time_est - 6.622
    # print(f'm_time {m_time}')
    log('m_time', m_time)

    # UTC time
    utc = m_time - lon_hour
    log('utc', utc)

    # Convert to local time
    local_time = utc -8
    # print(f'local_time {local_time}')
    log('local_time', local_time)

    return local_time

date = "12/04/2021"
latitude = 34.0522
longitude = -118.2437
# latitude = 44
# longitude = 100

sunrise = sun_rise_set(date, latitude, longitude, True)
print(f'*** Sunrise: {time_hh_mm(sunrise)}')

sunset = sun_rise_set(date, latitude, longitude, False)
print(f'*** Sunset: {time_hh_mm(sunset)}')
