for i in range(10):
    if i == 3:
        continue
        # break
    print(i)
else:
    print('done loop')


num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    # if num == 7:
    #     break
    print(num)
    num += 1
else:
    print('done while loop')
