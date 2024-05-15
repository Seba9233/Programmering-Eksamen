import tkinter as tk

def open_new_window():
    # Hide the main window
    root.withdraw()

    # Create the new window
    new_window = tk.Toplevel(root)
    new_window.title("Quiz vindue")

    # Label in the new window
    label = tk.Label(new_window, text="Det her er quiz vinduet", width=70, height=5)
    label.pack()

    # Three buttons in the new window
    button1 = tk.Button(new_window, text="Button 1", width=20, height=2, bg='blue')
    button1.pack(pady=5)  # Add space below each button

    button2 = tk.Button(new_window, text="Button 2", width=20, height=2, bg='red')
    button2.pack(pady=5)  # Add space below each button

    button3 = tk.Button(new_window, text="Button 3", width=20, height=2, bg='yellow')
    button3.pack(pady=5)  # Add space below each button

    # Destroy the main window when the new window is closed
    new_window.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

# Create the main window
root = tk.Tk()
root.geometry("300x200")

# Create a button widget
button = tk.Button(root, text="Quiz start", command=open_new_window, width=30, height=5, bg='#3c88cf')

# Add the button to the main window
button.pack()

# Start the Tkinter event loop
root.mainloop()
