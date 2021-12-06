import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.constants import DISABLED
from tkcalendar import Calendar
import request_info as req
import response_handler as res
import calculator as calc

def calculate(request_info, response_handler):
    if request_info.check_parameter_status():
        calculator = calc.Calculator()
        calculator.calculate(request_info, response_handler)

def create_param_frame(container, request_info):
    # Create the parameter frame with grid layout
    frame = ttk.LabelFrame(
        container,
        text='Parameter Settings')
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.columnconfigure(4, weight=2)

    # Create the datepicker
    today = datetime.date.today()
    cal = Calendar(frame,
        font="Arial 14",
        background='white',
        foreground='red',
        selectbackground='red',
        selectforeground='red',
        date_pattern='mm/dd/yyyy',
        cursor="hand1",
        year=today.year, month=today.month, day=today.day
    )
    cal.grid(column=0, row=0, columnspan=5)
    apply_date_button = ttk.Button(frame, text="Use This Date",
        command=lambda:[
        date.set(cal.get_date()),
        request_info.set_date(cal.get_date())
        ])
    apply_date_button.grid(column=2, row=1, pady=10, sticky='w')

    # Create the date input field

    date_label = ttk.Label(frame, text="Date:", font=('Times', 14, 'bold'))
    date_label.grid(row=3, column=1, padx=10, pady=5, sticky='w')

    date = tk.StringVar()
    date_entry = ttk.Entry(frame, width=12, textvariable=date, state=DISABLED)
    date_entry.grid(row=3, column=2, sticky='w')

    # Create the latitude input field and East/West combobox

    latitude_label = ttk.Label(frame, text="Latitude:", font=('Times', 14, 'bold'))
    latitude_label.grid(row=4, column=1, padx=10, pady=5, sticky='w')

    latitude = tk.DoubleVar()
    latitude.set(request_info.get_latitude())
    latitude_entry = ttk.Entry(frame, width=12, textvariable=latitude)
    latitude_entry.grid(row=4, column=2, sticky='w')
    latitude_entry.bind('<FocusOut>', (lambda event, lat=latitude: request_info.set_latitude(lat.get())))

    latitude_combobox = ttk.Combobox(frame, values=['N', 'S'], width=1, state='readonly')
    latitude_combobox.set(request_info.get_latitude_dir())
    latitude_combobox.grid(ipadx=3, row=4, column=3, sticky='w')
    latitude_combobox.bind('<<ComboboxSelected>>', (lambda event, cb=latitude_combobox: request_info.set_latitude_dir(cb.get())))

    # Create the longitude input field and North/South combobox

    longitude_label = ttk.Label(frame, text="Longitude:", font=('Times', 14, 'bold'))
    longitude_label.grid(row=5, column=1, padx=10, pady=5, sticky='w')

    longitude = tk.DoubleVar()
    longitude.set(request_info.get_longitude())
    longitude_entry = ttk.Entry(frame, width=12, textvariable=longitude)
    longitude_entry.grid(row=5, column=2, sticky='w')
    longitude_entry.bind('<FocusOut>', (lambda event, lng=longitude: request_info.set_longitude(lng.get())))

    longitude_combobox = ttk.Combobox(frame, values=['W', 'E'], width=1, state='readonly')
    longitude_combobox.set(request_info.get_longitude_dir())
    longitude_combobox.grid(ipadx=3, row=5, column=3, sticky='w')
    longitude_combobox.bind('<<ComboboxSelected>>', (lambda event, cb=longitude_combobox: request_info.set_longitude_dir(cb.get())))

    # Create the timezone input field and +/- combobox

    timezone_label = ttk.Label(frame, text="Timezone (h):", font=('Times', 14, 'bold'))
    timezone_label.grid(row=6, column=1, padx=10, pady=5, sticky='w')

    timezone = tk.IntVar()
    timezone.set(request_info.get_timezone())
    timezone_entry = ttk.Entry(frame, width=12, textvariable=timezone)
    timezone_entry.grid(row=6, column=2, sticky='w')
    timezone_entry.bind('<FocusOut>', (lambda event, alt=timezone: request_info.set_timezone(alt.get())))

    timezone_combobox = ttk.Combobox(frame, values=['-', '+'], width=1, state='readonly')
    timezone_combobox.set(request_info.get_timezone_sign())
    timezone_combobox.grid(ipadx=3, row=6, column=3, sticky='w')
    timezone_combobox.bind('<<ComboboxSelected>>', (lambda event, cb=timezone_combobox: request_info.set_timezone_sign(cb.get())))

    return frame

def create_results_frame(container, response_handler):
    # Create the resultes frame with grid layout
    frame = ttk.LabelFrame(
        container,
        text='Calculated Times')
    frame.columnconfigure(0, weight=1) 
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.columnconfigure(4, weight=1)

    # Create the times header row

    body_label = ttk.Label(frame, text="Body", font=('Times', 14, 'bold'))
    body_label.grid(row=0, column=1, pady=5)
    rise_label = ttk.Label(frame, text="Rise Time", font=('Times', 14, 'bold'))
    rise_label.grid(row=0, column=2, pady=5)

    set_label = ttk.Label(frame, text="Set Time", font=('Times', 14, 'bold'))
    set_label.grid(row=0, column=3, pady=5)

    # Create the Sun row

    sun_label = ttk.Label(frame, text="Sun")
    sun_label.grid(row=1, column=1, pady=5, sticky='w')

    sun_rise_entry = ttk.Entry(frame, width=10, textvariable=response_handler.sun_rise)
    sun_rise_entry.grid(row=1, column=2)

    sun_set_entry = ttk.Entry(frame, width=10, textvariable=response_handler.sun_set)
    sun_set_entry.grid(row=1, column=3)
    
    # Create the Moon row
    
    moon_label = ttk.Label(frame, text="Moon")
    moon_label.grid(row=2, column=1, pady=5, sticky='w')

    moon_rise_entry = ttk.Entry(frame, width=10, textvariable=response_handler.moon_rise)
    moon_rise_entry.grid(row=2, column=2)

    moon_set_entry = ttk.Entry(frame, width=10, textvariable=response_handler.moon_set)
    moon_set_entry.grid(row=2, column=3)

    return frame

def create_main_window():
    root = tk.Tk()
    root.title('Sumocalc')
    # root.resizable(0, 0)

    # Define the window dimensions and position the window on the screen
    window_width = 400
    window_height = 760
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/3 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Create application description
    image = tk.PhotoImage(file='./assets/sumo_icon_xs.png')
    description_label = ttk.Label(root,
        image=(image),
        compound='left',
        text='Sun and Moon - Rise and Set Times Calculator')
    description_label.pack(pady=15)

    # Request and response UI control objects
    request_info = req.RequestInfo()
    response_handler = res.ResponseHandler()


    # Create the input parameter frame
    param_frame = create_param_frame(root, request_info)
    param_frame.pack(pady=15, ipady=5, fill='x')

    # Create the calculate button
    calc_button = ttk.Button(root,
        text='Calculate',
        command=lambda: calculate(request_info, response_handler)
    )
    calc_button.pack(pady=10)

    # Create the output results frame
    results_frame = create_results_frame(root, response_handler)
    results_frame.pack(pady=15, ipady=5, fill='x')

    # Create exit button (The lambda construct allows function code to be defined directly in 
    # the command assignment.)
    exit_button = ttk.Button(
        root,
        text='Exit',
        command=lambda: root.quit()
    )
    exit_button.pack(pady=15)

    # Start the application and wait for and react to user input events
    root.mainloop()

# Verify that this file is the actual program being executed
if __name__ == "__main__":
    create_main_window()