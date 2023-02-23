def itoa(number):

    result = '' #number의 문자열을 저장할 변수
    while number > 0:
        #1. 숫자의 첫째자리 수를 문자로 변환해서 result 문자열에 더해주는 과정
        result = chr((ord('0') + number % 10)) + result
        #2. number = number //10
        number = number // 10
    return result
if __name__ == '__main__':
    num = 123
    string = itoa(num)
    print(string)