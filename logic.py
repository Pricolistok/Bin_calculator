from string import ascii_lowercase, ascii_uppercase


def work_with_row(row):
    for i in row:
        if i in '23456789' + ascii_lowercase + ascii_uppercase:
            return 'Error'
    if len(row.replace('+', ' ').replace('-', ' ').replace('*', ' ').split()) != 1:
        if row[0] not in '+-':
            resultInput = float(row.replace('+', '-').replace('*', '-').split('-')[0])
            len_first = len(row.replace('+', '-').replace('*', '-').split('-')[0])
        else:
            resultInput = float(row[0] + row[1:].replace('+', '-').replace('*', '-').split('-')[0])
            len_first = len(row.replace('+', '-').replace('*', '-').split('-')[1]) + 1
        num = ''
        for i in range(len_first, len(row)):
            if row[i] in '+-*' and num.count('+') + num.count('-') + num.count('*') < 1:
                num = num + row[i]
            elif row[i] in '01.':
                num = num + row[i]
            elif row[i] in '+-*':
                if num[0] == '+':
                    resultInput = countSumm(num[1:], str(float(resultInput)))
                    num = row[i]
                elif num[0] == '-':
                    resultInput = minus(str(float(resultInput)), num[1:])
                    num = row[i]
                else:
                    resultInput = countMultiplication(num[1:], str(float(resultInput)))
                    num = row[i]
        if num[0] == '+':
            resultInput = countSumm(num[1:], resultInput)
        elif num[0] == '-':
            resultInput = minus(str(float(resultInput)), num[1:])
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
    num1 = str(float(num1))
    num2 = str(float(num2))
    if len(num1.split('.')[1]) > len(num2.split('.')[1]):
        num2 = num2 + '0' * (len(num1.split('.')[1]) - len(num2.split('.')[1]))
    else:
        num1 = num1 + '0' * (len(num2.split('.')[1]) - len(num1.split('.')[1]))
    print(num1)
    print(num2)
    save = len(num2) - 1
    result = '0'
    dotInd = len(num1.split('.')[0]) + len(num2.split('.')[0])
    for i in range(len(num2) - 1, -1, -1):
        if num2[i] != '.':
            result = countSumm(result, str(int(num1.replace('.', '')) * int(num2[i])) + '0' * (len(num2) - save - 1))
            save -= 1
    result = list(str((result[:-2])))
    result.insert(dotInd, '.')
    result = str(float(str(''.join(result))))
    return result


def countMinus(arr1, arr2):
    for i in range(len(arr1) - 1, -1, -1):
        saveInd = i - 1
        if arr1[i] - arr2[i] < 0:
            while arr1[saveInd] < 1:
                arr1[saveInd] = 1
                saveInd -= 1
            arr1[saveInd] -= 1
            arr1[i] = 1
        else:
            arr1[i] = arr1[i] - arr2[i]
    return arr1




def maximum_value(arr1, arr2, dotind):
    summ1 = 0
    summ2 = 0
    arr1.reverse()
    arr2.reverse()
    for i in range(len(arr1) - 1, dotind - 1, -1):
        summ1 = summ1 + arr1[i] * (2 ** i)
        summ2 = summ2 + arr2[i] * (2 ** i)
    arr1.reverse()
    arr2.reverse()
    for i in range(dotind - 1, -1, -1):
        summ1 = summ1 + arr1[i] * (1 / (2 ** i))
        summ2 = summ2 + arr2[i] * (1 / (2 ** i))
    if summ1 > summ2:
        return 1
    return 2


def createBef(num1, num2):
    num1Bef = num1.split('.')[0]
    num2Bef = num2.split('.')[0]
    leni1 = len(num1Bef)
    leni2 = len(num2Bef)
    if leni1 > leni2:
        num2Bef = '0' * abs(leni1 - leni2) + num2Bef
        arr1Bef = [0] * leni1
        arr2Bef = [0] * leni1
        for i in range(leni1):
            arr1Bef[i] = int(num1Bef[i])
        for i in range(leni2):
            arr2Bef[i] = int(num2Bef[i])
    elif leni1 == leni2:
        leni2 = len(num2Bef)
        arr1Bef = [0] * leni2
        arr2Bef = [0] * leni2
        leni1 = len(num1Bef)
        for i in range(leni2):
            arr2Bef[i] = int(num2Bef[i])
        for i in range(leni1):
            arr1Bef[i] = int(num1Bef[i])
    else:
        num1Bef = '0' * abs(leni2 - leni1) + num1Bef
        leni2 = len(num2Bef)
        arr1Bef = [0] * leni2
        arr2Bef = [0] * leni2
        leni1 = len(num1Bef)
        for i in range(leni2):
            arr2Bef[i] = int(num2Bef[i])
        for i in range(leni1):
            arr1Bef[i] = int(num1Bef[i])
    return arr1Bef, arr2Bef


def createAft(num1, num2):
    num1 = str(float(num1))
    num2 = str(float(num2))
    num1Aft = num1.split('.')[1]
    num2Aft = num2.split('.')[1]
    leni1 = len(num1Aft)
    leni2 = len(num2Aft)
    if leni1 > leni2:
        arr1Aft = [0] * leni1
        arr2Aft = [0] * leni1
        leni2 = len(num2Aft)
        for i in range(leni1 - 1, -1, -1):
            arr1Aft[i] = int(num1Aft[i])
        for i in range(leni2):
            arr2Aft[i] = int(num2Aft[i])
    else:
        arr1Aft = [0] * leni2
        arr2Aft = [0] * leni2
        leni1 = len(num1Aft)
        for i in range(leni2 - 1, -1, -1):
            arr2Aft[i] = int(num2Aft[i])
        for i in range(leni1):
            arr1Aft[i] = int(num1Aft[i])
    return arr1Aft, arr2Aft


def minus(num1, num2):
    arr1Bef, arr2Bef = createBef(num1, num2)
    arr1Aft, arr2Aft = createAft(num1, num2)
    dotInd = len(arr1Bef)
    flag = 0
    arr1 = arr1Bef + arr1Aft
    arr2 = arr2Bef + arr2Aft
    if maximum_value(arr1, arr2, dotInd) == 1:
        arrResult = countMinus(arr1, arr2)
    else:
        arrResult = countMinus(arr2, arr1)
        flag = 1
    strResult = ''
    for i in range(len(arrResult)):
        strResult = strResult + str(arrResult[i])
    strResult = list(str(int(strResult)))
    if flag == 1:
        strResult.insert(dotInd - 1, '.')
    else:
        strResult.insert(dotInd - 1, '.')
    if flag == 1:
        strResult = '-' + ''.join(strResult)
    else:
        strResult = ''.join(strResult)
    return strResult



# def main():
#     print(work_with_row('110.011*10.01'))
#
#
# if __name__ == '__main__':
#     main()
