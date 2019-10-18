from Tickecter import MenuManager
import os

from Tickecter.TypeChecker import TypeChecker


def main():
    MM = MenuManager.MenuManager()

    while True:
        inpt = input()
        if inpt == 'EXIT':
            break
        elif inpt == 'RESTART':
            if MM.getMI().getwhere() != 0:
                MM.getMI().setMI(4200, False, 1)
                MM.userName = None
                MM.password = None
                os.system('cls')
                MM.print_login_menu()
            continue
        elif inpt == 'BACK':
            if MM.getMI().getwhere() == 2:
                MM.getMI().setMI(4300, MM.getMI().getisMember(), MM.getMI().getwhere())
                os.system('cls')
                MM.print_main_menu()
            continue
        MM.manageMenu(inpt)

    print("프로그램이 종료됩니다.")


if __name__ == "__main__":
    main()
