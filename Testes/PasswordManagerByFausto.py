import tkinter as tk
from tkinter import simpledialog, messagebox
from cryptography.fernet import Fernet

PASSWORDS_FILE = "stored_passwords.enc"  # Encrypted file to store passwords
KEY_FILE = "encryption_key.key"  # File to store the encryption key

try:
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()
except FileNotFoundError:
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

cipher_suite = Fernet(key)

# Load existing passwords from the file
try:
    with open(PASSWORDS_FILE, "rb") as file:
        encrypted_data = file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        passwords = eval(decrypted_data.decode())
except (FileNotFoundError, SyntaxError):
    passwords = {}


def store_password():
    service = simpledialog.askstring("Input", "Enter the service name:")
    password = simpledialog.askstring("Input", "Enter the password:")
    if service and password:
        passwords[service.lower()] = password
        save_passwords_to_file()
        messagebox.showinfo("Success", "Password stored successfully!")


def list_and_manage_passwords():
    password_list = "\n".join(f"{service}: {password}" for service, password in passwords.items())
    action = simpledialog.askstring("List",
                                    f"List of stored passwords:\n\n{password_list}\n\nEnter 'edit [service]' to edit a password, 'delete [service]' to delete a password, 'store' to add a new password, or 'cancel' to close.")

    if action:
        action_parts = action.split(" ", 1)
        if action_parts[0].lower() == "edit":
            edit_password(action_parts[1])
        elif action_parts[0].lower() == "delete":
            delete_password(action_parts[1])
        elif action_parts[0].lower() == "store":
            store_password()


def edit_password(service):
    if service.lower() in passwords:
        new_password = simpledialog.askstring("Edit Password", f"Enter the new password for {service}:")
        if new_password:
            passwords[service.lower()] = new_password
            save_passwords_to_file()
            messagebox.showinfo("Success", f"Password for {service} edited successfully!")
        else:
            messagebox.showwarning("Warning", "Password cannot be empty.")
    else:
        messagebox.showerror("Error", "Service not found.")


def delete_password(service):
    if service.lower() in passwords:
        confirm_delete = messagebox.askyesno("Confirm Deletion",
                                             f"Are you sure you want to delete the password for {service}?")
        if confirm_delete:
            del passwords[service.lower()]
            save_passwords_to_file()
            messagebox.showinfo("Success", f"Password for {service} deleted successfully!")
    else:
        messagebox.showerror("Error", "Service not found.")


def save_passwords_to_file():
    encrypted_data = cipher_suite.encrypt(str(passwords).encode())
    with open(PASSWORDS_FILE, "wb") as file:
        file.write(encrypted_data)


# GUI Setup
root = tk.Tk()
root.withdraw()  # Hide the main window

while True:
    enter = simpledialog.askstring("Password", "Enter your password (Type 'quit' to exit):")
    if enter == "METAllica1999":
        list_and_manage_passwords()
    elif enter.lower() == "quit":
        messagebox.showinfo("Goodbye", "Exiting the application.")
        save_passwords_to_file()  # Save passwords before exiting
        root.destroy()  # Close the main window
        exit()
    else:
        messagebox.showerror("Error", "Incorrect password. Please try again.")