from Tickecter import MenuManager
import os


def main():
    global input
    MM = MenuManager.MenuManager()

    while True:
        input = input()
        if input == 'EXIT':
            break
        elif input == 'RESTART':
            if MM.getMI().getwhere() != 0:
                MM.getMI().setmenuNum(4200)
                MM.getMI().setisMember(False)
                MM.getMI().setwhere(1)
                os.system('cls')
                MM.print_login_menu()
            del (input)
            continue
        elif input == 'BACK':
            if MM.getMI().getwhere() == 2:
                MM.getMI().setmenuNum(4300)
                os.system('cls')
                MM.print_main_menu()
            del (input)
            continue
        #MM.manageMenu(input)
        #del (input)

    #print("프로그램이 종료됩니다.")


if __name__ == "__main__":
    main()
