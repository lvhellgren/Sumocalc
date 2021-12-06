import calendar
import math
from datetime import datetime, date

# Class implementing calculations based on NOAA General Solar Position Calculations
# https://edwilliams.org/sunrise_sunset_algorithm.htm
class Calculator:
    def __init__(self):
        pass

    def log(self, s, v):
        # print(f'{s}:{v}')
        pass

    # Converts decimal hour value to hh:mm string
    def time_hh_mm(self, t) :
        if t < 0:
            t += 24
        elif t > 24:
            t -= 24
        self.log('time', t)
        hh = math.floor(t)
        mm = math.floor((t - hh) * 60)

        if mm < 10:
            mm *= 10

        return f'{hh}:{mm}'

    # Returns UTC time for sunrise/sunset
    def sun_rise_set(self, date, lat, lon, sunrise):
        zenith = 90

        # Compensated value for refraction at horizon
        # zenith = 90.8333

        # Multiplier for converting degrees to radians
        rad = math.pi / 180

        # Multiplier for converting radians to degrees
        deg = 180 / math.pi

        # date = datetime.strptime(date, '%m/%d/%Y')
        self.log('date', date)
        self.log('latitude', lat)
        self.log('longitude', lon)

        days_in_year = 365 + (1 if calendar.isleap(date.year) else 0)
        self.log('days_in_year', days_in_year)

        day_of_year = date.timetuple().tm_yday
        self.log('day_of_year', day_of_year)

        # Approximate times
        lon_hour = lon / 15
        self.log('lon_hour', lon_hour)
        time_offset = 6 if sunrise else 18
        time_est = day_of_year + (time_offset - lon_hour) / 24
        self.log('time_est', time_est)

        # Sun's mean anamoly
        m = 0.9856 * time_est - 3.289

        # Sun's true longitude
        sun_lon = m + (1.916 * math.sin(m * rad)) + (0.020 * math.sin(2 * m * rad)) + 282.634
        if sun_lon > 360:
            sun_lon -= 360
        elif sun_lon < 0:
            sun_lon += 360
        self.log('sun_lon', time_est)

        # Sun's right ascension
        r_ascension = math.atan(0.91764 * math.tan(sun_lon * rad)) * deg
        self.log('r_ascension', r_ascension)

        # Place r_ascension in the same quadrant as sun_lon
        sun_lon_quad = math.floor(sun_lon / 90) * 90
        r_a_quad = math.floor(r_ascension / 90) * 90
        r_ascension = r_ascension + sun_lon_quad - r_a_quad

        # Convert r_ascension into hours
        r_ascension /= 15
        self.log('r_ascension', r_ascension)

        # The sun's declination
        sin_dec = 0.39782 * math.sin(sun_lon * rad)
        cos_dec = math.cos(math.asin(sin_dec * rad))
        self.log('cos_dec', cos_dec)

        # The sun's local hour angle
        cos_h = (math.cos(zenith * rad) - (sin_dec * math.sin(lat * rad))) / (cos_dec * math.cos(lat * rad))
        self.log('cos_h', cos_h)

        hours = (360 - math.acos(cos_h) * deg) if sunrise else math.acos(cos_h) * deg
        hours /= 15
        self.log('hours', hours)

        # Local mean time
        m_time = hours + r_ascension - 0.06571 * time_est - 6.622
        self.log('m_time', m_time)

        # UTC time
        utc = m_time - lon_hour
        self.log('utc', utc)

        return utc

    def calculate(self, request, response):
        date = datetime.strptime(request._date, '%m/%d/%Y')

        latitude = request.get_latitude()
        if request.get_latitude_dir() == 'S':
            latitude = - latitude

        longitude = request.get_longitude()
        if request.get_longitude_dir() == 'W':
            longitude = - longitude

        timezone = request.get_timezone()
        if request.get_timezone_sign() == '-':
            timezone = - timezone

        sunrise = self.sun_rise_set(date, latitude, longitude, True) + timezone
        response.set_sun_rise(self.time_hh_mm(sunrise))

        sunset = self.sun_rise_set(date, latitude, longitude, False) + timezone
        response.set_sun_set(self.time_hh_mm(sunset))

        response.set_moon_rise('N/A')
        response.set_moon_set('N/A')
