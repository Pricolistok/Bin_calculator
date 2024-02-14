def work_with_row(row):
    if len(row.replace('+', ' ').replace('-', ' ').replace('*', ' ').split()) != 1:
        if row[0] not in '+-':
            result = float(row.replace('+', '-').replace('*', '-').split('-')[0])
            len_first = len(row.replace('+', '-').replace('*', '-').split('-')[0])
        else:
            result = float(row[0] + row[1:].replace('+', '-').replace('*', '-').split('-')[0])
            len_first = len(row.replace('+', '-').replace('*', '-').split('-')[1]) + 1
        print(result)
        num = ''
        for i in range(len_first, len(row)):
            if row[i] in '+-*' and num.count('+') + num.count('-') + num.count('*') < 1:
                num = num + row[i]
            elif row[i] in '0123456789.':
                num = num + row[i]
            elif row[i] in '+-*':
                if num[0] in '+-':
                    result += float(num)
                    num = row[i]
                else:
                    result *= float(num)
                    num = row[i]
            print(num)
        if num[0] in '+-':
            result += float(num)
        else:
            result *= float(num[1:])
        print(result)
        return to_second_ss(str(result))
    else:
        return to_second_ss(str(float(row)))


def slice_num(num):
    before_dot, end_dot = int(str(num).split('.')[0]), float('0.' + str(num).split('.')[1])
    return before_dot, end_dot


def to_second_ss(num):
    before_dot, end_dot = slice_num(num)
    sign = ''
    if before_dot < 0:
        sign = '-'
    before_dot = abs(before_dot)
    save_quotient = []
    result_end = ''
    result_before = ''
    iterate = 0
    while save_quotient.count(end_dot) <= 4 and end_dot != 0 and len(result_end) <= 5:
        end_dot *= 2
        num_after = slice_num(end_dot)
        print(num_after)
        if iterate != 0:
            save_quotient.append(num_after[1])
        result_end = result_end + str(num_after[0])
        iterate += 1
        end_dot = num_after[1]
    while before_dot > 0:
        result_before = str(before_dot % 2) + result_before
        before_dot //= 2
    if result_end == '':
        result_end = '0'
    if result_before == '':
        result_before = '0'
    print(str(sign + (7 - len(result_before)) * '0' + result_before + '.' + result_end))
    return str(sign + result_before + '.' + result_end)
