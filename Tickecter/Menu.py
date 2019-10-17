from . import FileManager, menuInfo, TypeChecker
from queue import PriorityQueue
import os
import time

class Menu:

    def __init__(self):
        print("현재 시간을 입력해 주세요.")
        self.__now_time = None
        self.__FM = FileManager.FileManager()
        self.__TC = TypeChecker.TypeChecker()
        self.MI = menuInfo.menuInfo(4100, False, 0)
        self.userName = None
        self.password = None
        self.want_reserveday = None
        self.day_movielist = None
        self.selected_movie = None
        self.final_cost = None
        self.seat_list = None
        self.seat_First = None

    def menu4100(self, input):
        assert isinstance(input, str)
        if self.__TC.time_check(input):
            self.__now_time = input
            self.print_login_menu()
            self.MI.setMI(4200, self.MI.getisMember(), 1)

    def menu4200(self, input):
        assert isinstance(input, str)
        new_input = int(input)

        if new_input == 1:
            print("ID를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
            self.MI.setMI(4211, self.MI.getisMember(), self.MI.getwhere())
        elif new_input == 2:
            print("ID를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
            self.MI.setMI(4221, self.MI.getisMember(), self.MI.getwhere())
        elif new_input == 3:
            os.system('cls')
            self.print_main_menu()
            self.MI.setMI(4300, self.MI.getisMember(), 2)
        else:
            print('입력 형식이 맞지 않습니다.')
            return -1

    def menu4211(self, input): # 로그인 메뉴-id
        # 파일 관리 클래스를 사용해 input 과 비교, if문으로 True면 다음 메뉴, False면 다시 입력받음,아이디를 잠시 저장
        assert isinstance(input, str)
        if self.__TC.ID_check(input):
            if self.__FM.dupli_checkID(input) :  # 존재하는 아이디면
                self.userName = input
                print("Password를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
                self.MI.setMI(4212, self.MI.getisMember(), self.MI.getwhere())
            else:      # 존재하지 않는 아이디면
                print("존재하지 않는 ID입니다. 다시 입력해 주세요.")
                self.MI.setMI(4211, self.MI.getisMember(), self.MI.getwhere())

    def menu4212(self, input): # 로그인 메뉴 -password
        # 파일 관리 클래스를 사용해 input 과 비교, if문으로 True면 다음 메뉴, False면 다시 입력받음, 비밀번호를 잠시 저장
        assert isinstance(input, str)
        self.password = input
        if self.__TC.pw_check(input):
            if self.__FM.userlist[self.userName]["userpassword"] == input:     # 비밀번호가 일치하면
                os.system('cls')
                self.print_main_menu()
                self.MI.setMI(4300, True, 2)
            else:         #일치하지 않으면
                print("일치하지 않는 Password입니다. 다시 입력해 주세요.")
                self.MI.setMI(4212, self.MI.getisMember(), self.MI.getwhere())

    def menu4221(self, input): # 회원 가입 메뉴- id 입력후
        # 파일 관리 클래스를 사용해 input 과 비교, if문으로 True면 다음 메뉴, False면 다시 입력받음, 아이디를 잠시 저장
        assert isinstance(input, str)
        if self.__TC.ID_check(input):
            if not self.__FM.dupli_checkID(input):     # 만들 수 있는 아이디면
                self.userName = input
                print("Password를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
                self.MI.setMI(4222, self.MI.getisMember(), self.MI.getwhere())
            else:  # 이미 존재하는 아이디면
                print("이미 존재하는 ID입니다. 다시 입력해 주세요.")
                self.MI.setMI(4221, self.MI.getisMember(), self.MI.getwhere())

    def menu4222(self, input):
        # 비밀번호를 잠시 저장
        assert isinstance(input, str)
        if self.__TC.pw_check(input):
            self.password = input
            print("등록할 카드 번호를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
            self.MI.setMI(4223, self.MI.getisMember(), self.MI.getwhere())

    def menu4223(self, input):
        assert isinstance(input, str)
        if self.__TC.cardNum(input):
            if self.__FM.dupli_checkCARDNUM(input) == 2:  # 이미 등록된 카드 번호이면
                print("이미 등록된 카드 번호입니다. 다시 입력해 주세요.")
                self.MI.setMI(4223, self.MI.getisMember(), self.MI.getwhere())
            elif self.__FM.dupli_checkCARDNUM(input) == 1:  # 존재하지 않는 카드 번호이면
                print("존재하지 않는 카드 번호입니다. 다시 입력해 주세요.")
                self.MI.setMI(4223, self.MI.getisMember(), self.MI.getwhere())
            else:  # 유효한 카드 번호이면 -> UserList를 업데이트
                self.__FM.join_user(self.userName, self.password, input)
                self.__FM.savefile()
                os.system('cls')
                self.userName = None
                self.password = None
                self.print_login_menu()
                self.MI.setMI(4200, self.MI.getisMember(), self.MI.getwhere())

    def menu4300(self, input):
        assert isinstance(input, str)
        new_input = int(input)
        if new_input == 1:
            self.print_10days()
            # 현재 날짜로부터 10일 후 까지의 달력 출력
            print("상영을 원하는 날짜를 8자리로 입력해 주세요.")
            self.MI.setMI(4311, self.MI.getisMember(), self.MI.getwhere())
        elif new_input == 2:
            if self.MI.getisMember():  # 회원이면
                # ReservationList 에서 회원의 예매 내역 출력
                self.printMovies("")
                print("취소하시려는 영화의 예매 코드를 입력해 주세요.(취소하지 않고  메인 메뉴로 돌아가시려면 “BACK”을 입력해 주세요)")
                self.MI.setMI(4322, self.MI.getisMember(), self.MI.getwhere())
            else:
                print("예매 코드를 입력해 주세요.")
                self.MI.setMI(43212, self.MI.getisMember(), self.MI.getwhere())
        # elif new_input == 3:
        # return 4300, False, 2  수정 필요
        else:
            print("입력 형식이 잘못됐습니다.")
            return -1

    def menu4311(self, input):  # 완성
        assert isinstance(input, str)
        if self.__TC.date_check(input):
            if int(input) < int(self.__now_time[0:8]):
                print("현재 날짜보다 이전 날짜입니다. 다시 입력해 주세요.")
                self.MI.setMI(4311, self.MI.getisMember(), self.MI.getwhere())
            else:
                self.want_reserveday = input
                # 상영중인 영화를 한 줄씩 출력
                if int(input) == int(self.__now_time[0:8]):  # 입력한 날짜가 현재 날짜이면 -> 현재 시간도 비교해 줘야함
                    self.day_movielist = self.__FM.day_movielist(input, self.__now_time[8:12])
                    if not self.printday_movie():
                        print("상영중인 영화가 없습니다. 다시 입력해 주세요.")
                        self.MI.setMI(4311, self.MI.getisMember(), self.MI.getwhere())
                        return
                else:
                    self.day_movielist = self.__FM.day_movielist(input, "0000")
                    if not self.printday_movie():
                        print("상영중인 영화가 없습니다. 다시 입력해 주세요.")
                        self.MI.setMI(4311, self.MI.getisMember(), self.MI.getwhere())
                        return
                print("예매할 영화를 선택하세요.(숫자.영화명 입력)")
                self.MI.setMI(4312, self.MI.getisMember(), self.MI.getwhere())

    def menu4312(self, input):
        assert isinstance(input, str)
        if self.__TC.checkMovieTitle(input):
            input = input.strip().split('.')  # 공백을 제거하고, . 을 기준으로 분리
            if self.print_seat(int(input[0]), input[1]):  # 입력한 영화가 존재할 경우
                # 선택한 영화의 좌석표를 출력
                print("예약할 좌석을 고르십시오.")
                self.MI.setMI(4313, self.MI.getisMember(), self.MI.getwhere())
            else:  # 입력한 영화가 존재하지 않을 경우
                print("존재하지 않는 영화입니다. 다시 입력해 주세요.")
                self.MI.setMI(4312, self.MI.getisMember(), self.MI.getwhere())

    def menu4313(self, input):
        assert isinstance(input, str)
        self.seat_list = input
        seat_count = self.count_seat(input)
        assert isinstance(seat_count, int)
        if self.__TC.checkyoursheet(input):
            if seat_count != -1:  # 입력한 좌석이 존재하는 경우 = 예매할 수 있는 경우
                # 결제 금액(좌석 수 x 가격)을 출력
                if int(self.selected_movie[1][3]) >= 1200:
                    cost = 10000
                else:
                    cost = 7000
                self.final_cost = seat_count * cost
                print("결제하실 금액은 총", self.final_cost, "원 입니다.")
                if self.MI.getisMember():
                    # 보유 마일리지를 출력
                    print("회원님의 마일리지 잔액은", self.__FM.getuser(self.userName, self.password).get("mileage"),
                          "원 입니다. 얼마를 사용하시겠습니까?")
                    self.MI.setMI(43141, self.MI.getisMember(), self.MI.getwhere())
                else:
                    print("결제하실 카드 번호를 입력해 주세요.")
                    self.MI.setMI(43142, self.MI.getisMember(), self.MI.getwhere())
            else:  # 입력한 좌석이 존재하지 않는 경우
                print("예약할 수 없는 좌석입니다. 다시 입력해 주세요")
                self.MI.setMI(4313, self.MI.getisMember(), self.MI.getwhere())

    def menu43141(self, input):
        assert isinstance(input, str)
        mileage = int(self.__FM.getuser(self.userName, self.password).get("mileage"))
        if input.isdecimal() and int(input) >= 0:
            if mileage >= int(input):  # 마일리지 잔액보다 적거나 같게 입력했을 경우
                print("나머지 금액은", self.final_cost - int(input), " 입니다. 등록된 카드로 결제하겠습니다.")
                # 마일리지를 저장
                mileage = mileage - int(input) + int(self.final_cost / 10)
                self.__FM.getuser(self.userName, self.password)['mileage'] = mileage

                # 예매 코드 출력
                print("결제가 완료되었습니다. 예매 코드 : ", self.selected_movie[0] + self.seat_First)

                self.__FM.bookmovie('1', self.userName, self.selected_movie[1], self.seat_list)
                # 수정된 파일들 저장
                self.__FM.savefile()
                time.sleep(1)  # 1초동안 예매 코드를 보여줌
                os.system('cls')
                self.print_main_menu()
                self.MI.setMI(4300, self.MI.getisMember(), self.MI.getwhere())
            else:
                print("초과된 마일리지 금액입니다. 다시 입력해 주세요.")
                self.MI.setMI(43141, self.MI.getisMember(), self.MI.getwhere())
        else:
            print("입력 형식이 맞지 않습니다.")
            return -1

    def menu43142(self, input):
        assert isinstance(input, str)
        #존재하지 않는 카드 번호일 경우
        if self.__TC.cardNum(input):
            if self.__FM.dupli_checkCARDNUM(input) == 1:
                print("존재하지 않는 카드 번호입니다. 다시 입력해 주세요.")
                self.MI.setMI(43142, self.MI.getisMember(), self.MI.getwhere())
            # 이미 등록된 카드 번호일 경우
            elif self.__FM.dupli_checkCARDNUM(input) == 2:
                print("이미 등록된 카드 번호입니다. 다시 입력해 주세요.")
                self.MI.setMI(43142, self.MI.getisMember(), self.MI.getwhere())
            # 유효한 카드 번호일 경우
            else:
                # 예매 코드 출력
                print("결제가 완료되었습니다. 예매 코드 : ", self.selected_movie[0] + self.seat_First)

                self.__FM.bookmovie('1', self.userName, self.selected_movie[1], self.seat_list)
                # 수정된 파일들 저장
                self.__FM.savefile()
                time.sleep(1)  # 1초동안 예매 코드를 보여줌
                os.system('cls')
                self.print_main_menu()
                self.MI.setMI(4300, self.MI.getisMember(), self.MI.getwhere())

    def menu43212(self, input):
        assert isinstance(input, str)
        if self.__TC.checkReservationCode(input):
            if self.__FM.getReservation("", input) != -1:     #존재하는 예매 코드인 경우
                # 예매 코드에 해당하는 영화정보 출력
                self.printMovies(input)
                print("취소하시려는 영화의 예매 코드를 입력해 주세요.(취소하지 않고  메인 메뉴로 돌아가시려면 “BACK”을 입력해 주세요.)")
                self.MI.setMI(4322, self.MI.getisMember(), self.MI.getwhere())
            else:  #존재하지 않는 예매 코드인 경우
                print("존재하지 않는 예매 코드입니다. 다시 입력해 주세요.")
                self.MI.setMI(43212, self.MI.getisMember(), self.MI.getwhere())

    def menu4322(self, input):
        assert isinstance(input, str)
        if self.__TC.checkReservationCode(input):
            if self.__FM.getReservation("", input) != -1:     #존재하는 예매 코드인 경우
                # 예매 코드를 취소 - ReservationList, MovieList를 업데이트
                movie = self.__FM.book_cancel(input)
                self.__FM.savefile()
                print(movie[2], "의 예매가 취소되었습니다.", sep='')
                time.sleep(1)
                os.system('cls')
                self.print_main_menu()
                self.MI.setMI(4300, self.MI.getisMember(), self.MI.getwhere())
            else:  #존재하지 않는 예매 코드인 경우
                print("존재하지 않는 예매 코드입니다. 다시 입력해 주세요.")
                self.MI.setMI(4322, self.MI.getisMember(), self.MI.getwhere())


    def print_login_menu(self):
        print("1. 회원 로그인")
        print("2. 회원 가입")
        print("3. 비회원 로그인")

    def print_main_menu(self):
        print("1. 영화 예매")
        print("2. 예매 내역 조회 및 취소")
        print("3. 영화 시간표 조회")

    def print_10days(self):
        year = int(self.__now_time[:4])
        month = int(self.__now_time[4:6])
        day = int(self.__now_time[6:8]) - 1

        count = 0  # 일주일마다 행을 나누기 위한 변수

        print('\t', year, '년')
        print('\t', month, '월')
        for i in range(0, 11):
            day = day + 1
            if month == 4 or month == 6 or month == 9 or month == 11:
                if day > 30:
                    month = month + 1
                    day = 1
                    count = 0
                    print('\n\t', month, '월')
            elif month == 2:
                if day > 28:
                    month = month + 1
                    day = 1
                    count = 0
                    print('\n\t', month, '월')
            else:
                if day > 31:
                    if month == 12:
                        year = year + 1
                        if year > 9999:
                            year = 0
                            print('\n\t', year, '년')
                        else:
                            print('\n\t', year, '년')
                        month = 1
                    else:
                        month = month + 1
                    day = 1
                    count = 0
                    print('\t', month, '월')
            if count != 6:
                print(day, end=' ')
            else:
                print(day)  # 일주일마다 행을 넘겨줌
            count = count + 1
        if count != 6:
            print()

        # 그날 영화 리스트 출력해주는 함수

    def printday_movie(self):
        if self.day_movielist:  # 리스트가 빈 리스트가 아닌 경우
            for index, elem in enumerate(self.day_movielist):
                print(str(index) + ". " + elem[1][2] + " 시작시간 " + elem[1][3])
            return True
        else:
            return False

        # 해당 영화 좌석 출력해주는 함수
    def print_seat(self, index, movie_name):
        assert isinstance(index, int)
        if self.day_movielist[index][1][2] == movie_name:  # 입력한 번호와 예매하고자 하는 영화명이 같으면
            self.selected_movie = self.day_movielist[index]  # 그 영화 정보를 저장
            seat_info = self.day_movielist[index][1][6].split('x')
            seat_ver = int(seat_info[0])
            seat_hor = int(seat_info[1])
            for a in range(0, seat_hor):
                print("-", end='')
            print("Screen", end='')
            for a in range(0, seat_hor):
                print("-", end='')
            print()
            alpha = 'A'
            for i in range(1, seat_ver + 2):
                if i == 1:
                    for j in range(0, seat_hor + 1):
                        if j == 0:
                            print(end='  ')
                        else:
                            print(j, end=' ')
                    print()
                else:
                    print(alpha, end=' ')
                    alpha = chr(ord(alpha) + 1)
                    for seat in list(self.day_movielist[index][1][5 + i]):
                        if seat == '0':
                            print("□", end=' ')
                        else:
                            print("■", end=' ')
                    print()
            return True
        else:
            return False

    def count_seat(self, seat_input):
        seatList = self.__FM.seats_to_list(seat_input)
        self.seat_First = seatList[0]
        cnt = 0
        for seat in seatList:
            row = ord(seat[0]) - ord('A') + 1
            col = int(seat[1:])
            if len(self.selected_movie[1][6 + row]) < col:                  #예약 가능 좌석 보다 높은 값일 때
                return -1
            if list(self.selected_movie[1][6 + row])[col - 1] == '1':  # 예약되어 있으면
                return -1
            else:
                cnt = cnt + 1
        return cnt

    #회원의 예매 내역을 시간순으로 출력해주는 함수
    def printMovies(self, reserve_code):
        if self.MI.getisMember():           #회원이면
            pq = PriorityQueue()
            R_list = self.__FM.getReservation(self.userName, "")
            #시간 정보만 따로 뽑아서 우선순위 큐에 넣어 정렬한다. - 시간이 작은 것부터 꺼내짐
            for index in R_list:
                Priority = int(self.__FM.reservationlist[index][2][0:8] + self.__FM.reservationlist[index][2][10:14])
                pq.put((Priority, self.__FM.reservationlist[index]))

            while not pq.empty():               #큐에 있는 모든 값을 출력
                reserve = pq.get()[1]
                movie = self.__FM.movielist[reserve[2][0:14]]
                print("예매 코드 ", reserve[2], " " , movie[2]," " , movie[0][0:4], "년 ", movie[0][4:6], "월 ", movie[0][6:8], "일 ", movie[3][0:2], ":", movie[3][2:], " ", reserve[3] , sep="")
        else:                               #getReservation 함수로 예매 코드에 해당하는 ReservationList의 index를 가져옴
            R_index = self.__FM.getReservation("", reserve_code)
            reserve = self.__FM.reservationlist[R_index]                #그 index로 ReservationList에서 예약 정보 리스트를 가져옴
            movie = self.__FM.movielist[self.__FM.reservationlist[R_index][2][0:14]]        #그 리스트의 예매 코드에서 좌석 정보만을 빼면 영화 정보를 찾을 수 있음.
            print("예매 코드 ", reserve[2], " ", movie[2], " ", movie[0][0:4], "년 ", movie[0][4:6], "월 ", movie[0][6:8],
                  "일 ", movie[3][0:2], ":", movie[3][2:], " ", reserve[3], sep="")
