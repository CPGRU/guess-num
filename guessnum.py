#產生一個隨機數1到100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對:印出"恭喜終於猜對了!"
#猜錯:印出比答案大小提示

import random
r = random.randint(1,100)
while True:
    num = input('請猜數字: ')
    num = int(num)
    if r < num :
        print('比答案大')
    elif r > num:
        print('比答案小')
    else:
        print('恭喜終於猜對!')
        break