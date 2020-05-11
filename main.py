# Author --dahai--

#  编写一个根据提示，猜成语名字的小程序

import riddleMessage as ridMess

welcome_info = '''
=========================================
【欢迎小朋友参加根据信息，猜语言故事的小游戏】
=========================================
计分规则：
    1.  如果根据一条信息，猜对答案，计4分；
    2.  如果根据二条信息，猜对答案，计4分；
    3.  如果根据三条信息，猜对答案，计4分；
    4.  如果根据四条信息，猜对答案，计4分；
    5.  如果没有猜到答案，计0分；
'''

def guess_riddle(guessCount):
    score = 0
    riddleMessage = ridMess.riddle_list[guess_count]
    # for  line in riddleMessage:
    #     print(line)

    for i in range(1,5):
        for j in range(i):
            print("%s. %s" %(j+1,riddleMessage[j]))
        ans_c = input("请输入你的答案：")
        if ans_c == riddleMessage[4]:
            print("你太棒了，答对了...")
            score = 4 - j
            return score

    print("你没有答对这个题目，答案是：%s" %riddleMessage[4])
    return score


guess_count = 0                       #  猜题计数
guess_score = []
guess_score_totle = 0
if __name__ == "__main__":
    print(welcome_info)
    # guess_total = ridMess.readRiddleMessageFromFile()
    ans = input("你准备好答题了吗？(Y or N):")
    if ans == 'Y' or ans == 'y':
        guess_total = ridMess.riddle_total_cnt
        for i in range(guess_total):
            print("本次答题总共有%s个谜语，现在开始第%s个谜语" %(guess_total,guess_count+1))
            riddle_score = guess_riddle(guess_count)
            guess_score_totle += riddle_score
            guess_score.append(riddle_score)
            print("\033[43:2m第%s个谜语，你得了%s分，共计%s分...\033[0m" %(guess_count+1,riddle_score,guess_score_totle))
            guess_count += 1

        print("共计%s分，你答题情况如下：" %guess_score_totle)
        for index,i in enumerate(guess_score):
            if i > 2:
                print("第%s题: %s分" %(index, i))
            else:
                ridMess.colorPrint(("第%s题: %s分" %(index, i)),1)
    else:
        ridMess.colorPrint("你还没准备好答题，下次再来吧...",1)
