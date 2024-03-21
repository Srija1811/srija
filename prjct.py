import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Dummy database for storing users and reminders
users = {}

def show_frame(frame):
    frame.tkraise()

def sign_up():
    username = sign_up_username_entry.get()
    if username in users:
        messagebox.showerror("Error", "Username already exists. Please choose another one.")
        return

    password = sign_up_password_entry.get()
    dob = sign_up_dob_entry.get()
    name = sign_up_name_entry.get()
    gender = sign_up_gender_entry.get()
    cardinals = sign_up_cardinals_entry.get()

    users[username] = {'password': password, 'dob': dob, 'name': name, 'gender': gender, 'cardinals': cardinals}
    messagebox.showinfo("Success", "Sign up successful.")
    show_frame(login_frame)

def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    if username in users and users[username]['password'] == password:
        messagebox.showinfo("Success", "Login successful.")
        show_frame(add_reminder_frame)
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Function to set reminder
def set_reminder(column, time_entry):
    reminder_time = time_entry.get()
    if not reminder_time:
        messagebox.showerror("Error", "Please enter a reminder time.")
    else:
        # Parse the time string and format it
        try:
            datetime.strptime(reminder_time, "%I:%M %p")
            messagebox.showinfo("Reminder Set", f"Reminder set for {column} at {reminder_time}.")
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please use HH:MM AM/PM.")

# Create GUI
root = tk.Tk()
root.title("CUE - The Reminder")

# Frames
sign_up_frame = tk.Frame(root)
login_frame = tk.Frame(root)
add_reminder_frame = tk.Frame(root)

for frame in (sign_up_frame, login_frame, add_reminder_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# Sign Up Frame
tk.Label(sign_up_frame, text="Sign Up").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
tk.Label(sign_up_frame, text="Username:").grid(row=1, column=0, padx=10, pady=5)
sign_up_username_entry = tk.Entry(sign_up_frame)
sign_up_username_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(sign_up_frame, text="Password:").grid(row=2, column=0, padx=10, pady=5)
sign_up_password_entry = tk.Entry(sign_up_frame, show="*")
sign_up_password_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(sign_up_frame, text="Date of Birth:").grid(row=3, column=0, padx=10, pady=5)
sign_up_dob_entry = tk.Entry(sign_up_frame)
sign_up_dob_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(sign_up_frame, text="Name:").grid(row=4, column=0, padx=10, pady=5)
sign_up_name_entry = tk.Entry(sign_up_frame)
sign_up_name_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(sign_up_frame, text="Gender:").grid(row=5, column=0, padx=10, pady=5)
sign_up_gender_entry = tk.Entry(sign_up_frame)
sign_up_gender_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(sign_up_frame, text="Cardinals:").grid(row=6, column=0, padx=10, pady=5)
sign_up_cardinals_entry = tk.Entry(sign_up_frame)
sign_up_cardinals_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Button(sign_up_frame, text="Sign Up", command=sign_up).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Login Frame
tk.Label(login_frame, text="Login").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
tk.Label(login_frame, text="Username:").grid(row=1, column=0, padx=10, pady=5)
login_username_entry = tk.Entry(login_frame)
login_username_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Label(login_frame, text="Password:").grid(row=2, column=0, padx=10, pady=5)
login_password_entry = tk.Entry(login_frame, show="*")
login_password_entry.grid(row=2, column=1, padx=10, pady=5)
tk.Button(login_frame, text="Login", command=login).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Add Reminder Frame
tk.Label(add_reminder_frame, text="Add Reminder").grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Function to create reminder buttons
def create_reminder_buttons():
    columns = ["Water", "Food", "Medicine", "Reading Time", "Phone Usage", "Exercise", "Periods"]
    time_entries = []  # To store time entry widgets for reminders
    for i, column in enumerate(columns):
        tk.Label(add_reminder_frame, text=column).grid(row=i+1, column=0, padx=10, pady=5)
        time_entry = tk.Entry(add_reminder_frame)
        time_entry.grid(row=i+1, column=1, padx=10, pady=5)
        time_entries.append(time_entry)
        tk.Button(add_reminder_frame, text="Set Reminder", command=lambda c=column, t=time_entry: set_reminder(c, t)).grid(row=i+1, column=2, padx=10, pady=5)

# Create reminder buttons
create_reminder_buttons()

# Show Sign Up Frame initially
show_frame(sign_up_frame)

root.mainloop()
