import tkinter as tk
from tkinter import messagebox

class WeaveWorxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WeaveWorx - Subscription Management")
        self.root.geometry("400x300")

        tk.Label(root, text="WeaveWorx", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(root, text="Subscription Status: ACTIVE", fg="green", font=("Arial", 12)).pack(pady=5)

        tk.Button(root, text="Renew Subscription", command=self.renew_subscription).pack(pady=10)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    def renew_subscription(self):
        messagebox.showinfo("Renew", "Redirecting to Payment...")

root = tk.Tk()
app = WeaveWorxApp(root)
root.mainloop()
