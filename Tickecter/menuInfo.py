class menuInfo:
    __menuNum = 0
    __isMember = 0
    __where = 0

    def __init__(self, mN, iM, w):
        self.__menuNum = mN
        self.__isMember = iM
        self.__where = w

    def getmenuNum(self):
        return self.__menuNum

    def getisMember(self):
        return self.__isMember

    def getwhere(self):
        return self.__where

    def setmenuNum(self, mN):
        assert isinstance(mN, int)
        self.__menuNum = mN

    def setisMember(self, iM):
        assert isinstance(iM, bool)
        self.__isMember = iM

    def setwhere(self, w):
        assert isinstance(w, int)
        self.__where = w
