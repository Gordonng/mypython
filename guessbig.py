import time
import random

# 讓使用者註冊
name = input('請填寫使用者名稱：')
age = input("{}您好，請輸入您的年齡 : ".format(name))
user_info = "[name,age]"   # 使用者資訊
user_properties = ['x 1-5']  # 用於存放使用者道具 預設道具
properties = ['x3 (250g)', 'x1-5 (300g)']  # 道具列表 顯示用

# 根據使用者年齡 給與不同的初始金幣
if 10 < user_info['age'] < 18:
    glod = 1000
elif 18 <= user_info['age'] <= 30:
    glod = 1500
else:
    glod = 500
    user_info['glod'] = glod

# 輸出相關提示資訊
print("\n")
time.sleep(1)
print('遊戲說明'.center(50, '*'))
print('*'.ljust(53), '*')
print('*', end='')
print("電腦每次投擲三枚骰子，總點數》=10為大，否則為小".center(32), end='')
print('*')
print('*'.ljust(53), '*')
print('*' * 54)
print("\n")

#             開始遊戲
result = input('是否開始遊戲 yes or no :  ')
go = true
if (result.lower() == 'yes'):
    while go:
        dices = ""
        # 開始投擲
        for i in range(0, 3):
            total = sum(dices)                          # 計算總和
            user_input = input('請輸入big or small : ')  # 等待使用者輸入
            u_input = user_input.strip().lower()
            time.sleep(1)

            # 判斷使用者輸入
            print('骰子點數為：{}'.format(dices), end=' ')

            if (total >= 10 and u_input == 'big') or (total < 10 and u_input == 'small'):
                print('您贏了!!!')
                multi = 1                               # 倍數

                if len(user_properties) > 0:            # 如果使用者有道具 選擇是否使用道具
                    use_pro = input('是否使用道具： ')
                    if use_pro.lower() == 'yes':
                        use_pro = int(input('請選擇使用第幾個道具{} ：'.format(user_properties)))
                        use_pro -= 1

                        # 判斷道具型別
                        if user_properties[use_pro] == 'x 3':
                            multi = 3
                            print('獎金翻3倍')
                        elif user_properties[use_pro] == 'x 1-5':
                            multi = random.randint(1, 5)
                            print('獎金翻{}倍'.format(multi))
                            user_properties.remove(user_properties[use_pro])  # 刪除道具
                            user_info['glod'] += 100 * multi;  # 金額增加
                        else:
                            print('您輸了!')
                            user_info['glod'] -= 100;  # 錯誤 使用者金幣減 100

                            # 判斷使用者金幣 是否夠下次玩 不夠則退出程式
                            if (user_info['glod'] <= 0):
                                break
        if user_info['glod'] % 1000 == 0:  # 使用者金幣 是1000的倍數是 可購買道具
            shop = input('您現在有金幣:{}，是否購買道具 yes or no: '.format(user_info['glod']))
            if shop.lower() == 'yes':
                good_num = int(input('請選擇要購買第幾個道具 {}'.format(properties)))
                if good_num == 1:
                    user_info['glod'] -= 250
                    print('購買成功！消耗金幣250')
                elif good_num == 2:
                    user_info['glod'] -= 300  # 使用者金幣減 300
                    print('購買成功！消耗金幣300')
                else:
                    print('沒有該道具，您失去了這次機會')
            else:
                #  一直提示 太煩
                # conti = input('您現在有金幣:{}，是否繼續遊玩,yes or no: '.format(user_info['glod']))
                print('您現在有金幣:{} '.format(user_info['glod']))
        else:
            print('歡迎下次遊玩，再見！')
