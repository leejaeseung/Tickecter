from . import FileManager, menuInfo
import os
import time

class Menu:

    def __init__(self):
        print("현재 시간을 입력해 주세요.")
        self.__now_time = 0
        self.__FM = FileManager.FileManager()
        self.MI = menuInfo.menuInfo(4100, False, 0) #__menuNum,__isMember,__where


    def menu4100(self, input):
        self.__now_time = str(input)
        self.print_login_menu()
        self.MI.setMI(4200, self.MI.getisMember(), 1)  #로그인 안한 상황

    def menu4200(self, input):
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
            return -1

    def menu4211(self, input):    # self.MI.isMember=1 인 경우. (회원 로그인)
        # 파일 관리 클래스를 사용해 input 과 비교, if문으로 True면 다음 메뉴, False면 다시 입력받음,아이디를 잠시 저장
        # if True :  #존재하는 아이디면
        tempID = str(input)     #아이디를 입력받아 임시 공간에 저장, FileManager 객체 __FM의 userlist의 userID와 비교.
        if tempID == self.__FM.userlist[tempID]:     #일치한다면  menu4212로..
            print("Password를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
            self.MI.setMI(4212, self.MI.getisMember(), self.MI.getwhere())

        # else:      #존재하지 않는 아이디면
        else:
            print("존재하지 않는 ID입니다. 다시 입력해 주세요.")
            self.MI.setMI(4211, self.MI.getisMember(), self.MI.getwhere())

    def menu4212(self, input):
        # 파일 관리 클래스를 사용해 input 과 비교, if문으로 True면 다음 메뉴, False면 다시 입력받음, 비밀번호를 잠시 저장
        tempPW = str(input)     #비밀번호를 입력받아 임시 공간에 저장
        if tempPW == self.__FM.userlist.userID.userpassword:     #객체 __FM의 userlist의 uesrpassword와 비교해서 비밀번호가 일치하면
            print("로그인 성공!")
        self.print_main_menu()
        self.MI.setMI(4300, True, 2)

        # 일치하지 않으면
        else:
            print("일치하지 않는 Password입니다. 다시 입력해 주세요.")
            self.MI.setMI(4212, self.MI.getisMember(), self.MI.getwhere())

    def menu4221(self, input):
        # 파일 관리 클래스를 사용해 input 과 비교, if문으로 True면 다음 메뉴, False면 다시 입력받음, 아이디를 잠시 저장
        tempID = str(input)      #아이디를 입력받아 임시 공간에 저장
        if tempID != self.__FM.userlist.userID:     #만들 수 있는 아이디면,
            print("생성가능한 아이디입니다.\nPassword를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
            self.MI.setMI(4222, self.MI.getisMember(), self.MI.getwhere())
            self.__FM.savefile()

        else:         # userlist에 이미 존재하는 아이디면
            print("이미 존재하는 ID입니다. 다시 입력해 주세요.")
            self.MI.setMI(4221, self.MI.getisMember(), self.MI.getwhere())

    def menu4222(self, input):
        # 비밀번호를 저장
        tempPw = str(input)
        print("아이디, 비밀번호 생성이 완료되었습니다.")
        print("등록할 카드 번호를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
        self.__MI.savefile()
        self.MI.setMI(4223, self.MI.getisMember(), self.MI.getwhere())

    def menu4223(self, input):
        tempCardnum = int(input)
        # if 2 :     #이미 등록된 카드 번호이면
        if tempCardnum == self.__FM.cardlist.cardnum:
            print("이미 등록된 카드 번호입니다. 다시 입력해 주세요.")
            self.MI.setMI(4223, self.MI.getisMember(), self.MI.getwhere())

        # elif 1 :   #존재하지 않는 카드 번호이면
            print("존재하지 않는 카드 번호입니다. 다시 입력해 주세요.")
            self.MI.setMI(4223, self.MI.getisMember(), self.MI.getwhere())

        elif tempCardnum != self.__FM.cardlist.cardnum:   #유효한 카드 번호이면 -> UserList를 업데이트
            os.system('cls')
            self.print_login_menu()
            self.MI.setMI(4200, self.MI.getisMember(), self.MI.getwhere())

    def menu4300(self, input):
        new_input = int(input)
        if new_input == 1:
            self.print_10days()
            # 현재 날짜로부터 10일 후 까지의 달력 출력
            print("상영을 원하는 날짜를 8자리로 입력해 주세요.")
            self.MI.setMI(4311, self.MI.getisMember(), self.MI.getwhere())
        #elif new_input == 2:

            #return 4221, False, 1  수정 필요
        #elif new_input == 3:
            #return 4300, False, 2  수정 필요
        #else:
            #return -1

    def menu4311(self, input):
        if int(input) < int(self.__now_time):
            print("현재 날짜보다 이전 날짜입니다. 다시 입력해 주세요.")
            self.MI.setMI(4311, self.MI.getisMember(), self.MI.getwhere())
        else:
            #상영중인 영화를 한 줄씩 출력
            print("상영중인 영화.....")
            print("예매할 영화를 선택하세요.(숫자.영화명 입력)")
            self.MI.setMI(4312, self.MI.getisMember(), self.MI.getwhere())

    def menu4312(self, input):
        #if True: # 입력한 영화가 존재할 경우
            # 선택한 영화의 좌석표를 출력
            print("예약할 좌석을 고르십시오.")
            self.MI.setMI(4313, self.MI.getisMember(), self.MI.getwhere())
        #else:    # 입력한 영화가 존재하지 않을 경우
            print("존재하지 않는 영화입니다. 다시 입력해 주세요.")
            #self.MI.setMI(4312, self.MI.getisMember(), self.MI.getwhere())

    def menu4313(self, input):
        #if True: #입력한 좌석이 존재하는 경우
            #결제 금액을 출력
            if self.MI.getisMember():
                #보유 마일리지를 출력
                print("회원님의 마일리지 잔액은 ㅁㅁㅁ 입니다. 얼마를 사용하시겠습니까?")
                self.MI.setMI(43141, self.MI.getisMember(), self.MI.getwhere())
            else:
                print("결제하실 카드 번호를 입력해 주세요.")
                self.MI.setMI(43142, self.MI.getisMember(), self.MI.getwhere())
        #else:      #입력한 좌석이 존재하지 않는 경우
            #print("존재하지 않는 좌석입니다. 다시 입력해 주세요")
            #self.MI.setMI(4313, self.MI.getisMember(), self.MI.getwhere())

    def menu43141(self, input):
        #if True:       #마일리지 잔액보다 적거나 같게 입력했을 경우
            print("나머지 금액은 ㅁㅁㅁ 입니다. 등록된 카드로 결제하겠습니다.")
            #마일리지를 변수에 저장
            self.MI.setMI(4315, self.MI.getisMember(), self.MI.getwhere())
        #else:
            print("초과된 마일리지 금액입니다. 다시 입력해 주세요.")
            self.MI.setMI(43141, self.MI.getisMember(), self.MI.getwhere())

    def menu43142(self, input):
        #if #존재하지 않는 카드 번호일 경우
            print("존재하지 않는 카드 번호입니다. 다시 입력해 주세요.")
            self.MI.setMI(43142, self.MI.getisMember(), self.MI.getwhere())

        #elif #이미 등록된 카드 번호일 경우
            print("이미 등록된 카드 번호입니다. 다시 입력해 주세요.")
            self.MI.setMI(43142, self.MI.getisMember(), self.MI.getwhere())
        #else: #유효한 카드 번호일 경우
            self.MI.setMI(4315, self.MI.getisMember(), self.MI.getwhere())

    def menu4315(self, input):
        #if self.MI.getisMember():       #회원이면 마일리지를 저장함

        #else:                          #비회원이면 마일리지 저장x

        print("결제가 완료되었습니다. 예매 코드 : ")
        # 예매 코드 출력
        time.sleep(1)                   #1초동안 예매 코드를 보여줌
        self.MI.setMI(4300, self.MI.getisMember(), self.MI.getwhere())

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

        count = 0       #일주일마다 행을 나누기 위한 변수

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
                print(day)                      #일주일마다 행을 넘겨줌
            count = count + 1
        if count != 6:
            print()
