import sys

S = input()
lst = sorted(list(S))
palindrome_lst = []
even = len(lst) % 2 - 1
odd = len(lst) % 2
cnt = 0
odd_lst = []
if even:
    for i in range(0, len(lst), 2):
        if lst[i] == lst[i + 1]:
            palindrome_lst.append(lst[i])
        elif lst[i] != lst[i + 1]:
            print("I'm Sorry Hansoo")
            palindrome_lst = []
            break
    result = palindrome_lst + palindrome_lst[::-1]
    if result:
        print("".join(result))
elif odd:
    for i in range(0, len(lst), 2):
        if cnt == len(lst) - 1:
            odd_lst.append(lst[cnt])
            break
        elif lst[cnt] == lst[cnt + 1]:
            palindrome_lst.append(lst[i])
            cnt += 2
        elif lst[cnt] != lst[cnt + 1]:
            odd_lst.append(lst[cnt])
            cnt += 1
        if len(odd_lst) == 2:
            print("I'm Sorry Hansoo")
            palindrome_lst = []
            odd_lst = []
            break
    result = palindrome_lst + odd_lst + palindrome_lst[::-1]
    if result:
        print("".join(result))