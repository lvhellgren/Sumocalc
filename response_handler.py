import tkinter as tk

# Class for holding response fields
class ResponseHandler:
    def __init__(self):
        self.sun_rise = tk.StringVar()
        self.sun_set = tk.StringVar()
        self.moon_rise = tk.StringVar()
        self.moon_set = tk.StringVar()

    def set_sun_rise(self, time):
        self.sun_rise.set(time)
    
    def set_sun_set(self, time):
        self.sun_set.set(time)

    def set_moon_rise(self, time):
        self.moon_rise.set(time)
    
    def set_moon_set(self, time):
        self.moon_set.set(time)