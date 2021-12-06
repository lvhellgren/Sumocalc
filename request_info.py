from tkinter import messagebox

# Class for holding and validating request parameters
class RequestInfo:
    def __init__(self):
        # The leading underscores in variable names is a Python convention
        # for indicating 'private' class members
        self._date = ''
        self._latitude = 34.4208
        self._latitude_dir = 'N'
        self._longitude = 119.6982
        self._longitude_dir = 'W'
        self._timezone = 8
        self._timezone_sign = '-'

    # Used for printing the object content
    def __str__(self):
        return f'''RequestInfo(
            {'Date:'} {self._date}
            {'Latitude:'} {self._latitude}, {self._latitude_dir}
            {'Longitude:'} {self._longitude}, {self._longitude_dir})
            {'Timezone:'} {self._timezone})'''

    def _build_msg(self, msg, sub_msg):
        if len(msg) > 0:
            msg += '\n'
        msg += sub_msg

        return msg

    # Checks request parameters for completenes
    def check_parameter_status(self):
        msg = ''
        if len(self._date) == 0:
            msg = self._build_msg(msg, '- Please select a date from the calendar')
        
        if not (self._latitude >= 0 and  self._latitude <= 90):
            msg = self._build_msg(msg, '- Latidude value must be 0 - 90')
        
        if not (self._longitude >= 0 and  self._longitude <= 180):
             msg = self._build_msg(msg, '- Longitude value must be 0 - 180')
        
        if self._timezone < -12 or self._timezone > 12:
             msg = self._build_msg(msg, '- Timezone value must be 0 - 12')
        
        status = True
        print(msg)
        if len(msg) > 0:
            status = False
            messagebox.showerror('Error', msg)

        return status

    # The rest is for setting and getting the request parameters
    #
    def set_date(self, date):
        self._date = date

    def get_date(self):
        return self._date

    def set_latitude(self, latitude):
        self._latitude = latitude

    def get_latitude(self):
        return self._latitude

    def set_latitude_dir(self, latitude_dir):
        self._latitude_dir = latitude_dir

    def get_latitude_dir(self):
        return self._latitude_dir

    def set_longitude(self, longitude):
        self._longitude = longitude
        
    def get_longitude(self):
        return self._longitude

    def set_longitude_dir(self, longitude_dir):
        self._longitude_dir = longitude_dir

    def get_longitude_dir(self):
        return self._longitude_dir

    def set_timezone(self, timezone):
        self._timezone = timezone

    def get_timezone(self):
        return self._timezone

    def set_timezone_sign(self, timezone_sign):
        self._timezone_sign = timezone_sign

    def get_timezone_sign(self):
        return self._timezone_sign