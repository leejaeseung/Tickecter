import pandas as pd

class FileManager:

    def __init__(self):
        CL = pd.read_csv("../CardList.csv")
        UL = pd.read_csv("../UserList.csv")
        ML = pd.read_csv("../MovieList.csv")
        RL = pd.read_csv("../ReservationList.csv")

        # 카드리스트 dir으로
        self.cardlist = dict([(a, b) for a,b in zip(CL.cardnum, CL.regist)])

        #유저리스트 아이디를 키로 dir
        self.userlist = dict([(userID,{"password":password,"registcard":cardnum,"mileage":mileage})
                         for userID, password, cardnum, mileage in zip(UL.userID, UL.userpassword, UL.registcard,UL.mileage)])

        #영화일정리스트 이차원 리스트
        self.movielist = [(day,moviecode,moviename,starttime,finishtime,screen,seat,[A,B,C,D,E,F,G,H,I,J])
                          for day, moviecode,moviename,starttime,finishtime,screen,seat,A,B,C,D,E,F,G,H,I,J
                          in zip(ML.day,ML.moviecode,ML.moviename,ML.starttime,ML.finishtime,ML.screen,ML.seat,ML.A,ML.B,ML.C,ML.D,ML.E,ML.F,ML.G,ML.H,ML.I,ML.J)]
        self.reservationlist = [(member,userID,reservationcode,seats,cancel)
                                for member,userID,reservationcode,seats,cancel in zip(RL.member,RL.userID,RL.reservationcode,RL.seats,RL.cancel)]



x = FileManager()
print(x.reservationlist)
print(x.movielist)
