from . import Menu, menuInfo, TypeChecker


class MenuManager(Menu.Menu):

    def __init__(self):
        super().__init__()
        self.__TC = TypeChecker.TypeChecker()

    def getMI(self):
        return self.MI

    def manageMenu(self, input):
        menu = self.MI.getmenuNum()

        if menu == 4100:
            # if self.__TC.date_check(input):
                self.menu4100(input)
        elif menu == 4200:
            self.menu4200(input)
        elif menu == 4211:
            self.menu4211(input)
        elif menu == 4212:
            self.menu4212(input)
        elif menu == 4221:
            self.menu4221(input)
        elif menu == 4222:
            self.menu4222(input)
        elif menu == 4223:
            self.menu4223(input)
        elif menu == 4300:
            self.menu4300(input)
        elif menu == 4311:
            self.menu4311(input)
        elif menu == 4312:
            self.menu4312(input)
        elif menu == 4313:
            self.menu4313(input)
        else:
            return -1
