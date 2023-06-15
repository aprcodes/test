try:
    # number = input()
    # # reversed = int(number[::-1])
    # # print(reversed)
    number = int(input())

    reversed = 0
    while number > 0:
        extract_digit = number%10
        reversed = reversed * 10 + extract_digit
        number //=10
    print(reversed)
    
except ValueError:
    print('Invalid entry')
    