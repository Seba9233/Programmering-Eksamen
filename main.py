import tkinter as tk


def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Quiz vindue")

    label = tk.Label(new_window, text="Der her er quiz vinduet", width=70, height=20)
    label.pack()


# Create the main window
root = tk.Tk()
root.geometry("300x300")

# Create a button widget
button = tk.Button(root, text="Quiz start", command=open_new_window, width=20, height=5)

# Add the button to the main window
button.pack()

# Start the Tkinter event loop
root.mainloop()
