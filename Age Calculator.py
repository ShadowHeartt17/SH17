import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_ages():
    try:
        # Get the entered DOB
        if dob_entry.get():
            dob = datetime.strptime(dob_entry.get(), "%Y-%m-%d")
        else:
            messagebox.showerror("Invalid Input", "Please enter your date of birth (DOB).")
            return

        # Get the current date
        current_date = datetime.today()

        # Calculate current age
        current_age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))

        # Get the selected future year from the dropdown
        future_year = int(year_var.get())

        # Ensure the selected future year is after the current year
        if future_year <= current_date.year:
            messagebox.showerror("Invalid Year", "Please choose a future year.")
            return

        # Calculate age in the selected future year
        future_date = datetime(future_year, dob.month, dob.day)
        future_age = future_year - dob.year - ((future_date.month, future_date.day) < (dob.month, dob.day))

        # Display results
        result_label.config(text=f"Current Age: {current_age}\nAge in {future_year}: {future_age}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date in the format YYYY-MM-DD.")

# Set up the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x350")
root.config(bg="#f0f0f0")

# Create a sleek rounded "Calculate Age" button
def style_button(btn):
    btn.config(bg="#4CAF50", fg="white", font=("Arial", 14), relief="flat", height=2, width=15, bd=0, 
               activebackground="#45a049", activeforeground="white", padx=10)

# Label for instruction
instruction_label = tk.Label(root, text="Enter your Date of Birth (DOB) and choose a future year:", 
                             font=("Arial", 12), bg="#f0f0f0")
instruction_label.pack(pady=10)

# DOB Entry
dob_label = tk.Label(root, text="Enter DOB (YYYY-MM-DD):", font=("Arial", 10), bg="#f0f0f0")
dob_label.pack(pady=5)

dob_entry = tk.Entry(root, font=("Arial", 12))
dob_entry.pack(pady=5)

# Year Selection Dropdown (future years 2024–2100)
year_var = tk.StringVar(root)
year_var.set("2025")  # Default value

year_dropdown = tk.OptionMenu(root, year_var, *[str(year) for year in range(2024, 2101)])
year_dropdown.config(font=("Arial", 12), width=10)
year_dropdown.pack(pady=10)

# Calculate Button
calc_button = tk.Button(root, text="Calculate Ages", command=calculate_ages)
style_button(calc_button)
calc_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
result_label.pack(pady=5)

# Start the main loop
root.mainloop()
