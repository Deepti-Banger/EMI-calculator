import tkinter as tk
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title("EMI Calculator")

# Create a frame for layout
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Adding widgets
loan_amount_label = ttk.Label(frame, text="Loan Amount ($):")
loan_amount_label.grid(row=0, column=0, sticky=tk.W)
loan_amount_entry = ttk.Entry(frame, width=25)
loan_amount_entry.grid(row=0, column=1)

interest_rate_label = ttk.Label(frame, text="Annual Interest Rate (%):")
interest_rate_label.grid(row=1, column=0, sticky=tk.W)
interest_rate_entry = ttk.Entry(frame, width=25)
interest_rate_entry.grid(row=1, column=1)

loan_duration_label = ttk.Label(frame, text="Loan Duration (years):")
loan_duration_label.grid(row=2, column=0, sticky=tk.W)
loan_duration_entry = ttk.Entry(frame, width=25)
loan_duration_entry.grid(row=2, column=1)

# Define the calculate_emi function before creating the button that uses it
def calculate_emi():
    try:
        P = float(loan_amount_entry.get())
        r = float(interest_rate_entry.get()) / 100 / 12
        n = int(loan_duration_entry.get()) * 12
        if r == 0:  # Simple case to avoid division by zero
            emi = P / n
        else:
            emi = P * r * ((1 + r)**n) / (((1 + r)**n) - 1)
        total_payment = emi * n
        emi_result_label.config(text=f"Monthly EMI: ${emi:.2f}")
        total_payment_label.config(text=f"Total Payment: ${total_payment:.2f}")
    except ValueError:
        emi_result_label.config(text="Please enter valid numbers")
        total_payment_label.config(text="")

# Calculate button that uses the calculate_emi function
calculate_button = ttk.Button(frame, text="Calculate EMI", command=calculate_emi)
calculate_button.grid(row=3, column=0, columnspan=2)

# Results labels
emi_result_label = ttk.Label(frame, text="")
emi_result_label.grid(row=4, column=0, columnspan=2)
total_payment_label = ttk.Label(frame, text="")
total_payment_label.grid(row=5, column=0, columnspan=2)

# Start the application loop
root.mainloop()
