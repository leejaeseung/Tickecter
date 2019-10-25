class menuInfo:

    #리스타트, 백 1이면 로그인 안한 상황 2면 메인메뉴 들어감. 0이면 현재날짜넣기

    def __init__(self, mN, iM, w):
        self.setMI(mN, iM, w)

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
