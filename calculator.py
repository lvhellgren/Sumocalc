# Class implementing calculations
class Calculator:
    def __init__(self):
        pass

    def calculate(self, request, response):
        print('Calculator.calculate method')
        print(request)

        response.set_sun_rise('08:12:34')
        response.set_sun_set('17:50:05')
        response.set_moon_rise('20:49:15')
        response.set_moon_set('06:22:24')
