num = int(input('num: '))

while num != 1:
    t = (0, -1, 1)
    print('{} {}'.format(num, t[num % 3]))
    num = int((num + t[num % 3]) / 3)
print(num)

# Explanation
# result = num % 3
# if result is 0, you can divide num by 3
# if result is 1, you need to subtract 1 from num in order to divide num by 3
# if result is 2, you need to add 1 to num in order do divide num by 3
# the tuple (0, -1, 1) represents this, and the correct index gets grabbed with (0, -1, 1)[num % 3]
