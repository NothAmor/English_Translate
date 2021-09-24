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
            ["这次事故（accident）给了他一个教训，从此他再也不会酒后驾车了。（teach someone a lesson）", "The accident taught him a lesson, and from then on, he has never driven a car after drinking."],
            ["我们都应该以李明为榜样，学好英语。（take a leaf out of someone's book）", "We should all take a leaf out of Li Ming's book and learn English well."]
        ],
        "lesson_3": [
            ["出于同情，布莱克太太（Mrs. Black）给了这位可怜的老人一些钱。（out of sympathy）", "Out of sympathy, Mrs. Black gave some money to the poor old man."],
            ["英语教师指着一个苹果用英语对全班同学说：“这是一个苹果。”（point to）", "The English teacher pointed to an apple and said to the whole class in English: 'This is an apple'"],
            ["当我们互相帮助时，我们的房间里就充满了爱。（be filled with）", "Our room is filled with love when we help each other."],
            ["我们应该听从这位老人的劝告，现在就回家去。（take someone's advice）", "We should take the old man's advice and go home right now."]
        ],
        "lesson_4": [
            ["老师对学生上课迟到很生气，就把那些迟到的学生关在了门外。(shut out)", "The teacher felt soangry with the students for being late that he/she shut them out."],
            ["小男孩伸出一只手去拿桌子上的书。(reach for)", "The young boy reached for the book on the desk with one of his hands"],
            ["你们不应该在上班时间玩电脑游戏。(at work)", "You are not supposed to play computer games while at wo"],
            ["经理亲自出马参加面试。(in person)", "The manager took part in the interview in person."]
        ],
        "lesson_5": [
            ["二十年后，李娜脱颖而出成为中国最伟大的女子网球运动员。(stand out)", "Twenty years later, Li Na stands out as the greatest woman tennis player in China."],
            ["老师鼓励这个男孩学画画，并告诉他说他是独一无二的。(one-of-a-kind)", "The teacher encouraged the boy to learn to draw and told him he was one-of-a-kind"],
            ["如果你不喜欢这个计划，你可以退出。(drop out)", "If you don't like the plan, you can drop out."],
            ["难道你相信他？我敢肯定他知道的比他说出来的多。(let on)", "Do you believe him?I'm sure he knows more than he's letting on."]
        ],
        "lesson_6": [
            ["政府要在附近（neighborhood）建一个新的购物中心。（put up）", "The government is going to put up a new shopping center in the neighborhood."],
            ["一个愚蠢的错误就能给你带来许多麻烦。（involve）", "One foolish mistake can involve you in a good deal of trouble."],
            ["他知道从错误中学习的重要性。（importance）", "He knew the importance of learning from mistakes."],
            ["成功是不能用（in terms of）金钱来衡量的。（measure）", "Success cannot be measured in terms of money."]
        ],
        "lesson_7": [
            ["最好的办法是学生和老师都参与课外活动(get involved in)", "The best way is that both students and teachers get involved in extracurricular activities."],
            ["平安夜是全体家庭成员欢聚一堂的温馨(heart-warming)时刻。(gather together)", "Christmas Eve is a heart-warming time for the family members to gather together."],
            ["我认为我们可以通过参加学校的社会活动接触社会和他人。(get in touch with)", "I think we can get in touch with the world and others through social activities on campus"],
            ["人们住在这座古老的小镇里，生活简单安宁,四周树木环绕。(surround)", "People live in this old small town，having a simple and peaceful life， surrounded by trees"]
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
            ["冬天失业率有上升的趋势。（tendency）", "There is a tendency for job losses to rise in the winter."],
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
            ["当时的局面很艰难,但她顺利地应付过去了。(deal with)", "It was a difficult situation but she dealt with it successfully."],
            ["学校和家长不应该只关注考试的结果。(focus on)", "Schools and parents should not focus only on exam results."],
            ["我们应该明白，年轻人时不时地犯错是很正常的。(every now and then)", "We need to understand that it's common for young people to make mistakes every now and then."],
            ["这位母亲从不在孩子们面前说中文，他们因此习惯了听她说英语。(be used to)", "The mother never speaks Chinese in front of her children, so that they are used to hearing English from her"],
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
            ["患重病常常导致失去自信和自尊。(resultin)", "Serious illness often resultsin a loss of confidence and self-respect."],
            [".犯罪常常和贫穷以及失业有关。(be related to)", "Crime is often related to poverty and unemployment."],
            ["琼斯先生以前是百万富翁，他不甘心接受贫穷。(come to terms with)", "Mr. Jones was once a millionaire and he can't come to terms with being poor."],
            ["快一点,我们没时间了。(run out)", "Hurry up! We are running out our time."]
        ],
        "lesson_18": [
            ["这个计划听起来虽然很难，但他决心将它付诸实施。（put something into practice）", "Difficult as the plan sounds, he is determined to put it into practice."],
            ["面对这么多的困难，球队怎么能赢得比赛呢？（in the face of）", "How could the team win the game in the face of so many difficulties?"],
            ["自两年前开业以来, 今年年初他的生意最兴隆。（at one's best）", "His business was at its best at the beginning of this year since it was started two years ago."],
            ["他虽然没有直说，但我们能从他的手势中得到一些信息。（pick up）", "Although he didn't say it directly, we could pick up some messages from his gestures."]
        ],
        "lesson_19": [
            ["我们必须想出解决这个问题的办法。（figure out）", "We must figure out how to solve the problem."],
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
            if answer.lower() == arr[1].lower():
                print("正确")
            else:
                print("请确认是否正确")
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

        if count == exam_num:
            break

        if [lesson_random, words_random] in words_exist:
            continue
        else:
            arr = words["words"]["lesson_{}".format(lesson_random)][words_random]
            answer = input(arr[0] + "\n")
            print("{}".format(arr[1]))
            if answer.lower() == arr[1].lower():
                print("正确")
            else:
                print("请确认是否正确")
            print(" ")
            words_exist.append([lesson_random, words_random])
            count += 1
