#產生一個隨機數1到100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對:印出"恭喜終於猜對了!"
#猜錯:印出比答案大小提示

import random
start = input('請輸入隨機數開始值: ')
end = input('請輸入隨機數結束值: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
    count += 1 #count = count + 1
    num = input('請猜數字: ')
    num = int(num)
    if r < num :
        print('比答案大')
    elif r > num:
        print('比答案小')
    else:
        print('恭喜終於猜對!')
        print('這是你猜的第',count, '次')
        break
    print('這是你猜的第',count, '次')