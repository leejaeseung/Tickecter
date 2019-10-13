from Tickecter import MenuManager
import os

from Tickecter.TypeChecker import TypeChecker


def main():
    global input
    MM = MenuManager.MenuManager()

    while True:
        input = input()
        """TP = TypeChecker()
        input2 = input()
        TP.checkyoursheet(input2)
        input2 = input()
        TP.pw_check(input2)
        input2 = input()
        TP.ID_check(input2)
        input2 = input()
        TP.cardNum(input2)
        input2 = input()
        TP.date_check(input2)
        input2 = input()
        TP.movieTitle(input2)"""
        if input == 'EXIT':
            break
        elif input == 'RESTART':
            if MM.getMI().getwhere() != 0:
                MM.getMI().setMI(4200, False, 1)
                MM.userName = None
                MM.password = None
                os.system('cls')
                MM.print_login_menu()
            del (input)
            continue
        elif input == 'BACK':
            if MM.getMI().getwhere() == 2:
                MM.getMI().setMI(4300, MM.getMI().getisMember(), MM.getMI().getwhere())
                os.system('cls')
                MM.print_main_menu()
            del (input)
            continue
        MM.manageMenu(input)
        del (input)

    print("프로그램이 종료됩니다.")


if __name__ == "__main__":
    main()
