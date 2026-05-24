import tkinter as tk
def calculate_product():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    product = num1 * num2
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, str(product))
window = tk.Tk()
window.geometry("400x300")
window.title("Getting Started with Widgets")
description = tk.Label(
    window,
    text="This application multiplies two numbers.",
    font=("Arial", 12)
)
description.pack(pady=10)
label1 = tk.Label(window, text="Enter first number:")
label1.pack()
label2 = tk.Label(window, text="Enter second number:")
label2.pack()
entry1 = tk.Entry(window)
entry1.pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack(pady=5)
button = tk.Button(
    window,
    text="Calculate Product",
    command=calculate_product
)
button.pack(pady=10)
result_box = tk.Text(window, height=2, width=20)
result_box.pack(pady=10)
window.mainloop()