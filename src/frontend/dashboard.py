import tkinter as tk
from backend.dashboard_backend import DashboardBackend

dashboardBackend = DashboardBackend()

class Dashboard():

    def __init__(self, size: str, title: str):
        self.__size: str = size
        self.__title: str = title

    def turn(self) -> None:
        dashboardBackend.rotation()

    def frame_settings(self) -> None:
        """Diese methode erstellt und setzt die einstellung für unser Frame"""
        self.root = tk.Tk()
        self.root.geometry(self.__size)
        self.root.title(self.__title)
        self.root.config(bg="black")

        self.item()

        self.root.mainloop()

    def item(self) -> None:
        title = tk.Label(text="Dashboard", font=("Arial", 16, "bold"), bg="black", fg="white")
        title.pack()

        counter = tk.Label(text="0", bg="black", fg="white", font=("Arial", 20, "bold"))
        counter.pack(expand=True)

        drop = tk.Button(text="Drop", font=("Arial", 16, "bold"), bg="green", fg="white", command=self.turn)
        drop.pack(expand=True, pady=60)