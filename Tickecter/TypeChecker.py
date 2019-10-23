import os


class TypeChecker:

    def ID_check(self, new_id):  # 아이디가 형식에 맞는지 확인
        assert isinstance(new_id, str)
        count = 0
        if len(new_id) < 4 or len(new_id) > 10:  # 길이
            return False
        for index_value in new_id:
            if (index_value.isalpha() and index_value.islower()) or index_value.isdigit():
                count += 1
            else:
                return False  # 입력받은 문자가 숫자나 문자가 아니면 False
        if count == 0 or new_id.isspace():  # 숫자나 문자가 1개도 없거나 공백 있음
            return False
        else:
            return True

    def date_check(self, date):  # 날짜가 형식에 맞는지 확인(날짜만, 8자리)
        assert isinstance(date, str)
        if date.isdigit() == 0 or len(date) != 8:
            return False
        else:
            if date[4] > '1' or date[6] > '3':  # 20월 이상, 40일 이상 먼저 거름
                return False
            elif date[4] == '0' and date[5] == '0' or date[6] == '0' and date[7] == '0':  # 월 또는 일이 00인 경우 제외
                return False
            else:
                if (date[4] == '0' and date[5] <= '9') or (date[4] == '1' and date[5] <= '2'):  # 0~9나  10~12월인지 검증
                    if (date[6] <= '2') or (
                            not (date[4] == '0' and date[5] == '2') and date[6] == '3' and date[7] <= '1'):
                        # 날짜가 10~29일, 또는 30~31일인지 확인(2월 제외)
                        if (date[5] == '4' or date[6] == '6' or date[6] == '9' or (
                                date[4] == '1' and date[5] == '1')) and (
                                date[6] == '3' and date[7] >= '1'):
                            # 4, 6, 9 11월일때는 31일이면 안 됨
                            return False
                        else:
                            return True
                    else:
                        if date[4] == '0' and date[5] == '2' and (date[7] == '9' or date[6] > '2'):
                            return False
                        else:
                            return False
                else:
                    return False

    def time_check(self, date):  # 날짜 및 시간이 형식에 맞는지 확인(12자리,날짜 시간 모두 검증)
        assert isinstance(date, str)
        if date.isdigit() == 0 or len(date) != 12:
            return False
        else:
            if date[4] > '1' or date[6] > '3':  # 20월 이상, 40일 이상 먼저 거름
                return False
            elif date[4] == '0' and date[5] == '0' or date[6] == '0' and date[7] == '0':  # 월 또는 일이 00인 경우 제외
                return False
            else:
                if (date[4] == '0' and date[5] <= '9') or (date[4] == '1' and date[5] <= '2'):  # 0~9나  10~12월인지 검증
                    if (date[6] <= '2') or (
                            not (date[4] == '0' and date[5] == '2') and date[6] == '3' and date[7] <= '1'):
                        # 날짜가 10~29일, 또는 30~31일인지 확인(2월 제외)
                        if (date[5] == '4' or date[6] == '6' or date[6] == '9' or (
                                date[4] == '1' and date[5] == '1')) and (
                                date[6] == '3' and date[7] >= '1'):
                            # 4, 6, 9 11월일때는 31일이면 안 됨
                            return False
                        else:
                            if date[8] > '2' or date[10] > '5' or (date[8] == '2' and date[9] > '4'):  # 30시 또는 60분, 25시
                                return False
                            else:
                                return True
                    else:
                        if date[5] == '2' and (date[7] == '9' or date[6] > '2'):
                            return False
                        else:
                            return False
                else:
                    return False

    def pw_check(self, password):  # 비밀번호가 형식에 맞는지 검증
        assert isinstance(password, str)
        count = 0
        if len(password) < 4 or len(password) > 10:  # 길이
            return False
        for index_value in password:
            if (index_value.isalpha() and index_value.islower()) or index_value.isdigit():
                count += 1
            else:
                return False  # 입력받은 문자중 하나라도 숫자나 문자가 아니면 False
        if count == 0 or password.count(' '):  # 숫자나 문자가 하나도 없거나 공백 포함
            return False
        else:
            return True

    def checkMovieTitle(self, title):
        assert isinstance(title, str)
        checker = title.split('.', maxsplit=1)  # '.'을 기준으로 문자열을 나눈다
        if len(title) > 20 or len(title) == 0 or title.count('. ') or title.count('  ') or title.count('.') == 0:
            # 글자가 없거나 20자를 넘거나 공백으로 시작하거나 공백이 연속으로 들어갔는지 또는 점이 없는지 확인
            return False
        else:
            if checker[0].isdigit() and checker[1]:  # '.'앞이 숫자인지 확인. 숫자이면 '.'뒤의 문자열 검증
                for index_value in checker[1]:
                    if not index_value.isalpha():
                        if index_value.isdigit() or index_value.isspace():
                            continue
                        # 입력된 문자 중 하나라도 숫자나 공백, 영문 소문자가 아니면 False
                        return False
                    else:
                        if not index_value.islower():
                            # 입력된 문자 중 하나라도 영문 소문자가 아니면 False
                            return False
                return True
            else:
                return False

    def cardNum(self, cardnumber):  # 카드번호가 형식에 맞는지 검증
        assert isinstance(cardnumber, str)
        if len(cardnumber) != 12 or cardnumber.isdigit() or cardnumber.isspace():
            return False
        else:
            return True

    def checkSeatsList(self, strseat):         # 좌석 str 받으면 형식 검증 후 리스트 리턴 함수
        assert isinstance(strseat, str)
        if len(strseat) < 2:
           list = []
           return list
        elif len(strseat) < 3:
            if self.checkOneSeat(strseat):
                list = [strseat]
                return list
            else:
                list = []
                return list
        else:
            if strseat.count("~") == 1:
                list = strseat.split("~")
                if self.checkOneSeat(list[0]) and self.checkOneSeat(list[1]):
                    firstseat = list[0]
                    lastseat = list[1]
                    list = []
                    if firstseat[0] == lastseat[0] and firstseat[1].isdigit() and lastseat[1].isdigit() and firstseat[1] != lastseat[1]:
                        for i in range(int(firstseat[1]), int(lastseat[1])+1):
                            list.append(firstseat[0] + str(i))
                        return list
                    else:
                        return list
                else:
                    list = []
                    return list
            elif strseat.find(","):
                list = strseat.split(",")
                for i in list:
                    if self.checkOneSeat(i) == 0 or strseat.count(i) > 1:
                        list = []
                        return list
                return list
            else:
                list = []
                return list

    def checkOneSeat(selfs, seat):
        assert isinstance(seat, str)
        if len(seat) == 2 and seat[0].isupper() and seat[1].isdigit():    # 한글자만 검증하므로 isalpha를 안 써도 된다.
            return True
        else:
            return False

    def checkReservationCode(self, code):  # 예매번호 형식 체크  ex) 20190929AA0930F1
        assert isinstance(code, str)
        if len(code) == 16:
            if code[0:8].isdigit() and code[10:14].isdigit() and code[15].isdigit():
                if code[8:10].isalpha() and code[8:10].isupper() and code[14].isalpha() and code[14].isupper():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
