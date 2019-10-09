import os

class Menu:

    def __init__(self):
        print("현재 시간을 입력해 주세요.")

    def menu4100(self, input):
        self.print_login_menu()
        return 4200, False, 1

    def menu4200(self, input):
        new_input = int(input)
        if new_input == 1:
            print("ID를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
            return 4211, False, 1
        elif new_input == 2:
            print("ID를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
            return 4221, False, 1
        elif new_input == 3:
            os.system('cls')
            self.print_main_menu()
            return 4300, False, 2
        else:
            return -1

    def menu4211(self,input):
        #파일 관리 클래스를 사용해 input 과 비교, if문으로 True면 다음 메뉴, False면 다시 입력받음,아이디를 잠시 저장
        #if True :  #존재하는 아이디면
            print("Password를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
            return 4212, False, 1
        #else:      #존재하지 않는 아이디면
            #print("존재하지 않는 ID입니다. 다시 입력해 주세요.")
            #return 4211, False, 1

    def menu4212(self,input):
        #파일 관리 클래스를 사용해 input 과 비교, if문으로 True면 다음 메뉴, False면 다시 입력받음, 비밀번호를 잠시 저장
        #if True :     #비밀번호가 일치하면
            self.print_main_menu()
            return 4300, True, 2
        #else :         #일치하지 않으면
            #print("일치하지 않는 Password입니다. 다시 입력해 주세요.")
            #return 4212, False, 1

    def menu4221(self,input):
        # 파일 관리 클래스를 사용해 input 과 비교, if문으로 True면 다음 메뉴, False면 다시 입력받음, 아이디를 잠시 저장
        #if True :     #만들 수 있는 아이디면
            print("Password를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
            return 4222, False, 1
        #else:          #이미 존재하는 아이디면
            #print("이미 존재하는 ID입니다. 다시 입력해 주세요.")
            #return 4221, False, 1

    def menu4222(self,input):
        #비밀번호를 잠시 저장
        print("등록할 카드 번호를 입력해 주세요.(되돌아 가려면 \"RESTART\"입력)")
        return 4223, False, 1

    def menu4223(self,input):
        #if 2 :     #이미 등록된 카드 번호이면
            #print("이미 등록된 카드 번호입니다. 다시 입력해 주세요.")
            #return 4223, False, 1
        #elif 1 :   #존재하지 않는 카드 번호이면
            #print("존재하지 않는 카드 번호입니다. 다시 입력해 주세요.")
            #return 4223, False, 1
        #else :     #유효한 카드 번호이면 -> UserList를 업데이트
        os.system('cls')
        self.print_login_menu()
        return 4200, False, 1

    def print_login_menu(self):
        print("1. 회원 로그인")
        print("2. 회원 가입")
        print("3. 비회원 로그인")

    def print_main_menu(self):
        print("1. 영화 예매")
        print("2. 예매 내역 조회 및 취소")
        print("3. 영화 시간표 조회")
