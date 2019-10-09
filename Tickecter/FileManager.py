import pandas as pd

class FileManager:

    def __init__(self):
        CL = pd.read_csv("././Ticketer/CardList.csv")
        UL = pd.read_csv("././Ticketer/UserList.csv")
        ML = pd.read_csv("././Ticketer/MovieList.csv")
        RL = pd.read_csv("././Ticketer/ReservationList.csv")
