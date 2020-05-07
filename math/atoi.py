class Atoi:
    @staticmethod
    def convert_str_to_int(string: str):
        sign = 1
        num = 0
        for i in range(len(string)):
            if string[i] is '-':
                sign = -1
            if string[0] is ' ' or string[0] is '-' or ('0' <= string[0] <= '9'):
                if string[i] is not '' and ('0' <= string[i] <= '9') and string[i] is not '-':
                    num = num * 10 + (ord(string[i]) - ord('0'))
            else:
                break
        num = sign * num
        if num > 2 ** 31-1:
            return 2 ** 31 - 1
        elif num < -2 ** 31:
            return -2 ** 31
        return num



print(Atoi().convert_str_to_int("42"))
