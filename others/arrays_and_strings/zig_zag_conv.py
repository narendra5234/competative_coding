class ZigZagConv(object):
    @staticmethod
    def convert(s, rows):
        if rows == 1:
            return s
        n = len(s)
        count = 2 * rows - 2
        zig_zag_str = ""
        for i in range(rows):
            for j in range(i, n, count):
                zig_zag_str += s[j]
                if i != rows - 1 and i != 0:
                    if j + count - 2 * i < n:
                        zig_zag_str += s[j + count - 2 * i]
        return zig_zag_str

    @staticmethod
    def convert_1(s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        l = [''] * numRows

        index, step = 0, 1

        for x in s:
            l[index] += x

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return ''.join(l)


obj = ZigZagConv()
print(obj.convert_1("PAYPALISHIRING", 4))
