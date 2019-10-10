import pandas as pd

class FileManager:

    def __init__(self):
        CL = pd.read_csv("../CardList.csv")
        UL = pd.read_csv("../UserList.csv")
        ML = pd.read_csv("../MovieList.csv")
        #RL = pd.read_csv("../ReservationList.csv")

        # 카드리스트 dic으로
        self.cardlist = dict([(a, b) for a,b in zip(CL.cardnum, CL.regist)])

        #유저리스트 아이디를 키로
        self.userlist = dict([(userID,{"password":password,"registcard":cardnum,"mileage":mileage})
                         for userID, password, cardnum, mileage in zip(UL.userID, UL.userpassword, UL.registcard,UL.mileage)])
        self.movielist = []

x = FileManager()
print(x.userlist)
