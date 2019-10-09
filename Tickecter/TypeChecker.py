import os
class TypeChecker:

    def ID_check(self, new_id):
        countalpha = 0
        countnum = 0
        if len(new_id) < 4 or len(new_id) > 10:
            print("입력 형식에 맞지 않습니다.")  # 길이
            return False
        for index_value in new_id:
            if index_value.isalpha() == 1 and index_value.islower() == 1:
                countalpha = countalpha + 1
                # print(countalpha)
            elif index_value.isdigit() == 1:
                countnum = countnum + 1
                # print(countnum)
        if countnum + countalpha == 0 or new_id.count(' ') > 0:
            print("입력 형식에 맞지 않습니다.")  # 숫자나 문자가 없거나 공백 있음
            return False
        else:
            import csv
            input_file = "UserList.csv"
            with open(input_file, 'r', newline='') as csv_in_file:
                selected_column = [0]
                idCheck = csv.reader(csv_in_file)
                next(idCheck)
                for row_list in idCheck:
                    for index_value in selected_column:
                        if row_list[index_value] == new_id:
                            print("존재하는 아이디입니다.")
                            return False
            print("사용 가능한 아이디입니다.")
            return True


    def date_check(self, date):
        if date.isdigit() == 0:
            print('숫자만 입력 가능합니다.')
        else:
            if date[4] > '1' or date[6] > '3':  # 20월 이상, 40일 이상 먼저 거름
                print('날짜가 입력 형식에 맞지 않습니다.')
                return False
            elif date[4] == '0' and date[5] == '0' or date[6] == '0' and date[7] == '0':  # 월 또는 일이 00인 경우 제외
                print('날짜가 입력 형식에 맞지 않습니다.')
                return False
            elif (date[4] == '0' and date[5] <= '9') or (date[4] == '1' and date[5] <= '2'):  # 0~9나  10~12월인지 검증
                if (date[6] <= '2') or (
                        date[5] != '2' and date[6] == '3' and date[7] <= '1'):  # 날짜가 10~29일, 또는 30~31일인지 확인(2월 제외)
                    if (date[5] == '4' or date[6] == '6' or date[6] == '9' or (date[4] == '1' and date[5] == '1')) and (
                            date[6] == '3' and date[7] >= '1'):
                        # 4, 6, 9 11월일때는 31일이면 안 됨
                        print('날짜가 입력 형식에 맞지 않습니다.')
                        return False
                    elif date[5] == '2' and (date[7] == '9' or date[6] > '2'):
                        print('날짜가 입력 형식에 맞지 않습니다.')
                        return False
                    else:
                        return True


    def pw_check(self, password):
        countalpha = 0
        countnum = 0
        if len(password) < 4 or len(password) > 10:
            print("입력 형식에 맞지 않습니다.")  # 길이
            return False
        for index_value in password:
            if index_value.isalpha() == 1 and index_value.islower() == 1:
                countalpha += 1
            elif index_value.isdigit() == 1:
                countnum += 1
        if countnum + countalpha == 0 or password.count(' '):
            print("입력 형식에 맞지 않습니다.")  # 숫자나 문자 없거나 공백 포함
            return False
        else:
            print("사용 가능한 비밀번호입니다.")
            return True


    def movieTitle(self, title):
        if len(title) > 20 and title[0].isspace() == 1:
            print("입력 형식에 맞지 않습니다.")  # 길이
            return False
        else:
            for index_value in title:
                if (index_value.isalpha() == 0 or index_value.islower() == 0) and index_value.isdigit() == 0:
                    print("입력 형식에 맞지 않습니다.")  # 숫자나 영문 소문자가 아님
                    return False
        if title.count('  ') > 0:
            print("입력 형식에 맞지 않습니다.")  # 공백 연속으로 들어감
            return False
        else:
            import csv
            input_file = "MovieList.csv"
            with open(input_file, 'r', newline='') as csv_in_file:
                selected_column = [2]
                titlecheck = csv.reader(csv_in_file)
                next(titlecheck)
                for row_list in titlecheck:
                    for index_value in selected_column:
                        if row_list[index_value] == title:
                            return True
        print("상영중인 영화가 아닙니다.")
        return False


    def checkyoursheet(self, sheet):
        if sheet[0].isupper() == 0 or sheet[1:].isdigit() == 0:
            print("입력 형식에 맞지 않습니다.")  # 길이
            return False
        else:
            return True