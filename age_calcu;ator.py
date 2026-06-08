import tkinter as tk
from datetime import date
def calculate_age():
    try:
        name = name_entry.get()
        day = int(date_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        today = date.today()
        age = today.year - year
        if (today.month, today.day) < (month, day):
            age -= 1
        result_label.config(
            text=f"Hello {name}! You are {age} years old."
        )
    except ValueError:
        result_label.config(text="Please enter valid values.")
window = tk.Tk()
window.title("Age Calculator App")
window.geometry("400x400")
heading = tk.Label(
    window,
    text="Age Calculator",
    font=("Arial", 16, "bold")
)
heading.grid(row=0, column=0, columnspan=2, pady=10)
name_label = tk.Label(window, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(window)
name_entry.grid(row=1, column=1, padx=10, pady=5)
date_label = tk.Label(window, text="Date:")
date_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
date_entry = tk.Entry(window)
date_entry.grid(row=2, column=1, padx=10, pady=5)
month_label = tk.Label(window, text="Month:")
month_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
month_entry = tk.Entry(window)
month_entry.grid(row=3, column=1, padx=10, pady=5)
year_label = tk.Label(window, text="Year:")
year_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
year_entry = tk.Entry(window)
year_entry.grid(row=4, column=1, padx=10, pady=5)
calculate_button = tk.Button(
    window,
    text="Calculate Age",
    command=calculate_age
)
calculate_button.grid(row=5, column=0, columnspan=2, pady=15)
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.grid(row=6, column=0, columnspan=2, pady=10)
window.mainloop()