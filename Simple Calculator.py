import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operation == "Add":
            result.set(f"Result: {num1 + num2}")
        elif operation == "Subtract":
            result.set(f"Result: {num1 - num2}")
        elif operation == "Multiply":
            result.set(f"Result: {num1 * num2}")
        elif operation == "Divide":
            if num2 == 0:
                result.set("Division by zero error")
            else:
                result.set(f"Result: {num1 / num2}")
    except ValueError:
        result.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and place entry fields
entry_num1 = tk.Entry(root, width=20)
entry_num1.pack()

entry_num2 = tk.Entry(root, width=20)
entry_num2.pack()

# Create and place buttons for operations
add_button = tk.Button(root, text="Add", command=lambda: calculate("Add"))
add_button.pack()

subtract_button = tk.Button(root, text="Subtract", command=lambda: calculate("Subtract"))
subtract_button.pack()

multiply_button = tk.Button(root, text="Multiply", command=lambda: calculate("Multiply"))
multiply_button.pack()

divide_button = tk.Button(root, text="Divide", command=lambda: calculate("Divide"))
divide_button.pack()

# Create and place a label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

# Run the GUI application
root.mainloop()
