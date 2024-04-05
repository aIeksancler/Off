import tkinter as tk
import subprocess

def start_shutdown():
    try:
        global remaining_time, countdown_id
        minutes = int(entry.get())
        remaining_time = minutes * 60
        update_countdown()
        shutdown_button.config(command=cancel_shutdown, text="Cancel")
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Enter minutes to shutdown")
        root.focus_set()

def cancel_shutdown():
    global remaining_time
    shutdown_button.config(text="Start", command=start_shutdown)
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, "Enter minutes to shutdown")
    root.after_cancel(countdown_id)
    root.focus_set()

def update_countdown():
    global remaining_time, countdown_id
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, "Shutdown in: {:02d}:{:02d}".format(minutes, seconds))
    entry.config(state="disabled")
    if remaining_time > 0:
        remaining_time -= 1
        countdown_id = root.after(1000, update_countdown)
    else:
        shutdown_button.config(text="Bye!")
        subprocess.run(["shutdown", "/s", "/t", "0"])

def select_entry_text(event):
    entry.select_range(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Off")
root.geometry("200x70")
root.resizable(False, False)

# Create entry widget
entry = tk.Entry(root, width=100, justify="center", state="normal")
entry.pack(pady=5)
entry.insert(0, "Enter minutes to shutdown")
entry.bind("<FocusIn>", select_entry_text)
entry.bind("<Return>", lambda event: start_shutdown())

# Create shutdown button
shutdown_button = tk.Button(root, text="Start", command=start_shutdown)
shutdown_button.pack(pady=5)

# Run the application
root.mainloop()
