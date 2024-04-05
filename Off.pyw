import tkinter as tk
import subprocess

def start_shutdown():
    try:
        global remaining_time
        minutes = int(entry.get())
        remaining_time = minutes * 60
        update_countdown()
        shutdown_button.config(state="disabled")
        cancel_button.config(state="normal")
    except ValueError:
        label.config(text="Please enter a valid number of minutes")

def cancel_shutdown():
    global remaining_time
    remaining_time = 0
    update_countdown()
    shutdown_button.config(state="normal")
    cancel_button.config(state="disabled")

def update_countdown():
    global remaining_time
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    countdown_label.config(text="Shutdown in: {:02d}:{:02d}".format(minutes, seconds))
    if remaining_time > 0:
        remaining_time -= 1
        root.after(1000, update_countdown)
    else:
        subprocess.run(["shutdown", "/s", "/t", "0"])

def select_entry_text(event):
    entry.select_range(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Off")
root.geometry("200x120")
root.resizable(False, False)

# Create entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
entry.insert(0, "Enter minutes to shutdown")
entry.bind("<FocusIn>", select_entry_text)

# Create shutdown button
shutdown_button = tk.Button(root, text="Start", command=start_shutdown)
shutdown_button.pack(pady=5)

# Create cancel button
cancel_button = tk.Button(root, text="Cancel", command=cancel_shutdown, state="disabled")
cancel_button.pack(pady=5)

# Create countdown label
countdown_label = tk.Label(root, text="")
countdown_label.pack(pady=5)

# Create label to display messages
label = tk.Label(root, text="")
label.pack(pady=5)

# Run the application
root.mainloop()
