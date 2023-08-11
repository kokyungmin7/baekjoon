import sys

H = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

number_dic_en = {
    0: "o' clock", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
    12: "twelve", 13: "thirteen", 14: "fourteen", 15: "quarter",
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    20: "twenty", 21: "twenty one", 22: "twenty two", 23: "twenty three", 24: "twenty four",
    25: "twenty five", 26: "twenty six", 27: "twenty seven", 28: "twenty eight", 29: "twenty nine", 30: "half"}

if 30 < M:
    m = 60 - M

if M == 0:
    print(number_dic_en[H], number_dic_en[M], sep=' ')
elif M < 30:
    if M == 15:
        print(number_dic_en[M], 'past', number_dic_en[H], sep=' ')
    elif M == 1:
        print(number_dic_en[M], 'minute past', number_dic_en[H], sep=' ')
    else:
        print(number_dic_en[M], 'minutes past', number_dic_en[H], sep=' ')
elif M == 30:
    print(number_dic_en[M], 'past', number_dic_en[H], sep=' ')
elif M > 30:
    M = 60 - M
    if M == 15:
        print(number_dic_en[M], 'to', number_dic_en[H+1 if H < 12 else 1], sep=' ')
    elif M == 1:
        print(number_dic_en[M], 'minute to', number_dic_en[H+1 if H < 12 else 1], sep=' ')
    else:
        print(number_dic_en[M], 'minutes to', number_dic_en[H+1 if H < 12 else 1], sep=' ')
