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


def main():
    print(minus('1.0', "100.0"))


if __name__ == '__main__':
    main()