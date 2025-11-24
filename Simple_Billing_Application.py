import tkinter as tk
from tkinter import messagebox

def calculate_bill():
    try:
        # Get values from entry boxes (same logic as your backend)
        p1 = float(entry_p1.get())
        q1 = int(entry_q1.get())
        p2 = float(entry_p2.get())
        q2 = int(entry_q2.get())
        p3 = float(entry_p3.get())
        q3 = int(entry_q3.get())
        off = float(entry_discount.get())

        # === Your original logic (unchanged) ===
        total_order_value = p1 * q1 + p2 * q2 + p3 * q3
        total_amount_payble_after_discount = total_order_value - (total_order_value * off / 100)
        # ======================================

        # Show results in labels
        label_total_value_result.config(
            text=f"₹{total_order_value:.2f}"
        )
        label_payable_result.config(
            text=f"₹{total_amount_payble_after_discount:.2f}"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for all fields.")


# Create main window
root = tk.Tk()
root.title("Simple Billing System")
root.geometry("500x400")

title_label = tk.Label(root, text="Billing System", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Frame for inputs
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

# Row 1 - Item 1
tk.Label(frame_inputs, text="Price of first item:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_p1 = tk.Entry(frame_inputs)
entry_p1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Quantity of first item:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
entry_q1 = tk.Entry(frame_inputs)
entry_q1.grid(row=0, column=3, padx=5, pady=5)

# Row 2 - Item 2
tk.Label(frame_inputs, text="Price of second item:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_p2 = tk.Entry(frame_inputs)
entry_p2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Quantity of second item:").grid(row=1, column=2, sticky="w", padx=5, pady=5)
entry_q2 = tk.Entry(frame_inputs)
entry_q2.grid(row=1, column=3, padx=5, pady=5)

# Row 3 - Item 3
tk.Label(frame_inputs, text="Price of third item:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_p3 = tk.Entry(frame_inputs)
entry_p3.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Quantity of third item:").grid(row=2, column=2, sticky="w", padx=5, pady=5)
entry_q3 = tk.Entry(frame_inputs)
entry_q3.grid(row=2, column=3, padx=5, pady=5)

# Discount row
tk.Label(frame_inputs, text="Discount (%):").grid(row=3, column=0, sticky="w", padx=5, pady=10)
entry_discount = tk.Entry(frame_inputs)
entry_discount.grid(row=3, column=1, padx=5, pady=10)

# Calculate button
btn_calculate = tk.Button(root, text="Calculate Bill", command=calculate_bill, font=("Arial", 12, "bold"))
btn_calculate.pack(pady=10)

# Results section
frame_results = tk.Frame(root)
frame_results.pack(pady=10)

tk.Label(frame_results, text="Total bill value:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
label_total_value_result = tk.Label(frame_results, text="₹0.00", font=("Arial", 10, "bold"))
label_total_value_result.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_results, text="Bill after discount:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
label_payable_result = tk.Label(frame_results, text="₹0.00", font=("Arial", 10, "bold"))
label_payable_result.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()