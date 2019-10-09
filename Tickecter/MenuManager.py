from . import Menu, menuInfo


class MenuManager(Menu.Menu):

    def __init__(self):
        super().__init__()
        self.__MI = menuInfo.menuInfo(4100, False, 0)

    def getMI(self):
        return self.__MI

    def manageMenu(self, input):
        menu = self.__MI.getmenuNum()

        if menu == 4100:
            mN, iB, w = super().menu4100(input)
            self.__MI = menuInfo.menuInfo(mN, iB, w)
        elif menu == 4200:
            mN, iB, w = super().menu4200(input)
            self.__MI = menuInfo.menuInfo(mN, iB, w)
        elif menu == 4211:
            mN, iB, w = super().menu4211(input)
            self.__MI = menuInfo.menuInfo(mN, iB, w)
        elif menu == 4212:
            mN, iB, w = super().menu4212(input)
            self.__MI = menuInfo.menuInfo(mN, iB, w)
        elif menu == 4221:
            mN, iB, w = super().menu4221(input)
            self.__MI = menuInfo.menuInfo(mN, iB, w)
        elif menu == 4222:
            mN, iB, w = super().menu4222(input)
            self.__MI = menuInfo.menuInfo(mN, iB, w)
        elif menu == 4223:
            mN, iB, w = super().menu4223(input)
            self.__MI = menuInfo.menuInfo(mN, iB, w)
        elif menu == 4230:
            mN, iB, w = super().menu4230(input)
            self.__MI = menuInfo.menuInfo(mN, iB, w)
        elif menu == 4300:
            mN, iB, w = super().menu4212(input)
            self.__MI = menuInfo.menuInfo(mN, iB, w)

        else:
            return -1
