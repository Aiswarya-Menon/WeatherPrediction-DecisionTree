import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime
import geocoder

# Load the weather data
# Replace 'your_dataset.csv' with your actual dataset file
data = pd.read_csv('climate.csv')

# Create a decision tree classifier
X = data[['precipitation', 'temp_max', 'temp_min', 'wind']]
y = data['weather']
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Create Tkinter application
root = tk.Tk()

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width / 2) - (800 / 2)  # Assuming window width is 800
y_coordinate = (screen_height / 2) - (600 / 2)  # Assuming window height is 600

# Set the geometry of the window to center it on the screen
root.geometry("800x600+{}+{}".format(int(x_coordinate), int(y_coordinate)))

# Set the background color
root.configure(bg="#396285")
root.title("Weather Prediction and Alert System")

# Heading font
heading_font = Font(family="Helvetica", size=24, weight="bold")

# Create the heading label
heading_label = ttk.Label(root, text="Weather Prediction and Alert System",
                          font=heading_font, foreground="white", background="#396285")
heading_label.grid(row=0, column=0, columnspan=2, pady=(
    20, 10), sticky="ew")  # Add some padding to the top

# Function to predict weather


def predict_weather():
    try:
        precipitation = float(precipitation_entry.get())
        temp_max = float(temp_max_entry.get())
        temp_min = float(temp_min_entry.get())
        wind = float(wind_entry.get())

        if wind > 15:
            messagebox.showwarning(
                "Alert", "Cyclone Alert: Heavy wind \n National Disaster Response Force (NDRF): 011-26107953")
        elif precipitation > 10:
            messagebox.showwarning(
                "Alert", "Flood Alert: Heavy precipitation (cm) \n National Emergency Response Center (NERC): 011-26701728, 011-26701729")
        elif temp_max < -5:
            messagebox.showwarning(
                "Alert", "Heavy Snowfall Alert: Very Low Temperature (°C) \n Tip: Stay Away from Remote Locations")
        elif temp_min > 38:
            messagebox.showwarning(
                "Alert", "Drought Alert: Very High temperature (°C) \n Tip: Save Enough Water, don't waste it")
        else:
            prediction = clf.predict(
                [[precipitation, temp_max, temp_min, wind]])
            messagebox.showinfo(
                "Prediction", f"The predicted weather is: {prediction[0]}")
    except Exception as e:
        messagebox.showerror(
            "Error", "Please enter valid numerical values for weather parameters.")


# GUI components
label1 = ttk.Label(root, text="Precipitation:",
                   foreground="white", background="#396285")
label1.grid(row=1, column=0, padx=(50, 0), pady=5,
            sticky="e")  # Add left padding

precipitation_entry = ttk.Entry(root)
precipitation_entry.grid(row=1, column=1, padx=(0, 5), pady=5, sticky="w")

precipitation_unit_label = ttk.Label(
    root, text="cm", foreground="white", background="#396285")
precipitation_unit_label.grid(row=1, column=2, padx=(0, 0), pady=5, sticky="w")

label2 = ttk.Label(root, text="Max Temperature:",
                   foreground="white", background="#396285")
label2.grid(row=2, column=0, padx=(50, 0), pady=5,
            sticky="e")  # Add left padding

temp_max_entry = ttk.Entry(root)
temp_max_entry.grid(row=2, column=1, padx=(0, 5), pady=5,
                    sticky="w")  # Align textboxes to the left

temp_max_unit_label = ttk.Label(
    root, text="°C", foreground="white", background="#396285")
temp_max_unit_label.grid(row=2, column=2, padx=(0, 0), pady=5, sticky="w")

label3 = ttk.Label(root, text="Min Temperature:",
                   foreground="white", background="#396285")
label3.grid(row=3, column=0, padx=(50, 0), pady=5,
            sticky="e")  # Add left padding

temp_min_entry = ttk.Entry(root)
temp_min_entry.grid(row=3, column=1, padx=(0, 5), pady=5,
                    sticky="w")  # Align textboxes to the left

temp_min_unit_label = ttk.Label(
    root, text="°C", foreground="white", background="#396285")
temp_min_unit_label.grid(row=3, column=2, padx=(0, 0), pady=5, sticky="w")

label4 = ttk.Label(root, text="Wind Speed:",
                   foreground="white", background="#396285")
label4.grid(row=4, column=0, padx=(5, 0), pady=5,
            sticky="e")  # Add left padding

wind_entry = ttk.Entry(root)
wind_entry.grid(row=4, column=1, padx=(0, 5), pady=5,
                sticky="w")  # Align textboxes to the left

wind_unit_label = ttk.Label(
    root, text="mph", foreground="white", background="#396285")
wind_unit_label.grid(row=4, column=2, padx=(0, 0), pady=5,
                     sticky="w")  # Proper alignment for units

predict_button = ttk.Button(
    root, text="Predict", command=predict_weather, width=10)
predict_button.grid(row=5, column=0, columnspan=3, padx=5,
                    pady=20, sticky="ew")  # Center the button

# Get current date and time
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Get current location
location = geocoder.ip('me').city

# Create labels for date, time, and location
date_label = ttk.Label(root, text="Date: " + current_date, foreground="white",
                       font=("Helvetica", 14, "bold"), background="#396285")
date_label.grid(row=6, column=0, columnspan=3, pady=(30, 5),
                sticky="ew")  # Center align below the button

time_label = ttk.Label(root, text="Time: " + current_date, foreground="white",
                       font=("Helvetica", 14, "bold"), background="#396285")
time_label.grid(row=7, column=0, columnspan=3, pady=(5, 5),
                sticky="ew")  # Center align below the button

location_label = ttk.Label(root, text="Location: " + location,
                           foreground="white", font=("Helvetica", 14, "bold"), background="#396285")
location_label.grid(row=8, column=0, columnspan=3, pady=(
    5, 30), sticky="ew")  # Center align below the button

root.mainloop()
