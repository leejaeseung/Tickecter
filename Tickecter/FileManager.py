import pandas as pd

class FileManager:

    def __init__(self):
        CL = pd.read_csv("../CardList.csv",dtype=str)
        UL = pd.read_csv("../UserList.csv",dtype=str)
        ML = pd.read_csv("../MovieList.csv",dtype=str)
        RL = pd.read_csv("../ReservationList.csv",dtype=str)

        # 카드리스트 카드번호를 키로 딕셔너리
        self.cardlist = dict([(a, b) for a,b in zip(CL.cardnum, CL.regist)])

        #유저리스트 아이디를 키로 딕셔너리
        self.userlist = dict([(userID,{"userpassword":password,"registcard":cardnum,"mileage":mileage})
                         for userID, password, cardnum, mileage in zip(UL.userID, UL.userpassword, UL.registcard,UL.mileage)])

        #영화일정리스트 이차원 리스트
        self.movielist = [(day,moviecode,moviename,starttime,finishtime,screen,seat,A,B,C,D,E,F,G,H,I,J)
                          for day, moviecode,moviename,starttime,finishtime,screen,seat,A,B,C,D,E,F,G,H,I,J
                          in zip(ML.day,ML.moviecode,ML.moviename,ML.starttime,ML.finishtime,ML.screen,ML.seat,ML.A,ML.B,ML.C,ML.D,ML.E,ML.F,ML.G,ML.H,ML.I,ML.J)]
        #예약리스트 이차원 리스트
        self.reservationlist = [(member,userID,reservationcode,seats,cancel)
                                for member,userID,reservationcode,seats,cancel in zip(RL.member,RL.userID,RL.reservationcode,RL.seats,RL.cancel)]

    def savefile(self):
        ##card
        df_cardlist = pd.DataFrame()
        df_cardlist['cardnum']= self.cardlist.keys()
        df_cardlist['regist']= self.cardlist.values()

        # user
        us_list = []
        for a,b in self.userlist.items():
            us_list.append((a,b["userpassword"],b["registcard"],b["mileage"]))
        df_userlist = pd.DataFrame(us_list)
        df_userlist.set_axis(["userID", "userpassword", "registcard", "mileage"], axis='columns', inplace=True)

        # movie
        df_movielist= pd.DataFrame(self.movielist)
        df_movielist.set_axis(["day","moviecode",'moviename','starttime','finishtime','screen','seat','A','B','C','D','E','F','G','H','I','J'],axis='columns',inplace=True)

        # reservation
        df_reservation = pd.DataFrame(self.reservationlist)
        df_reservation.set_axis(["member","userID","reservationcode","seats","cancel"],axis='columns',inplace=True)

        # 파일 저장 - 실제 작동할때는 파일명앞에 ../추가  "../CardList.csv"
        df_cardlist.to_csv("CardList.csv",header=True,index=False)
        df_userlist.to_csv("UserList.csv",header=True,index=False)
        df_movielist.to_csv("MovieList.csv",header=True,index=False)
        df_reservation.to_csv("ReservationList.csv",header=True, index=False)


    #아이디 존재 유무 리턴함수
    def dupli_checkID(self,inputID):
        if self.userlist.get(inputID,False):
            return True
        else:
            return False

    #카드 번호등록 유무 리턴 함수
    def dupli_checkCARDNUM(self,inputCARDNUM):
        if self.cardlist.get(inputCARDNUM,False):
            return True
        else:
            return False

    #좌석 str 받으면 리스트 리턴 함수


    #회원 가입(아이디,비밀번호,카드 매개로 받아 user하나 더생성)함수 //카드리스트랑 ,유저리스트 수정

    #영화예매(회원/비회원,아이디,영화 정보 ,,,좌석리스트) 받아 영화 예매 함수, 유저리스트에서 마일리지, 예약리스트


x =FileManager()
print(x.dupli_checkCARDNUM("2040111912894451"))
x.savefile()
#사용예
# x = FileManager()
# print(x.userlist["u8s0e9r"]["userpassword"])
# print(x.movielist[3][2])
# print(x.reservationlist)
# print(x.movielist)
