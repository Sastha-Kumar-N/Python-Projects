import tkinter as tk
from tkinter import filedialog

def replace_head1():
    custom_input = custom_input_entry.get()
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip().startswith("<!--**Head1-->"):
                # Add the <a> element before the custom input line
                file.write('<a class="h2 m-0 text-white text-uppercase font-weight-bold" href="">')
                file.write(custom_input)
                file.write('</a>\n')
            else:
                file.write(line)

    result_label.config(text="Replacement done!")

def browse_file():
    global file_path
    file_path = filedialog.askopenfilename()
    file_path_label.config(text=file_path)

# Create the main window
window = tk.Tk()
window.title("HTML File Content Replacer")

# Create and configure widgets
file_path_label = tk.Label(window, text="Select an HTML file:")
file_path_label.pack()

browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack()

custom_input_label = tk.Label(window, text="Custom Input:")
custom_input_label.pack()

custom_input_entry = tk.Entry(window)
custom_input_entry.pack()

replace_button = tk.Button(window, text="Replace", command=replace_head1)
replace_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI main loop
window.mainloop()
