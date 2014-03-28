__author__ = 'tongqingqiu'

import sys


class TextReader:
    """A text reader class"""

    def __init__(self):
        pass

    @staticmethod
    def read(filename, first_line_header):
        ins = open(filename, "r")
        data = []
        line_num = 0
        max_temp_span = 0
        max_temp_span_row_num = -1
        for line in ins:
            line_num += 1
            if first_line_header:
                if line_num == 1:
                    continue
            stripped_line = line.strip()
            if len(stripped_line) > 0:
                stripped_line = stripped_line.replace('*', '')
                row = stripped_line.split()
                high = float(row[1])
                low = float(row[2])
                if max_temp_span < (high - low):
                    max_temp_span = high - low
                    max_temp_span_row_num = row[0]
                data.append(stripped_line)
        ins.close()
        return max_temp_span_row_num


    @staticmethod
    def read_football(filename, first_line_header):
        ins = open(filename, "r")
        data = []
        line_num = 0
        max_temp_span = 0
        team_name = ''
        for line in ins:
            line_num += 1
            if first_line_header:
                if line_num == 1:
                    continue

            stripped_line = line.strip()
            if not stripped_line[0].isdigit():
                continue
            if len(stripped_line) > 0:
                stripped_line = stripped_line.replace('*', '')
                row = stripped_line.split()
                print row
                high = float(row[6])
                low = float(row[8])
                if max_temp_span < (high - low):
                    max_temp_span = high - low
                    team_name = row[1]
                data.append(stripped_line)
        ins.close()
        return team_name


def main():
    input_file = sys.argv[1]
    print TextReader.read_football(input_file, True)


if __name__ == '__main__':
    main()
