class menuInfo:

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

    def setMI(self, mN, iM, w):
        assert isinstance(mN, int)
        self.__menuNum = mN
        assert isinstance(iM, bool)
        self.__isMember = iM
        assert isinstance(w, int)
        self.__where = w
