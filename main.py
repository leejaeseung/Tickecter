from Tickecter import MenuManager
import os

def main():
    MM = MenuManager.MenuManager()

    while True:
        inpt = input()
        assert MM.getMI().getwhere() == 0 or MM.getMI().getwhere() == 1 or MM.getMI().getwhere() == 2
        if inpt == 'EXIT':
            break
        elif inpt == 'RESTART':
            if MM.getMI().getwhere() != 0 or MM.getMI().getmenuNum() != 4100:
                MM.getMI().setMI(4200, False, 1)
                MM.userName = ""
                MM.password = ""
                os.system('cls')
                MM.print_login_menu()
            continue
        elif inpt == 'BACK':
            if MM.getMI().getwhere() == 2 or MM.getMI().getmenuNum() >= 4300:
                MM.getMI().setMI(4300, MM.getMI().getisMember(), MM.getMI().getwhere())
                os.system('cls')
                MM.print_main_menu()
            continue
        MM.manageMenu(inpt)


    print("프로그램이 종료됩니다.")


if __name__ == "__main__":
    main()
