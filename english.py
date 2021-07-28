import random

words = {
    "words": {
        "lesson_1": [
            ["昨晚在晚会上你玩得开心吗？（have a great time）", "Did you have a great time at the party last night?"],
            ["这个学期她选修了英语、计算机和驾驶三门课程。（take a course）", "This term she has taken courses in English, computers/computing, and driving."],
            ["朋友帮了他很多忙，他欠他们的情。（have a debt）", "He has a debt to his friends who have helped him a lot."],
            [" 我明白了一个道理：永远不要让你的朋友失望。（let down）", "I have learnt one thing: never let your friends down."]
        ],
        "lesson_2": [
            ["假如你让他待在你家，你就是在自找麻烦。（ask for）", "If you let him stay at your home, you are asking for trouble."],
            ["善于学习语言的人能够把他们的错误变成通向成功的一大步。（turn...into）", "Good language learners can turn their mistakes into a big step toward their success"],
            ["这次事故（accident）给了他一个教训，从此他再也不会酒后驾车了。（teach someone a lesson）", "The accident taught him a lesson, and from then on, he would never drive a car after drinking"],
            ["我们都应该以李明为榜样，学好英语。（take a leaf out of someone's book）", "We should all take a leaf out of Li Ming's book and learn English well."]
        ],
        "lesson_3": [
            ["出于同情，布莱克太太（Mrs. Black）给了这位可怜的老人一些钱。（out of sympathy）", "Out of sympathy, Mrs. Black gave some money to the poor old man."],
            ["英语教师指着一个苹果用英语对全班同学说：“这是一个苹果。”（point to）", "The English teacher pointed to an apple and said to the whole class in English: 'This is an apple'"],
            ["当我们互相帮助时，我们的房间里就充满了爱。（be filled with）", "Our room is filled with love when we help each other."],
            ["我们应该听从这位老人的劝告，现在就回家去。（take someone's advice）", "We should take the old man's advice and go home right now."]
        ],
        "lesson_4": [
            ["虽然有战争的威胁（threat），人们仍一如既往地工作着。（go about）", "Despite the threat of war, people went about their work as usual."],
            ["请允许我就这些问题讲几句话。（allow somebody to do）", "Please allow me to say a few words about the problems."],
            ["她站起身来惊讶地盯着我。（stare at）", "She stood up and stared at me in surprise."],
            ["大火迅速蔓延到大楼的其他部分。（spread）", "Fire quickly spread to the other parts of the building."]
        ],
        "lesson_5": [
            ["人们期望看到有更多的优秀球员到国外去打篮球。（look forward to）", "People look forward to seeing more excellent players play basketball abroad."],
            ["球迷们都围着他要签名。（surround）", "The football fans surrounded him and asked for his signature."],
            ["她没有足够的力气来推开这扇门。（strength）", "She doesn't have enough strength to push this door open."],
            ["你应该意识到担心是无济于事的，你该做点什么才行。（aware）", "You should be aware that it is no use worrying; you need to do something about it."]
        ],
        "lesson_6": [
            ["政府要在附近（neighborhood）建一个新的购物中心。（put up）", "The government is going to put up a new shopping center in the neighborhood."],
            ["一个愚蠢的错误就能给你带来许多麻烦。（involve）", "One foolish mistake can involve you in a good deal of trouble."],
            ["他知道从错误中学习的重要性。（importance）", "He knew the importance of learning from mistakes."],
            ["成功是不能用（in terms of）金钱来衡量的。（measure）", "Success cannot be measured in terms of money."]
        ],
        "lesson_7": [
            ["根据一个古老的习俗，新娘应该戴婚礼面纱。（according to）", "According to an old custom, the bride should wear a wedding veil."],
            ["“4”这个数字在中文里听上去与“死”很接近。（sound close to）", """"4" is a number that sounds close to the word "death" in Chinese."""],
            ["在欢迎会上，学生代表上台发了言。（reception）", "At the welcome reception, a student representative made a speech."],
            ["买衬衣之前最好试穿一下。（try on）", "You'd better try it on before you buy a shirt."]
        ],
        "lesson_8": [
            ["在西方人看来，与人交谈时不看着对方的眼睛是很不礼貌的。（have a conversation）", "To Westerners, it is very impolite not to look at his or her eyes while having a conversation with him or her."],
            ["有的手势在不同的文化中表达的意思完全相反。（entirely）", "In different cultures, some gestures have entirely different meanings."],
            ["库克先生不仅能左手使筷子（chopsticks），而且还能用左手写字。（what is more）", "Mr. Cook can use chopsticks with his left hand, and what's more, he can write with his left hand, too."],
            ["他的优点之一就是敢于向权威挑战。（challenge）", "One of his strong points is that he dares to challenge the authority."]
        ],
        "lesson_9": [
            ["我们刚要开始比赛就下起了雨。（be about to）", "We were about to start the race when it rained."],
            ["北方冬季寒冷，而相比之下南方却相当温暖。（in contrast）", "In winter, it's cold in the north. In contrast, it's pretty warm in the south."],
            ["约翰没来是因为生病了，而你的情况却不同。（in one's case）", "John was absent from class because he was ill, but it was different in your case."],
            ["关于你的请求（request），我恐怕无法马上给予答复。（with regard to）", "With regard to your request, I'm afraid I can't give you an immediate reply."]
        ],
        "lesson_10": [
            ["等他到机场时，飞机已经起飞了。（by the time）", "By the time he arrived at the airport, the plane had taken off."],
            ["在校园（campus）里，车速被限制在每小时30英里。（be limited to）", "On the campus, the car speed is limited to 30 miles per hour."],
            ["这对双胞胎姐妹（twin sisters）之间的不同之处在于：一个依赖父母，另一个却很独立。（one one's own）", "The difference between the twin sisters is that one is dependent on her parents, and the other is on her own."],
            ["一方面汽车有用，可另一方面它们也造成污染（pollution）。（on the one hand... on the other hand）", "On the one hand, cars are useful, but on the other (hand), they cause pollution."]
        ],
        "lesson_11": [
            ["房子着火了，里面的人面临着死亡的危险。（in danger of）", "The house was on fire and people inside were in danger of losing their lives."],
            ["他买不起这么好的房子。（afford to do）", "He cannot afford to buy such a nice house."],
            ["这个主意听起来也许有些怪，不过还真有点道理。（make sense）", "Although this idea may sound strange, it does make sense."],
            ["约翰看起来是个好人。即便如此，我还是不信任他。（even so）", "John seems (to be) a nice person. Even so, I don't trust him."]
        ],
        "lesson_12": [
            ["如果他一开始谈论过去，你就永远都没法从他那儿脱身。（get away from）", "If he starts talking about the past, you'll never get away from him."]
        ]
    }
}

while True:
    lesson = input("请输入你想考核的单元.\n")
    try:
        lesson = int(lesson)
        if lesson > 11:
            print("数值超出支持范围, 支持(1-11)")
            continue
        else:
            break
    except Exception as e:
        print("未知错误")

random_arr = []
while True:
    if len(random_arr) == 4:
        break
    random_num = random.randint(0, 3)
    if random_num in random_arr:
        continue
    else:
        arr = words["words"]["lesson_{}".format(lesson)][random_num]
        answer = input(arr[0] + "\n")
        print("{}".format(arr[1]))
        print(" ")
        random_arr.append(random_num)