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
            ["如果他一开始谈论过去，你就永远都没法从他那儿脱身。（get away from）", "If he starts talking about the past, you'll never get away from him."],
            ["冬天失业率有上升的趋势。（tendency）","There is a tendency for job losses to rise in the winter."],
            ["在我不断地要求下，父亲终于同意和我一起去澳大利亚了。（frequent）", "Because of my frequent demands, father finally agreed to go to Australia with me."],
            ["他把老店卖了，开了一家新店，以便赚更多的钱。（make money）", "He sold his shop and opened a new one to make more money."]
        ],
        "lesson_13": [
            ["我们应该从失败中吸取教训, 这是很重要的。（learn a lesson from）", "It is important for us to learn a lesson from the failure."],
            ["他相信自己想当证券经纪人的梦想总有一天会实现。（come true）", "He believes that one day his dream of becoming a stockbroker will come true."],
            ["很多学生最后从事的工作不需要用到所学的知识。（end up）", "Many students end up doing jobs that do not make use of what they have learnt."],
            ["我一提到他的名字，母亲就变得很不开心。（as soon as）", "As soon as I mentioned his name, my mother became very unhappy."]
        ],
        "lesson_14": [
            ["只要你经常锻炼， 你又会变得健康起来。（as long as）", "As long as you get regular exercise, you will become healthy again."],
            ["我一直想读一本有关太空的书，但是我好像总没时间去读。（get around to）", "I have always been thinking of reading a book on space, but I never seem to get around to it."],
            ["那位作家自从买了电脑后，就再也不用笔写小说了。（no longer）", "Since the writer had bought the computer, he no longer wrote his stories with a pen."],
            ["学校制定了一些新的规章制度，人人必须遵守。（set up）", "The school has set up some new rules that everybody must follow."],
        ],
        "lesson_15": [
            ["看见大海，孩子们开心得大叫起来。（at the sight of）", "The children cried with delight at the sight of the sea."],
            ["你刚刚说的话我没太听懂，你能再说一遍吗？（catch on）", "I didn't quite catch on to what you said just now. Would you say it again?"],
            ["他知道那项任务很难，但还是接受了。（be conscious of）", "He was conscious of the difficulty of the task, but he still accepted it."],
            ["直到现在，每当想起那天发生的事情时，我还是觉得莫名其妙。（to this day）", "To this day, when I recall what happened that day, I still feel confused."]
        ],
        "lesson_16": [
            ["她似乎以贬低别人为快。（speak poorly of）", "She seems to enjoy speaking poorly of others."],
            ["他过度地喝酒抽烟，结果死了。（as a consequence of）", "He died as a consequence of heavy drinking and smoking."],
            ["你永远无法从他那儿得到直接的回答。（get... out of）", "You can never get a straight answer out of him."],
            ["我们的产品在过去几年中逐渐受到欢迎。（little by little）", "Our products have become popular little by little over the past few years."]
        ],
        "lesson_17": [
            ["我们明天就该开始进行那个项目了，可你却还没有准备好。（work on）", "We are supposed to start working on that project tomorrow, but you haven't got things ready."],
            ["我今晚得把工作赶完，所以我不能和你一起去看电影了。（catch up on）", "I have to catch up on my work tonight, so I can't go to the movies with you."],
            ["约翰不习惯这儿的新生活，所以打算搬走。（be accustomed to）", "John wants to move because he is not accustomed to the new life here."],
            ["她伸手拿起电话，拨了一个朋友的号码。（reach for）", "She reached for her telephone and dialed the number of a friend."]
        ],
        "lesson_18": [
            ["这个计划听起来虽然很难，但他决心将它付诸实施。（put something into practice）", "Difficult as the plan sounds, he is determined to put it into practice."],
            ["面对这么多的困难，球队怎么能赢得比赛呢？（in the face of）", "How could the team win the game in the face of so many difficulties?"],
            ["自两年前开业以来, 今年年初他的生意最兴隆。（at one's best）", "His business was at its best at the beginning of this year since it was started two years ago."],
            ["他虽然没有直说，但我们能从他的手势中得到一些信息。（pick up）", "Although he didn't say it directly, we could pick up some messages from his gestures."]
        ],
        "lesson_19": [
            ["我们必须想出解决这个问题的办法。（figure out）", "We must figure out how to solve the problem. OR: We must figure out the solutions to the problem."],
            ["他看着包，像是在看着一件他看不懂的东西。（beyond one's comprehension）", "He looked at the bag as if he were looking at something beyond his comprehension."],
            ["我会使用计算机，但是说到修计算机，我是一无所知。（come to）", "I know how to use a computer, but when it comes to repairing it, I know nothing about it."],
            ["我们迷了路，更糟的是，天开始下雨了。（what's worse）", "We got lost. What's worse, it started to rain."]
        ],
        "lesson_20": [
            ["学经验使她具有担任此项工作的条件。（qualify for）", "Her teaching experience qualifies her for the job."],
            ["不适用于海外合资企业。（apply to）", "The new law does not apply to the joint venture overseas."],
            ["如果你已决定租这所房子，请先付50美元。（in advance）", "If you have decided to rent this house, please pay 50 dollars in advance."],
            ["一入境就被捕了。（upon/on entry to）", "Upon entry to the country, he was arrested."]
        ]
    }
}

print("请输入你想使用的功能的序号：")
print("1.单元考核")
print("2.全局随机抽考")
print("请输入1或2")
func_select = int(input())

if func_select == 1:
    while True:
        lesson = input("请输入你想考核的单元.\n")
        try:
            lesson = int(lesson)
            if lesson > 20:
                print("数值超出支持范围, 支持(1-20)")
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

elif func_select == 2:

    words_exist = []
    count = 0

    print("请输入你想考核的个数:")
    exam_num = int(input())

    while True:
        lesson_random = random.randint(1, 20)
        words_random = random.randint(0, 3)

        if count == 4:
            break

        if [lesson_random, words_random] in words_exist:
            continue
        else:
            arr = words["words"]["lesson_{}".format(lesson_random)][words_random]
            answer = input(arr[0] + "\n")
            print("{}".format(arr[1]))
            print(" ")
            words_exist.append([lesson_random, words_random])
            count += 1