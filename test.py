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
    resultAfterDot, saveElementAfterDot = countSummAfterDot(num1, num2)
    resultBeforeDot = countSummBeforeDot(num1, num2)
    resultBeforeDot = countSummBeforeDot(resultBeforeDot, str(saveElementAfterDot) + '.0')
    return resultBeforeDot + '.' + resultAfterDot


def main():
    print(countSumm('101010.01011', "111101.01010"))


if __name__ == '__main__':
    main()