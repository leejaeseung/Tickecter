import pandas as pd

class FileManager:

    def __init__(self):
        CL = pd.read_csv("../Tickecter/CardList.csv", dtype=str)
        UL = pd.read_csv("../Tickecter/UserList.csv", dtype=str)
        ML = pd.read_csv("../Tickecter/MovieList.csv", dtype=str)
        RL = pd.read_csv("../Tickecter/ReservationList.csv", dtype=str)

        # 카드리스트 카드번호를 키로 딕셔너리
        self.cardlist = dict([(a, b) for a, b in zip(CL.cardnum, CL.regist)])

        #유저리스트 아이디를 키로 딕셔너리
        self.userlist = dict([(userID,{"userID":userID,"userpassword": password, "registcard": cardnum, "mileage": mileage})
                         for userID, password, cardnum, mileage in zip(UL.userID, UL.userpassword, UL.registcard,UL.mileage)])

        #영화일정리스트 이차원 리스트
        self.movielist = dict([(key, [day,moviecode,moviename,starttime,finishtime,screen,seat,A,B,C,D,E,F,G,H,I,J])
                          for key, day, moviecode,moviename,starttime,finishtime,screen,seat,A,B,C,D,E,F,G,H,I,J
                          in zip(ML.day+ML.moviecode+ML.starttime,ML.day,ML.moviecode,ML.moviename,ML.starttime,ML.finishtime,ML.screen,ML.seat,ML.A,ML.B,ML.C,ML.D,ML.E,ML.F,ML.G,ML.H,ML.I,ML.J)])
        #예약리스트 이차원 리스트
        self.reservationlist = [[member,userID,reservationcode,seats,cancel]
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
        mv_list = []
        for a,b in self.movielist.items():
            mv_list.append(b)
        df_movielist= pd.DataFrame(mv_list)
        df_movielist.set_axis(["day","moviecode",'moviename','starttime','finishtime','screen','seat','A','B','C','D','E','F','G','H','I','J'],axis='columns',inplace=True)

        # reservation
        df_reservation = pd.DataFrame(self.reservationlist)
        df_reservation.set_axis(["member","userID","reservationcode","seats","cancel"],axis='columns',inplace=True)

        # 파일 저장 - 실제 작동할때는 파일명앞에 ../추가  "../CardList.csv"
        df_cardlist.to_csv("CardList.csv",header=True,index=False)
        df_userlist.to_csv("UserList.csv",header=True,index=False)
        df_movielist.to_csv("MovieList.csv",header=True,index=False)
        df_reservation.to_csv("ReservationList.csv", header=True, index=False)

        # csv는 ,로 셀을 구분.. 좌석에 ,를 사용하면?
        #좌석 번호 저장 할때 csv가 ,로 셀을 구분하여 문자열에,이 포함될경우 자동으로 ""로 묶어줌 그래서 A1~A4는 "이 포함되지 않으나 A1,A2는 "이 포함되어 저장

    #아이디 존재 유무 리턴함수
    def dupli_checkID(self,inputID):
        if self.userlist.get(inputID,False): #존재 한다면
            #함수에 따라 달라져서 그냥 둠.
            return True
        else: #존재 x
            return False

    #카드 번호등록 유무 리턴 함수
    def dupli_checkCARDNUM(self,inputCARDNUM):
        if self.cardlist.get(inputCARDNUM) == '0':
            return 0
        elif self.cardlist.get(inputCARDNUM, False) == '1':
            return 2
        else:
            return 1


    #회원 가입(아이디,비밀번호,카드 매개로 받아 user하나 더생성)함수 //카드리스트랑 ,유저리스트 수정
    def join_user(self,id,password,cardnum):
        self.userlist[id] ={"userpassword":password,"registcard":cardnum,"mileage":0}
        self.cardlist[cardnum] = str(1)

    #유저 정보 리스트 리턴함수 이 리스트의 값을 변경하면 유저 정보 변함, 마일리지적립,사용할 때 또는...
    def getuser(self,id,password):
        if self.userlist[id]["userpassword"] != password:
            return False
        else:
            return self.userlist[id]


    #날짜와 시간 입력시 그날의 그시간 이후의 영화 리스트 반환
    def day_movielist(self,day,starttime):
        daylist =[]
        for _code,movieinfo in self.movielist.items():
            if movieinfo[0] == day and int(movieinfo[3]) > int(starttime): # 상영날짜가 day인 아직 시작하지 않은 영화
                daylist.append([_code, movieinfo])  #이부분에서 _code와 movieinfo 리스트 하나로 묶는법을 잘 모르겠.
        return daylist

    # 좌석 str 받으면 리스트 리턴 함수
    def seats_to_list(self, strseat):
        if "~" in strseat:
            list = strseat.split("~")
            seatlist = []
            for i in range(int(list[0][1:]), int(list[1][1:]) + 1):
                seatlist.append(list[0][0] + str(i))
            return seatlist
        elif "," in strseat:
            list = strseat.split(",")
            return list
        else:
            list = [strseat]
            return list


    #영화예매(회원/비회원,아이디,영화 정보 ,,,좌석리스트) 받아 영화 예매 함수
    def bookmovie(self,isuser,id,choice_movie,strseat):
        seatlist =self.seats_to_list(strseat)
        self.reservationlist.append([isuser,id,choice_movie[0]+choice_movie[1]+choice_movie[3]+seatlist[0],strseat,"0"])
        for seat in seatlist:
            hori = 7 + ord(seat[0]) - ord('A')
            vert = int(seat[1:]) - 1
            choice_movie[hori] =choice_movie[hori][0:vert] + "1" + choice_movie[hori][vert + 1:]

    #아이디를 입력받으면 해당 회원의 예매 코드에 해당하는 예약 리스트들의 인덱스 리스트 리턴하는 함수 ,회원이 아닌경우 code_num을 넣으면 예약리스트의 인덱스 하나 리턴
    def getReservation(self, username="",code_num=''):  
        list=[]
        if username != '':
            for index, reserlist in enumerate(self.reservationlist):
                if reserlist[0] == '1' and reserlist[1] == username:
                    list.append(index)
            return list
        else:
            for index, reserlist in enumerate(self.reservationlist):
                if reserlist[4]=='0' and reserlist[2] == code_num:
                    return index

            
       


    #예매 코드를 입력받으면 ReservationList에서 해당 예매코드를 취소하는 함수
    def book_cancel(self,index):
        reserv= self.reservationlist[int(index)]
        if reserv[4] =='1':
            print("이미 취소 된 내역 입니다.")
            return False
        else:
            seatlist= self.seats_to_list(reserv[3])
            choice_movie =self.movielist[reserv[2][:-2]]
            reserv[4] ='1'
            for seat in seatlist:
                hori = 7 + ord(seat[0]) - ord('A')
                vert = int(seat[1:]) - 1
                choice_movie[hori] = choice_movie[hori][0:vert] + "0" + choice_movie[hori][vert + 1:]


# member, userID, reservationcode, seats, cancel


#movielist day,moviecode,moviename,starttime,finishtime,screen,seat,A,B,C,D,E,F,G,H,I,J

# 클래스 선언

x=FileManager()
#user일때
y = x.getReservation(username="user")
for index, i in enumerate(y):
    print(x.reservationlist[i])
index=input("인덱스 입력")
x.book_cancel(y[int(index)])
#비회원
# y= x.getReservation(code_num="20191020AA0710A3")
# print(x.reservationlist[y])
# x.book_cancel(y)

# movie =x.day_movielist("20191020","1710")
# print(movie)
# index =input("인덱스를 입력하시요")
# x.bookmovie("1","user",movie[int(index)][1],"A1,A2,A4")

x.savefile()

# x.savefile()

#사용예
# x = FileManager()
# print(x.userlist["u8s0e9r"]["userpassword"])
# print(x.movielist[3][2])
# print(x.reservationlist)
# print(x.movielist)
# print(x.dupli_checkCARDNUM("2040111912894451"))

#출력확인 seat_to list
# print(x.seats_to_list("A1~A4"))
# print(x.seats_to_list("A1,A4,B4"))
# print(x.seats_to_list("B3"))

#출력 테스트
# print(x.userlist)
# print(x.cardlist)
# x.join_user("aaaa","1231aa","2040430744863878")
# print(x.userlist)
# print(x.cardlist)

#유저리스트 값 변경되는지 테스트
# print(x.userlist)
# y= x.getuser("u8s0e9r","p6as8s")
# y["mileage"] ="2933"
# print(x.userlist)