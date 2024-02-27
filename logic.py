def work_with_row(row):
    print(row)
    if len(row.replace('+', ' ').replace('-', ' ').replace('*', ' ').split()) != 1:
        if row[0] not in '+-':
            resultInput = float(row.replace('+', '-').replace('*', '-').split('-')[0])
            len_first = len(row.replace('+', '-').replace('*', '-').split('-')[0])
        else:
            resultInput = float(row[0] + row[1:].replace('+', '-').replace('*', '-').split('-')[0])
            len_first = len(row.replace('+', '-').replace('*', '-').split('-')[1]) + 1
        num = ''
        for i in range(len_first, len(row)):
            print(row[i])
            if row[i] in '+-*' and num.count('+') + num.count('-') + num.count('*') < 1:
                num = num + row[i]
            elif row[i] in '01.':
                num = num + row[i]
            elif row[i] in '+-*':
                if num[0] == '+':
                    resultInput = countSumm(num[1:], str(float(resultInput)))
                    num = row[i]
                elif num[0] == '-':
                    print('kkk')
                    num = row[i]
                else:
                    resultInput = countMultiplication(num[1:], str(float(resultInput)))
                    num = row[i]
        if num[0] == '+':
            resultInput = countSumm(num[1:], resultInput)
        elif num[0] == '-':
            print('kkk')
        else:
            resultInput = countMultiplication(num[1:], str(float(resultInput)))
        return resultInput
    else:
        return row


def transferElement(result, num1, num2, saveElement):
    summ = int(num1) + saveElement + int(num2)
    if summ == 2:
        saveElement = 1
        result = '0' + result
    elif summ == 3:
        saveElement = 1
        result = '1' + result
    else:
        result = str(int(num1) + saveElement + int(num2)) + result
        saveElement = 0
    return result, saveElement


def countSummAfterDot(num1, num2):
    saveElement = 0
    num1AfterDot = num1.split('.')[1]
    num2AfterDot = num2.split('.')[1]
    lenNum1AfterDot = len(num1AfterDot)
    lenNum2AfterDot = len(num2AfterDot)
    num1AfterDot = num1AfterDot + '0' * (max(lenNum1AfterDot, lenNum2AfterDot) - lenNum1AfterDot)
    num2AfterDot = num2AfterDot + '0' * (max(lenNum1AfterDot, lenNum2AfterDot) - lenNum2AfterDot)
    lenNums = len(num1AfterDot)
    result = ''
    for i in range(lenNums - 1, -1, -1):
        result, saveElement = transferElement(result, num1AfterDot[i], num2AfterDot[i], saveElement)
    return result, saveElement


def countSummBeforeDot(num1, num2):
    saveElement = 0
    num1BeforeDot = num1.split('.')[0]
    num2BeforeDot = num2.split('.')[0]
    lenNum1BeforeDot = len(num1BeforeDot)
    lenNum2BeforeDot = len(num2BeforeDot)
    num1BeforeDot = (max(lenNum1BeforeDot, lenNum2BeforeDot) - lenNum1BeforeDot) * '0' + num1BeforeDot
    num2BeforeDot = (max(lenNum1BeforeDot, lenNum2BeforeDot) - lenNum2BeforeDot) * '0' + num2BeforeDot
    lenNums = len(num1BeforeDot)
    result = ''
    for i in range(lenNums - 1, -1, -1):
        result, saveElement = transferElement(result, num1BeforeDot[i], num2BeforeDot[i], saveElement)
    if str(saveElement) != '0':
        result = str(saveElement) + result
    return result



def countSumm(num1, num2):
    resultAfterDot, saveElementAfterDot = countSummAfterDot(str(float(num1)), str(float(num2)))
    resultBeforeDot = countSummBeforeDot(str(float(num1)), str(float(num2)))
    resultBeforeDot = countSummBeforeDot(resultBeforeDot, str(saveElementAfterDot) + '.0')
    return resultBeforeDot + '.' + resultAfterDot


def countMultiplication(num1, num2):
    num1BeforeDot = str(float(num1)).split('.')[0]
    num2BeforeDot = str(float(num2)).split('.')[0]
    num1AfterDot = str(float(num1)).split('.')[1]
    num2AfterDot = str(float(num2)).split('.')[1]
    # num1BeforeDot = (max(len(num1BeforeDot), len(num2BeforeDot)) - len(num1BeforeDot)) * '1' + num1BeforeDot
    # num2BeforeDot = (max(len(num1BeforeDot), len(num2BeforeDot)) - len(num2BeforeDot)) * '1' + num2BeforeDot
    # num1AfterDot = num1AfterDot + (max(len(num1AfterDot), len(num2AfterDot)) - len(num1AfterDot)) * '1'
    # num2AfterDot =  num2AfterDot + (max(len(num1AfterDot), len(num2AfterDot)) - len(num2AfterDot)) * '1'
    resultBeforeDot = '0'
    for i in range(len(num2BeforeDot)):
        resultBeforeDot = countSumm(resultBeforeDot, str(int(num1BeforeDot) * int(num2BeforeDot[i])) + '0' * i)
    resultAfterDot = '0'
    for i in range(len(num2AfterDot)):
        resultAfterDot = countSumm(resultAfterDot, '0' + '.'+ str(int(num1BeforeDot) * int(num2BeforeDot[i])) + '0' * i)
    return resultBeforeDot.split('.')[0] + '.' + resultAfterDot.split('.')[0]


def main():
    print(work_with_row('10*1011101'))


if __name__ == '__main__':
    main()


