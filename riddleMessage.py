# Author --dahai--


# 输出彩色打印消息
# print 带颜色输出格式
#   开头部分： \033[显示方式;前景色;背景色 m
#   结尾部分： \33[0m
#   backColorNuM: 0 - 7
#   color: 黑色，红色，绿色，黄色，蓝色，紫红色，青蓝色，白色 (40-47)
def colorPrint(str_input, backColorNum):
    title = "\033["
    end = "\033[0m"

    backColorStr = str(backColorNum + 40) + "m"

    str_colorPrint = title + backColorStr + str_input + end
    print(str_colorPrint)

'''
# 寓言谜语1
riddle_message1_0 = "这则寓言故事出自《庄子·秋水》..."
riddle_message1_1 = "这则寓言故事中出现了两种动物..."
riddle_message1_2 = "这则寓言文言文中有一句话是这样写的 “井蛙不可以语于海者，拘于虚也。” "
riddle_message1_3 = "这则寓言故事告诉我们不要做见识短浅，思路狭窄的人。要做见多识广，知识渊博的人。"
riddle_answer1 = "井底之蛙"

riddle_question1 = [riddle_message1_0,riddle_message1_1,riddle_message1_2,riddle_message1_3,riddle_answer1]

# 寓言谜语2
riddle_message2_0 = "这则寓言故事出自《韩非子•五蠹》..."
riddle_message2_1 = "这则寓言故事出现了一种农具是耒(lěi)..."
riddle_message2_2 = "这则寓言故事中的人物由于自己的行为得到了宋国人的耻笑。 ..."
riddle_message2_3 = "这则寓言故事的近义词是坐享其成、好逸恶劳。..."
riddle_answer2 = "守株待兔"

riddle_question2 = [riddle_message2_0,riddle_message2_1,riddle_message2_2,riddle_message2_3,riddle_answer2]

riddle_message = [riddle_question1,riddle_question2]
riddle_message_lens = len(riddle_message)
'''

##  从文件中读取谜语信息
riddle_list = []
riddle_total_cnt = 0

def  readRiddleMessageFromFile():
    fileName = "riddleMessage.txt"
    total_cnt = 0
    with open(fileName, 'r', encoding='utf-8') as f1:
        riddle_quest = []
        append_flag = False
        for line in f1:
            if "=== start ===\n" in line:
                append_flag = True
                continue
            if "=== end ===" in line:
                append_flag = False
                total_cnt += 1
                riddle_list.append(riddle_quest)
                riddle_quest = []

            if append_flag == True:
                riddle_quest.append(line.strip())
                # print(line.strip())

    return total_cnt

if __name__ == "riddleMessage":
    riddle_total_cnt = readRiddleMessageFromFile()
