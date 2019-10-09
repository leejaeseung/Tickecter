from . import Menu, menuInfo, TypeChecker


class MenuManager(Menu.Menu):

    def __init__(self):
        super().__init__()
        self.__TC = TypeChecker.TypeChecker()

    def getMI(self):
        return super().MI

    def manageMenu(self, input):
        menu = super().MI.getmenuNum()

        if menu == 4100:
            # if self.__TC.date_check(input):
                super().menu4100(input)
        elif menu == 4200:
            super().menu4200(input)
        elif menu == 4211:
            super().menu4211(input)
        elif menu == 4212:
            super().menu4212(input)
        elif menu == 4221:
            super().menu4221(input)
        elif menu == 4222:
            super().menu4222(input)
        elif menu == 4223:
            super().menu4223(input)
        elif menu == 4300:
            super().menu4300(input)
        elif menu == 4311:
            super().menu4311(input)
        elif menu == 4312:
            super().menu4312(input)
        elif menu == 4313:
            super().menu4313(input)
        else:
            return -1
