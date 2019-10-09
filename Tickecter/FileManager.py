import pandas as pd

class FileManager:

    def __init__(self):
        CL = pd.read_csv("././CardList.csv")
        UL = pd.read_csv("././UserList.csv")
        ML = pd.read_csv("././MovieList.csv")
        #RL = pd.read_csv("././ReservationList.csv")
