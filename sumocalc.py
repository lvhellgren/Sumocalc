import sys
import datetime

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkcalendar import Calendar, DateEntry

def log():
    print("Clicked")

def apply_date():
    print("Apply date clicked")

def create_param_frame(container):
    # Create the parameter frame with grid layout
    frame = ttk.LabelFrame(
        container,
        text='Parameter Settings')
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)

    # Create the datepicker
    today = datetime.date.today()
    cal = Calendar(frame,
        font="Arial 14",
        background='white',
        foreground='red',
        selectbackground='red',
        selectforeground='red',
        # selectmode='day',
        cursor="hand1",
        year=today.year, month=today.month, day=today.day
    )
    cal.grid(column=0, row=0, columnspan=4)
    apply_button = ttk.Button(frame, text="Use This Date", command=apply_date)
    apply_button.grid(column=0, row=1, columnspan=4, pady=10)

    # Create the date input field
    date_label = ttk.Label(frame, text="Date:", font=('Times', 14, 'bold'))
    date_label.grid(row=3, column=1, pady=5, sticky='w')
    date = tk.StringVar()
    date_entry = ttk.Entry(frame, textvariable=date)
    date_entry.grid(row=3, column=2)

    # Create the latitude input field
    latitude_label = ttk.Label(frame, text="Latitude:", font=('Times', 14, 'bold'))
    latitude_label.grid(row=4, column=1, pady=5, sticky='w')
    latitude = tk.StringVar()
    latitude_entry = ttk.Entry(frame, textvariable=latitude)
    latitude_entry.grid(row=4, column=2)

    # Create the longitude input field
    longitude_label = ttk.Label(frame, text="Longitude:", font=('Times', 14, 'bold'))
    longitude_label.grid(row=5, column=1, pady=5, sticky='w')
    longitude = tk.StringVar()
    longitude_entry = ttk.Entry(frame, textvariable=longitude)
    longitude_entry.grid(row=5, column=2)

    return frame

def create_results_frame(container):
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
    sun_label.grid(row=1, column=1, pady=5)

    sun_rize_time = tk.StringVar()
    sun_rize_entry = ttk.Entry(frame, width=10, textvariable=sun_rize_time)
    sun_rize_entry.grid(row=1, column=2)

    sun_set_time = tk.StringVar()
    sun_set_entry = ttk.Entry(frame, width=10, textvariable=sun_set_time)
    sun_set_entry.grid(row=1, column=3)
    
    # Create the Moon row
    moon_label = ttk.Label(frame, text="Moon")
    moon_label.grid(row=2, column=1, pady=5)

    moon_rize_time = tk.StringVar()
    moon_rize_entry = ttk.Entry(frame, width=10, textvariable=moon_rize_time)
    moon_rize_entry.grid(row=2, column=2)

    moon_set_time = tk.StringVar()
    moon_set_entry = ttk.Entry(frame, width=10, textvariable=moon_set_time)
    moon_set_entry.grid(row=2, column=3)

    return frame

def create_main_window():
    root = tk.Tk()
    root.title('Sumocalc')
    # root.resizable(0, 0)

    # Set the window icon (does not seem to work on MacOS, perhaps on other OSs)
    # root.iconbitmap('~/Downloads/sumo_icon.ico')

    # Define the window dimensions and center the window on the screen
    window_width = 400
    window_height = 740
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Create application description
    image = tk.PhotoImage(file='/Users/acme/UCSB/Sumocalc/assets/sumo_icon_xs.png')
    description_label = ttk.Label(root,
        image=(image),
        compound='left',
        text='Sun and Moon - Rise and Set Times Calculator')
    description_label.pack(pady=15)

    # Create the input parameter frame
    param_frame = create_param_frame(root)
    param_frame.pack(pady=15, ipady=5, fill='x')

    # Create the calculate buttonls
    calc_button = ttk.Button(root,
        text='Calculate',
        command=lambda: showinfo('Info', 'TODO')
    )
    calc_button.pack(pady=10)

    # Create the output results frame
    results_frame = create_results_frame(root)
    results_frame.pack(pady=15, ipady=5, fill='x')

    # Create exit button (The lambda construct allows function code to be defined directly in the command assignment.)
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