from . import Menu


class MenuManager(Menu.Menu):   #상속

    def __init__(self):
        super().__init__()

    def getMI(self):
        return self.MI

    def manageMenu(self, input):
        assert isinstance(input, str)
        menu = self.MI.getmenuNum()
        assert isinstance(menu, int)

        if menu == 4100:
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
        elif menu == 43141:
            self.menu43141(input)
        elif menu == 43142:
            self.menu43142(input)
        elif menu == 43212:
            self.menu43212(input)
        elif menu == 4322:
            self.menu4322(input)
        else:
            return -1
