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
            ["老师对学生上课迟到很生气，就把那些迟到的学生关在了门外。(shut out)", "The teacher felt so angry with the students for being late that he/she shut them out."],
            ["小男孩伸出一只手去拿桌子上的书。(reach for)", "The young boy reached for the book on the desk with one of his hands."],
            ["你们不应该在上班时间玩电脑游戏。(at work)", "You are not supposed to play computer games while at work."],
            ["经理亲自出马参加面试。(in person)", "The manager took part in the interview in person."]
        ],
        "lesson_5": [
            ["二十年后，李娜脱颖而出成为中国最伟大的女子网球运动员。(stand out)", "Twenty years later, Li Na stands out as the greatest woman tennis player in China."],
            ["老师鼓励这个男孩学画画，并告诉他说他是独一无二的。(one-of-a-kind)", "The teacher encouraged the boy to learn to draw and told him he was one-of-a-kind."],
            ["如果你不喜欢这个计划，你可以退出。(drop out)", "If you don't like the plan, you can drop out."],
            ["难道你相信他？我敢肯定他知道的比他说出来的多。(let on)", "Do you believe him? I'm sure he knows more than he's letting on."]
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
            ["人们住在这座古老的小镇里，生活简单安宁,四周树木环绕。(surround)", "People live in this old small town，having a simple and peaceful life，surrounded by trees"]
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
            ["患重病常常导致失去自信和自尊。(result in)", "Serious illness often results in a loss of confidence and self-respect."],
            ["犯罪常常和贫穷以及失业有关。(be related to)", "Crime is often related to poverty and unemployment."],
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

single_choice = {
    "single_choice": {
        "lesson_1": [[
            ["A good____is the first step to a good job.", "A.education  B.unit  C.text  D.subject", "A"],
            ["College education provide more____for a bright future", "A.lessons B.courses C.opportunities D.subjects", "C"],
            ["He had a___to his wife who gave him the money to start his business.", "A.job B.debt C.chance D.career", "B"],
            ["A____is helpful in looking for a job,but it doesn’t mean a job.", "A.certificate B.grade C.record D.debt", "A"],
            ["If you think getting a certificate means getting a job,you are____yourself. ", "A.keeping B.having C.cheating D.doing", "C"],
            ["Try to have a real_____of the course.Having it on your record doesn’t mean much.", "A.understanding B.understand C.knowing D.know", "A"],
            ["To be honest with yourself is to_______yourself.", "A.look at B.do C.refuse D.respect", "D"],
            ["People often end their letters with “Yours_____”.", "A.truly B.true C.very D.real", "A"]
        ]],
        "lesson_2": [[
            ["All the students in Mrs.Black’s class are working very hard in order to_____themselves in English.", "A. expect B.compare C.improve D.learn", "C"],
            ["We all know that Chinese is our ____ language.", "A. normal B. lucky        C. nice        D. native", "D"],
            ["All the parents are happy that the school  ____  its students with a free lunch.", "A. provides B. masters C. figures   D. teaches", "A"],
            ["I can finish reading a novel in one day if its story  ____ me very much.", "A. understands B. interests C. improves D. respects", "B"],
            ["College students are expected to  ____ second language.", "A. attend       B. adjust   C. master   D. suppose", "C"],
            ["Children learn from watching their parents, in ____ to asking questions.", "A. education B. subject  C. reason  D. addition", "D"],
            ["If you have sleep trouble, a doctor can help you ____ out why it’s happening.", "A. figure      B. decide   C. account D. manage", "A"],
            ["It’s normal to spend two or three years working in one’s own country before working ____", "A. outside      B. overseas   C. at home   D. inside", "B"]
        ]],
        "lesson_3": [[
            ["The____of this country comes from its oil.", "A. wealth  B. view  C. sympathy  D. tale", "A"],
            ["They agreed to meet the____week in the People’s Park", "A.exact  B.following  C.early  D.late", "B"],
            ["Generally speaking(一般来说），views on this subject_____widely", "A.manage  B.succeed  C.graduate  D.differ", "D"],
            ["The sick old man asked the doctor for____ to get better soon.", "A.award  B.advice  C.situation  D.sheet", "B"],
            ["We were all______to hear the news that Tom,the silly boy,had won an award.", "A.fluent  B.rude  C.amazed  D.successful ", "C"],
            ["Tony often____with his wife about money.", "A.argues B.interviews  C.embarrasses  D.improves ", "A"],
            ["The little girl got much____from her father when she told him about her pains", "A.detail  B.energy  C.sympathy  D.suggestion ", "C"],
            ["I’ve learned from my uncle that dogs______people by their smell.", "A.improve  B.recognize  C.expect  D.teach", "B"]
        ]],
        "lesson_4": [[
            ["The driver fell ____ while driving and killed an old man.", "A. sleeping B. asleep C. to sleep D. a sleep", "B"],
            ["Changes were taking place, though at the time no one fully ____ how important these changes were to be", "A. appreciated B. expected C. touched D. begged", "A"],
            ["The mother told her son to _____ putting himself in danger.", "A. run away B. go away C. avoid D. keep away", "C"],
            ["When I was young, I was silly enough to_______ my teachers to know everything.", "A. tell B. ask C. beg D. expect", "D"],
            ["Jack waved his hand as he continued to ______ at the pre-war photograph of the two men.", "A. see B. watch C. touch D. stare", "D"],
            ["A newborn baby needs _____ care and attention", "A. constant B. fluent C. amazed D. pretty", "A"],
            ["He drew me closer until our bodies were ____.", "A. avoiding B. proceeding C. touching D. expecting", "C"],
            ["The company has ____ a new toy and it sells well in the market.", "A. worked B. taken C. opened D. designed", "D"]
        ]],
        "lesson_5": [[
            ["She expects to defend her ____ successfully in the next Olympics (奥林匹克运动会).", "A. tournament B. title C. prize D. personality", "B"],
            ["The defending World Cup ____ was fastest in practice", "A. coach B. title C. champion D. fan", "C"],
            ["He believes that this oil painting ____ among the best in the world.", "A. ranks B. appreciates C. includes D. requests", "A"],
            ["She is living ____ that some players just get better with age.", "A. champion B. heroine C. proof D. memory", "C"],
            ["I had come to know that our Italian ____ had spent many years in New York.", "A. personality B. host C. generation D. double", "B"],
            ["I feel that I can help singers, especially the younger ____ .", "A. champion B. coach C. guy D. generation", "D"],
            ["As a secretary, I have to do lots of things, ____ making coffee for the boss.", "A. including B. in addition C. instead of D. except", "A"],
            ["He’s through to the men’s tennis ____ for the first time.", "A. tournament B. final C. prize D. court", "B"]
        ]],
        "lesson_6": [],
        "lesson_7": [[
            ["There's no supermarket in the ____ area.", "A. immediate  B. temporary  C. recent  D. brief", "A"],
            ["It should also be noted that this issue has aroused the interest of the academic ____ in this country.", "A. club  B. federation  C. organization  D. community", "D"],
            ["He likes to rub shoulders with the students, letting them ____ his happiness.", "A. share  B. create  C. prefer  D. imagine", "A"],
            ["Families, ____ those with young children, have learned a lot from the program.", "A. especial  B. especially  C. particular  D. really", "B"],
            ["I would ____ it if we had a bigger house, but we are not able to buy one.", "A. create  B. prefer  C. share  D. surround", "B"],
            ["Project Hope is a(n) ____ that raises money to build schools and buy books for children in poor areas.", "A. community  B. club  C. organization  D. union", "C"],
            ["Football fans ran onto the training field and ____ the famous coach.", "A. surrounded  B. shared  C. selected  D. gathered", "A"],
            ["The new factory is expected to ____ more than 400 new jobs.", "A. make  B. find  C. create  D. take", "C"],
        ], [
            ["Speech is silver, _____ is golden.", "A. emotion  B. gesture  C. silence  D. conversation", "C"],
            ["The three students ____ to help the disabled children at weekends.", "A. interrupt  B. participate  C. allow  D. volunteer", "D"],
            ["Thousands of college students around the United States ____ in sports.", "A. participate  B. go  C. take  D. volunteer", "A"],
            ["Most colleges will ____ students to change their subject choices in the early weeks of a semester.", "A. ruin  B. allow  C. prefer  D. appreciate", "B"],
            ["The narrator in the story felt ____ when all the kids were staring at him in the silence.", "A. impaired  B. silent  C. bored  D. nervous", "D"],
            ["A slight ____ of the door showed where she was hiding.", "A. movement  B. gesture  C. hug  D. desgin", "A"],
            ["He was very upset because the heavy rain had ____ his painting.", "A. allowed  B. ruined  C. panicked  D. surrounded", "B"],
            ["Don't ____ the speaker now; he will answer questions later.", "A. allow  B. ruin  C. interrupt  D. yell", "C"],
        ]],
        "lesson_8": [[
            ["Born deaf(聋的),she could not use _____language to communicate with us.", "A.nonverbal  B.verbal  C.foreign  D.body", "B"],
            ["Being a(n)_____of America,the famous movie star decided to run for US president.", "A.native  B.male  C.original  D.female", "A"],
            ["One cannot _____across his thoughts to others well if he doesn’t master enough words.", "A.pass  B.hand  C.transport  D.put", "D"],
            ["Could you give me more of his ____information before I agree to interview him?", "A.background  B.underground  C.back  D.behind", "A"],
            ["His _____expression(表情) shows that he is unhappy about that", "A.body  B.hand  C.facial  D.verbal", "C"],
            ["Mom always tells me to work more _____so that I can have more time to play and relax.", "A.efficient B.easily C.ease D.efficiently", "D"],
            ["Though defeated,the guest team ____us to another match this Saturday.", "A.changed  B.wanted  C.challenged  D.made", "C"],
            ["The teacher granted her the ____to be in charge of Group One at the spring-outing(春游).", "A.ability  B.authority  C.certificate  D.authorities", "B"]
        ], [
            ["You must have said something to ____her,as she was crying after talking with you", "A.defend  B.offend  C.confuse  D.direct", "B"],
            ["Do you know why she looks so ____?She got high marks in the final examinations.", "A.cheerful  B.sad  C.angry  D.confused", "A"],
            ["In America,making the ____gesture means”very good”.", "A.thumbs-down  B.small fingers-down  C.small fingers-up D.thumbs-up", "D"],
            ["I didn’t have enough strength to ____him back from beating a man in this way.", "A.put  B.stop  C.hold  D.catch", "C"],
            ["The country has experienced ____changes since the economic reform.", "A.little  B.directly  C.instantly  D.significant", "D"],
            ["We’ve had many ____in working out this problem,so we need your help.", "A.difficulties  B.horror  C.trouble  D.issues", "A"],
            ["This young man always thinks differently from the others,and what’s more,he even behaves in the ____way.", "A.against  B.opposite  C.across  D.another", "B"],
            ["Without careful scientific research,how can they ____that there is no life on that planet (星球)?", "A.draw  B.include  C.result  D.conclude ", "D"]
        ]],
        "lesson_9": [[
            ["In addition to working a full day at his _____, he has to take care of his family", "A.charge  B.company  C.career  D.cash", "B"],
            ["The whole composition is good ____some careless mistakes.", "A.except for  B.except that  C.except  D.except from", "A"],
            ["If you are not careful,you are going to ____the balloon.", "A.win  B.beat  C.empty  D.burst", "D"],
            ["Airline personnel(员工)can buy ____tickets at reduced prices", "A.bus  B.train  C.flight  D.movie", "C"],
            ["Six ____languages are used at the United Nations.", "A.national  B.official  C.native  D.authority", "B"],
            ["We can visit you on Saturday or Sunday.Our plans are fairly ______.", "A.flexible  B.possible  C.impossible  D.personal," "A"],
            ["Modern music may have a _____influence,as well as a positive(积极的) one on teenagers.", "A.good  B.poor  C.nice  D.negative", "D"],
            ["His white hair was in sharp ____to his dark skin", "A.difference  B.contrast  C.opposite  D.background", "B"]
        ]],
        "lesson_10": [[
            ["Students should be encouraged to be ___thinkers.", "A.independent  B.independence  C.advantage  D.average", "A"],
            ["Charlie thinks money will _____all his problem", "A.perform  B.solve  C.score  D.force", "B"],
            ["The doctor was____an operation to save the patient’s life", "A.acting  B.limiting  C.performing  D.assuming ", "C"],
            ["New medicines are ____remarkable results in the treatment of cancer.", "A.finding  B.requiring  C.solving  D.producing", "D"],
            ["You should read more books to enlarge (扩大)your ____.", "A.vocabulary  B.memory  C.brain  D.score ", "A"],
            ["The good weather could be an important _____in tomorrow’s game.", "A.fact  B.factor  C.force  D.activity", "B"],
            ["This kind of plant ____a lot of water at all times", "A.assumes  B.limits  C.produces  D.requires", "D"],
            ["Soldiers are expected to ______orders", "A.obey  B.ask  C.do  D.fear", "A"]
        ]],
        "lesson_11": [],
        "lesson_12": [],
        "lesson_13": [[
            ["The timetable says that the plane ____ off at 8:30 every morning.", "A. took  B. takes  C. is taking  D. had taken", "B"],
            ["For the whole period of two months, there ____ no rain in this area, Now the crops are dead.", "A. is  B. was  C. has been  D. have been", "C"],
            ["The man who spoke at the meeting yesterday ____ his brother.", "A. is  B. was  C. has been  D. had been", "A"],
            ["Has he told you where he ____ his holiday next month?", "A. spent  B. has spent  C. will spent  D. would spend", "C"],
            ["I will have a good time whether I ____.", "A. win or lose  B. won or lost  C. had won or lost  D. would win or lost", "A"],
            ["He'll probably fly on the same plane as I ____ yesterday.", "A. have done  B. will do  C. did  D. do", "C"],
            ["Will you tell us how you ____ to overcome the difficulties last week?", "A. have managed  B. had managed  C. will manage  D. managed", "D"],
            ["She promised to give me whatever help I ____.", "A. will need  B. would need  C. had needed  D. was needing.", "B"]
        ]],
        "lesson_14": [],
        "lesson_15": [[
            ["The speaker ____ for a moment, and then began to answer the question.", "A. shook  B. paused  C. pressed  D. tripped", "B"],
            ["She is so strange. She always tries to ____ talking to me.", "A. prefer  B. protect  C. avoid  D. assure", "C"],
            ["He suffered a serious ____ in the car crash, and died on the way to hospital.", "A. injury  B. accident  C. fall  D. attack", "A"],
            ["It is unnecessary for those who study hard to consider that ____ of failing the exam.", "A. danger  B. warning  C. surprise  D. possibility", "D"],
            ["We often ____ the happy time we spent at your home last summer.", "A. recall  B. remind  C. present  D. provide", "A"],
            ["I'm ____ of his purpose in saying those words, but I don't want to argue with him.", "A. careless  B. conscious  C. content  D. confident", "B"],
            ["While I was walking alone down the street, three man came up to me and asked me for ____ to the beach.", "A. contacts  B. contents  C. materials  D. directions", "D"],
            ["Jack is among the brightest of his ____: He can speak several foreign languages and has won three national prizes.", "A. honor  B. ability  C. generation  D. edge", "C"]
        ]],
        "lesson_16": [],
        "lesson_17": [],
        "lesson_18": [[
            ["It was reported that the earthquake was the most _____ to have struck that area in fifty years.", "A. special B. powerful C. favorite D. exciting", "B"],
            ["It took the experts several months to decide on the ___ for the new airport.", "A. source B. earth C. site D. character", "C"],
            ["The workers are repairing the house. It was _ _ by a fallen tree during the last storm.", "A. struck B. operated C. described D. calculated", "A"],
            ["He was seriously injured in a car __ last year.", "A. shock B. crash C. passage D. mistake", "B"],
            ["They were ____ to hear that their son had been arrested for taking drugs", "A. wandered B. ruined C. prepared D. shocked", "D"],
            ["These events provided the ____ for her first novel.", "A. perspiration B. function C. inspiration D. strength", "C"],
            ["Friends and neighbors can be a good __ of support to families who are experiencing difficulty.", "A. source B. genius C. quality D. equipment", "A"],
            ["I failed to __ Sally to go with me to the party, so I went alone.", "A. handle B. achieve C. inspire D. persuade", "D"]
        ]],
        "lesson_19": [],
        "lesson_20": [[
            ["Unfortunately, we now have plenty of ____ that many children do not do half as well on tests as they actually could if they tried.", "A. evidence  B. blocks  C. suitability  D. instruction", "A"],
            ["A foreigner's first ____ of the US is likely to be that everyone is in a rush-often under pressure.", "A. effect  B. entry  C. impression  D. addition", "C"],
            ["The small country was destroyed by ten years of ____ fighting.", "A. impressive  B. active  C. slim  D. bitter", "D"],
            ["The ____ with the most votes will be elected president of the association, whether he or she wins more than half the votes or not.", "A. emplyer  B. candidate  C. judge  D. assistant", "B"],
            ["Under the team leader's ____, we did very well in the match.", "A. advice  B. hunt  C. suitability  D. guidance", "D"],
            ["Being poor makes many people sad. But in the case of my father, it influences him ____", "A. otherwise  B. equally  C. suitably  D. additionally", "A"],
            ["It's well accepted that we are able to ____ a person by what he or she says.", "A. compose  B. imply  C. judge  D. employ", "C"],
            ["He is more ____ for the job than the other candidates because he has more experience in this field.", "A. favorable  B. suitable  C. equal  D. qualifying", "B"]
        ]],
    }
}

word_select = {
    "word_select": {
        "lesson_1": [[
            "credit,confuse,decide,sense,experience,dorm,saving,comfort,account,suppose",
            [
                ["He has never been away from home.So being homesick is a new ____ to him.", "experience"],
                ["A man should have a(n)____of responsibility for his family.", "sense"],
                ["She is new here.She doesn’t know the way to her ____.", "dorm"],
                ["Being on one’s own means making one’s own ____.", "decisions"],
                ["The best way to keep one’s money safe is to put one’s ____ in a bank.", "savings"],
                ["No ____ cards are accepted in this store.", "credit"],
                ["He is ____ to come at nine o’clock.", "supposed"],
                ["I have a nice, ____ room on the third floor", "comfortable"]
        ]]],
        "lesson_2": [[
            "success,award,manage,interview,embarrass,accent,fluent,risk,reality,situation",
            [
                ["She speaks Japanese with a Chinese ____.", "accent"],
                ["One of the firefighters(消防队员) won a(n) ____ for bravery（勇敢）", "award"],
                ["Hard work and good ideas will lead to ____ in business.", "success"],
                ["Mr.Black ____ famous people every week in his radio program.", "interviews"],
                ["Some young men started smoking without realizing what the____were.", "risks"],
                ["Tony Green has worked very hard to make his dream a(n) ____.", "reality"],
                ["Ann speaks ____ Japanese,as she has lived there for three years.", "fluent"],
                ["The box was very heavy,but Tom still ____ to carry it home.", "managed"]
            ]
        ]],
        "lesson_3": [[
            "various,relative,obvious,secretly,fashionable,whenever,realize,inviation,department,error",
            [
                ["The men from the two countries met ____ because they didn’t want the public(公众）to know about their meeting.", "secretly"],
                ["It was ____ to everyone that the child had been badly treated.", "obvious"],
                ["The teachers are discussing the good points and weak points of ____teaching methods", "various"],
                ["This hat style is now liked by ____ women in Paris", "fashionable"],
                ["Mr.White has got a wedding ____ from his friend in Paris", "invitation"],
                ["I soon ____ that I had made a silly mistake.", "realized"],
                ["You can use my computer____you like.", "whenever"],
                ["The computer made a(n)____on my phone bill(账单）", "error"]
            ]
        ]],
        "lesson_4": [[
            "modern,request,machine,service,electric,greet,regular,alive,item,memory",
            [
                ["The parents _____ their children to go to bed before 10 p.m.", "request"],
                ["They are ____ customers to the supermarket, and they know where to get what they need at once.", "regular"],
                ["All the parents are happy that the school provides the best ____ for its students in the dorm.", "service"],
                ["The data (数据) is stored in the computer’s _____ .", "memory"],
                ["It was hard to believe that the boy was still ____ after the air crash", "alive"],
                ["The development of ____ society also brings about many problems.", "modern"],
                ["Nowadays I am a lot better placed and able to eat better because of the ____ cooker (锅).", "electric"],
                ["His suggestion about giving up this plan was ____ with silence.", "greeted"]
            ]
        ]],
        "lesson_5": [[
            "truth,retire,quality,outstanding,wonder,definite,available,influence,disease,ease",
            [
                ["Could you tell me the ____ about it?", "truth"],
                ["-----Can I borrow some children’s books from the library?" + "\n" + "-----Sorry.I’m afraid they are not ____ now.", "available"],
                ["The store-owner was fined（罚）＄500 for selling goods of low _____.", "quality"],
                ["Can you give me a (n) ____ answer to this question?", "definite"],
                ["Workers in that company would ____ with a good pension（养老金）", "retire"],
                ["No one ____ him as much as his father did in forming his personality（个性）.", "influenced"],
                ["He was sent to a hospital because of a serious ____.", "disease"],
                ["Albert Einstein（爱因斯坦）is one of the most ____ scientists of the 20th century", "outstanding"]
            ]
        ]],
        "lesson_6": [
            [
                "habit,importance,electric,involve,recent,tradition,celebrate,measure,cheer",
                [
                    ["The good news got ____ from the audience", "cheers"],
                    ["These factories will take every possible ____ to reduce pollution（减少污染）.", "measure"],
                    ["Waterfalls（瀑布）can be used to produce _____power.", "electric"],
                    ["Can you come to the party to ____ Jim’s graduation?", "celebrate"],
                    ["It’s a(n) ____ to sing “Jingle Bells” at Christmas.", "tradition"],
                    ["These classes help members learn how to change their eating ____.", "habits"],
                    ["In some way, he ____ several of his friends in the trouble.", "involved"],
                    ["In the end,he realized the ____ of foreign languages.", "importance"]
                ]
        ], [
                "select,include,honor,attempt,simple,design,art,determine,develop,hang",
                [
                    ["Courses are not ____ merely for students to pass exams.", "designed"],
                    ["Please ____ those details that you would like to change.", "select"],
                    ["There is a long wire（电线）____ outside the window.", "hanging"],
                    ["There are six people present at the meeting, ____ three women.", "including"],
                    ["He ____ told her that he worked for the corporation（公司）.", "simply"],
                    ["They accept what is happening without ____ to change it.", "attempting"],
                    ["He was a great ____; he composed（创作）many great songs.", "artist"],
                    ["These problems can appear in ____ and underdeveloped countries.", "developed"]
                ]
        ]],
        "lesson_7": [[]],
        "lesson_8": [[]],
        "lesson_9": [[
            "notice,standard,product,manager,fit,convenient,base,mystery,tend,hire",
            [
                ["We _____an advertising (广告) company to help sell our new product.", "hired"],
                ["We need to improve the educational ______of this country.", "standards"],
                ["Teamwork is _____on mutual(相互的)respect,trust,and understanding.", "based"],
                ["A college graduate ____to show little interest in poorly-paid jobs.", "tends"],
                ["The price of the new______is much higher than that of the old one.", "product"],
                ["People used to build houses that _____the climate of their areas.", "fitted"],
                ["They had a(n) ____guest at their party last night", "mystery"],
                ["I’m willing to meet you on any day that is _____for you", "convenient"]
            ]
        ]],
        "lesson_10": [[
            "enter,compete,position,circle,taste,command,share,bear,prove,stage",
            [
                ["He _____ the church as a young man", "entered"],
                ["The plan is still in its early ____.", "stage"],
                ["I’ve always had a(n) ____ for the 19th-century America literature.", "taste"],
                ["The captain(船长) of a ship ____ a heavy responsibility.", "bears"],
                ["Mary is sociable and has a large ____ of friends.", "circle"],
                ["Janet took ____ of the situation and got everyone out of the building.", "command"],
                ["In order to ____ her point,she showed them the latest sales figures.", "prove"],
                ["We haven’t enough books for everyone ;some of you will have to ____.", "share"]
            ]
        ]],
        "lesson_11": [[
            "damage,deny,public,inspect,actually,location,structure,claim,register,amount",
            [
                ["Bees communicate by dancing: for example, they do a kind of dance to tell other bees about the ____ of flowers.", "location"],
                ["It was said that Nancy was going to marry a rich Englishman, but she ____ it", "denied"],
                ["We need a huge ____ of money to build a new high school for the children in this area.", "amount"],
                ["Since you broke the window, you should pay for the ____", "damage"],
                ["People who fish and sail sometimes ____ to have seen strange animals in the sea.", "claim"],
                ["He looks young, but ____ he is much the elder of the two.", "actually"],
                ["The guard walked through the train ____ everyone’s ticket.", "inspecting"],
                ["The new smart ____ could be very expensive to build. However, they would be less likely to be damaged during earthquakes. ", "structures"]
            ]
        ], [
            "critical,defeat,uniform,oppose,admit,value,treat,replay,purchase,murder",
            [
                ["Among the decisions that most people make, ____ a house is perhaps the biggest one.", "purchasing"],
                ["Don’t be ____ about him; he is a beginner.", "critical"],
                ["Their basketball team had bad luck yesterday: it was their third ____ in four matches.", "defeat"],
                ["It is human nature to be ____ to change because it requires us to cross over into the unknown.", "opposed"],
                ["His works mirrored such positive ____ as cheerfulness and kindness.", "values"],
                ["Highlights of the race were ____ on the news.", "replayed"],
                ["The teacher was very popular among the students because he ____ them as his own children", "treated"],
                ["When I asked the students if they’d like to have the lesson near the lake, I got a(n) ____ answer: “Yes!”", "uniform"]
            ]
        ]],
        "lesson_12": [[
            "weight,character,blind,justify,false,disorder,rate,control,concept,model",
            [
                ["Many people take exercise to lose ____ and change their body shapes.", "weight"],
                ["The young man who had just come to work in the office was ____ as one of the few best employees in the company.", "rated"],
                ["She looks ill, as she has been experiencing a sleeping ____ for some time.", "disorder"],
                ["In my own life, I have developed some of both my mother’s and father’s ____.", "character"],
                ["Dog owners have been required to keep their animals under ____.", "control"],
                ["I understand some of the subject’s key ____, but I’m not sure about its details.", "concepts"],
                ["The results of the study have certainly ____ the money that has been spent on the project.", "justified"],
                ["What is known as “good reason” is the ability to judge rightly, separating the true from the ____.", "false"]
            ]
        ]],
        "lesson_13": [[
            "fiercely,purpose,achieve,wasteful,launch,billion,judge,headquarters,motivate,pretend", [
            ["The ____ of buying this book was to improve my English.", "purpose"],
            ["Some of my friends think it's ____ that I spend so much time reading blogs online.", "wasteful"],
            ["The new company would have ____ in Frankfurt and New York.", "headquarters"],
            ["You have first got to ____ the children and then to teach them.", "motivate"],
            ["Money can help us to ____ our goals if we use it with care and understanding.", "achieve"],
            ["She argued ____ with her husband. Then she packed up her things and went back to her mother's house to live.", "fiercely"],
            ["India's population of more than a ____ people is widely expected to overtake the population of China by the middle of the 21st century.", "billion"],
            ["If you ____ to know what you don't know, you'll only make a fool of yourself.", "pretend"],
        ]]],
        "lesson_14": [
            ["unpleasant,inform,headline,replace,project,delay,urgently,successfully,absorb,separate",
            [
                ["I juust glanced at the ____. I didn't have time to read the reports.", "headlines"],
                ["The opening of the new subway may be ____ for several months.", "delayed"],
                ["What a(n) ____ woman your colleague is, always complaining about one thing or another, never satisfied!", "unpleasant"],
                ["These e-books are not going to ____ the printed books, because many people believe that paper books just feel good in their hands.", "replace"],
                ["The boss asked his secretary to keep him well ____ of the program's progress.", "informed"],
                ["The children were ____ into groups for the game.", "separated"],
                ["Our boss is leaving on a trip and needs those papers ____.", "urgently"],
                ["The little boy was so ____ in a picture book that he did not hear the bell.", "absorbed"],
        ]], [
            "locate,convince,delight,favorite,enclose,confident,delicious,bare,previous,particularly", [
                ["I have been busy recently, ____ this week.", "particularly"],
                ["The bacon sandwich is still a national ____.", "favorite"],
                ["On the ____ night, she had promised not to say a word, but the next day, the whole town knew the secret.", "previous"],
                ["Mary is ____ that love rather than money is the key to happiness.", "convinced"],
                ["I thought the whole meal was good and the soup was particularly ____.", "delicious"],
                ["The first Mcdonald's restaurant is ____ in Downey, Southern California.", "located"],
                ["I was ____ when I knew my best friend had won the race.", "delighted"],
                ["In contrast to your belief that we will fail, I am ____ that we will succeed.", "confident"],
            ]
        ]],
        "lesson_15": [
            ["overcome,regret,satisfy,response,impatient,expression,insist,contrary,beneath,external", [
                ["She was ____ by his sweet words.", "overcome"],
                ["She was so _____ that she went to the kitchen three times to see whenether the fish had been cooked.", "impatient"],
                ["The book was ____ the newspaper. That's why he couldn't find it at first.", "beneath"],
                ["The ____ wall of the house was badly damaged by the storm", "external"],
                ["The school ____ that it is doing everything it can to cooperate.", "insists"],
                ["I'm not at all ____ with the service at the restaurant.", "satisfied"],
                ["The results of the research were completely ____ to what we had expected.", "contrary"],
                ["There was a sad ____ on her face when she said she had lost her new cellphone.", "expression"]
            ]],],
        "lesson_16": [
            ["introduce,deliver,couple,advise,obtain,curious,degree,wisdom,funeral,microphone", [
                ["Children are ____ about animals and how they live.", "curious"],
                ["Without the ____, the speaker could hardly be heard.", "microphone"],
                ["We ____ the new players to begin with something easy.", "advise"],
                ["You need a doctor's ____ to join our project.", "degree"],
                ["There was a ____ of things I wanted to discuss.", "couple"],
                ["The first thing you need to learn here is how to ____ information.", "obtain"],
                ["Only close relatives were allowed to attend the ____.", "funeral"],
                ["Do you remember being ____ to Dr.Smith during your last visit.", "introduced"]
            ]]],
        "lesson_17": [
            ["evidence,power,trust,pollute,unlikely,unusual,economic,sale,relate,widespread", [
                ["It's _____ that she’ll arrive before seven.", "unlikely"],
                ["Smoking is ____ to lung cancer and many diseases", "related"],
                ["The report says ____ of new homes are up 20% over the last six months.", "sales"],
                ["The police are gathering ____ to help them prove who killed the bank clerk.", "evidence"],
                ["Many lakes and rivers have been _____ by industrial waste.", "polluted"],
                ["The weather is ____ warm for this time of year.", "unusually"],
                ["There are reports of ____ flooding in northern France", "widespread"],
                ["You must ____ your own feelings and decide for yourself.", "trust"]
            ]], [
                "industrial,reduce,tour,contain,compare,declare,occasional,environment,expend,shift", [
                    ["How much liquid do you think this bottle ____?", "contains"],
                    ["We decided to buy the house after the seller ____ the price by ten percent.", "reduced"],
                    ["If we ____ the furniture against the walls, we ‘ll have more space to dance.", "shift"],
                    ["People are more concerned about ____ issues than before.", "environmental"],
                    ["The building ____ a national monument in 1980.", "was declared"],
                    ["He spent five years in Paris, with ____ visits to italy.", "occasional"],
                    ["There are no plans to ____ the local airport.", "expand"],
                    ["Germany is one of the world’s leading _____ nations", "industrial"]
                ]
            ]],
        "lesson_18": [[
            "overnight,remind,successful,ability,possess,mall,employ,addition,former,general", [
                ["let’s meet at the _____ and go see a movie.", "mall"],
                ["His reading _____ is very good for a child of six; he now can read short stories without any help from others.", "ability"],
                ["In ____ times, there was a shop round the corner, but it has been pulled down.", "former"],
                ["This is a big car-making company in the city and it ____ around ten thousand workers.", "employs"],
                ["I ____ her how much the fare was.", "remind"],
                ["I do not _____ a car; the one I drove to the party the other night belongs to Brown.", "possess"],
                ["She is making very good preparations; she wants the meeting to be a really ____ one.", "successful"],
                ["Don’t expect it to improve _____.", "overnight"]
            ]
        ]],
        "lesson_19": [
            ["likewise,comprehension,helpful,disturb,effective,probably,urge,manufacture,feature,identify", [
                ["He is a manager in a big company that ____ car parts.", "manufactures"],
                ["I'm sorry to ____ you, but my car has broken down and I am wondering if I could use your phone.", "disturb"],
                ["The most surprising ____ of the house was a large room as big as a swimming pool.", "feature"],
                ["He was too far away to be able to ____ faces.", "identify"],
                ["Just water these plants twice a week, and ____ the ones in the bedroom.", "likewise"],
                ["How she manages to fit so much into a working day is beyond my ____.", "comprehension"],
                ["I'll ____ start off for Hong Kong next week, but I'm not quite sure.", "probably"],
                ["Sometimes, e-mail can be the most ____ form of communication, for messages can be exchanged within a very shor time.", "effective"]
            ]],
            ["organize,garage,traffic,electronic,channel,nowhere,skillfully,relax,engineer,schedule",
                ["He broke his arm last year but he plays the piano as ____ as ever.", "skillfully"],
                ["New measures about car control have been introduced to solve the ____ problem in the city.", "traffic"],
                ["The computer contains a large number of ____ switches.", "electronic"],
                ["We had a very tight ____ on the trip.", "schedule"],
                ["In the winter break, I went ____ but stayed at home.", "nowhere"],
                ["The students ____ a party to welcome the expert from England.", "organized"],
                ["The doctor told him to ____ a month or so before going back to work.", "relax"],
                ["My father likes watching TV and his favorite is the sports ____.", "channel"]
            ]],
        "lesson_20": [
            ["prisoner,recommendation,eager,tiring,policy,joint,continually,readily,instinct,continual", [
                ["Drivers are being warned that an escaped ____ has been seen on the way to Paris.", "prisoner"],
                ["She's very ____ about sports: Among other things, she plays tennis twice a week.", "eager"],
                ["New buildings have been springing up everywhere in cities and towns since China began to carry out the opening-up ____.", "policy"],
                ["The ____ source of our strength was our mutual trust and respect.", "continually"],
                ["We did it together; it was a ____ effort.", "joint"],
                ["The best way of finding a lawyer is through personal _____.", "recommendation"],
                ["People prefer to live in an area where transport is ____ available.", "readily"],
                ["She knew by ____ that he would never come back if he went abroad.", "instinct"]
            ]
        ]],
    }
}

# 句子考核单元考察
def words_1():
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

# 句子考核随机抽考
def words_2():
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

# 单选考核, 如果单元内只有一个Section有单选的函数
def length_1(lesson):
    random_arr = []
    while True:
        lesson_len = len(single_choice["single_choice"]["lesson_{}".format(lesson)][0])

        if len(random_arr) == lesson_len:
            break
        random_num = random.randint(0, lesson_len - 1)
        if random_num in random_arr:
            continue
        else:
            arr = single_choice["single_choice"]["lesson_{}".format(lesson)][0][random_num]
            answer = input(arr[0] + "\n" + arr[1] + "\n")
            print("正确答案: {}".format(arr[2]))
            if answer.lower() == arr[2].lower():
                print("正确")
            else:
                print("请确认是否正确")
            print(" ")
            random_arr.append(random_num)

# 单选考核, 如果单元内有两个Section都是单选, 并且选择了单个Section, 则进入这个函数
def single_choice_section_select(lesson, section):
    if section == 1:
        section = 0
    elif section == 2:
        section = 1

    random_arr = []
    while True:
        lesson_arr = single_choice["single_choice"]["lesson_{}".format(lesson)][section]
        lesson_len = len(lesson_arr)

        if len(random_arr) == lesson_len:
            break
        random_num = random.randint(0, lesson_len - 1)
        if random_num in random_arr:
            continue
        else:
            arr = lesson_arr[random_num]
            answer = input(arr[0] + "\n" + arr[1] + "\n")
            print("正确答案: {}".format(arr[2]))
            if answer.lower() == arr[2].lower():
                print("正确")
            else:
                print("请确认是否正确")
            print(" ")
            random_arr.append(random_num)

# 单选考核, 如果选择了单元内两个Section合并考核就进入这个函数
def single_choice_section_3(lesson):
    random_arr = []
    while True:
        lesson_arr = single_choice["single_choice"]["lesson_{}".format(lesson)][0] + single_choice["single_choice"]["lesson_{}".format(lesson)][1]
        lesson_len = len(lesson_arr)

        if len(random_arr) == lesson_len:
            break
        random_num = random.randint(0, lesson_len - 1)
        if random_num in random_arr:
            continue
        else:
            arr = lesson_arr[random_num]
            answer = input(arr[0] + "\n" + arr[1] + "\n")
            print("正确答案: {}".format(arr[2]))
            if answer.lower() == arr[2].lower():
                print("正确")
            else:
                print("请确认是否正确")
            print(" ")
            random_arr.append(random_num)

# 单项选择功能入口函数
def single_choice_1():
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

    lesson_len = len(single_choice["single_choice"]["lesson_{}".format(lesson)])
    if lesson_len == 1:
        length_1(lesson)
    elif lesson_len == 2:
        print("---1.单元Section A考核")
        print("---2.单元Section B考核")
        print("---3.双Section合并考核")
        print("---请输入1-3进行功能选择...")
        while True:
            func_select = int(input("请输入序号进行选择: "))
            if func_select == 1:
                single_choice_section_select(lesson, func_select)
                break
            elif func_select == 2:
                single_choice_section_select(lesson, func_select)
                break
            elif func_select == 3:
                single_choice_section_3(lesson)
                break
            else:
                print("未知错误!")
    elif lesson_len == 0:
        print("此单元没有单项选择题!")

# 单元内只有一个Section是选词填空的情况
def word_select_single_length(lesson):
    random_arr = []
    lesson_arr = word_select["word_select"]["lesson_{}".format(lesson)][0]
    words = lesson_arr[0].split(",")
    print("")
    print("单词列表:")
    print(words[0:5])
    print(words[5:])
    print("")

    while True:
        lesson_len = len(lesson_arr[1])
        if len(random_arr) == lesson_len:
            break
        random_num = random.randint(0, lesson_len - 1)
        if random_num in random_arr:
            continue
        else:
            arr = lesson_arr[1][random_num]
            print(arr[0] + "\n")
            answer = input("请输入答案: ")
            print("正确答案: {}".format(arr[1]))
            if answer.lower() == arr[1].lower():
                print("正确")
            else:
                print("请确认是否正确")
            print(" ")
            random_arr.append(random_num)

# 单元内有两个Section是选词填空的情况
def word_select_both_length(lesson, section):
    random_arr = []
    lesson_arr = word_select["word_select"]["lesson_{}".format(lesson)][section]
    words = lesson_arr[0].split(",")
    print("")
    print("单词列表:")
    print(words[0:5])
    print(words[5:])
    print("")

    while True:
        lesson_len = len(lesson_arr[1])
        if len(random_arr) == lesson_len:
            break
        random_num = random.randint(0, lesson_len - 1)
        if random_num in random_arr:
            continue
        else:
            arr = lesson_arr[1][random_num]
            print(arr[0] + "\n")
            answer = input("请输入答案: ")
            print("正确答案: {}".format(arr[1]))
            if answer.lower() == arr[1].lower():
                print("正确")
            else:
                print("请确认是否正确")
            print(" ")
            random_arr.append(random_num)

# 选词填空功能入口函数
def word_select_1():
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

    lesson_len = len(word_select["word_select"]["lesson_{}".format(lesson)])
    if lesson_len == 1:
        word_select_single_length(lesson)

    elif lesson_len == 2:
        print("---1.单元Section A考核")
        print("---2.单元Section B考核")
        print("---请输入1-2进行功能选择...")
        while True:
            func_select = int(input("请输入序号进行选择: "))
            if func_select == 1:
                word_select_both_length(lesson, 0)
                break
            elif func_select == 2:
                word_select_both_length(lesson, 1)
                break
            else:
                print("未知错误!")
    elif lesson_len == 0:
        print("此单元没有选词填空题!")

if __name__ == '__main__':
    print("---请输入你想使用的功能的序号：")
    print("---1.句子考核")
    print("---2.选择题考核")
    print("---3.选词填空题考核")
    print("---请输入1-3进行功能选择...")
    print("---程序制作By: 方一力")
    print("")
    func_select = int(input("请输入序号进行选择: "))
    print("")

    if func_select == 1:
        print("---1.单元考核")
        print("---2.全部单元随机抽考")
        print("---请输入1-2进行功能选择...")
        print("")

        while True:
            func_select = int(input("请输入序号进行选择: "))

            if func_select == 1:
                words_1()
                break
            elif func_select == 2:
                words_2()
                break
            else:
                print("未知错误!")

    elif func_select == 2:
        print("---1.单元考核")
        print("---2.全部单元随机抽考")  # 没写完
        print("---请输入1-2进行功能选择...")
        print("")
        while True:
            func_select = int(input("请输入序号进行选择: "))

            if func_select == 1:
                single_choice_1()
                break
            elif func_select == 2:
                words_2()
                break
            else:
                print("未知错误!")

    elif func_select == 3:
        print("---1.单元考核")
        print("---2.全部单元随机抽考") # 没写完
        print("---请输入1-2进行功能选择...")
        print("")
        while True:
            func_select = int(input("请输入序号进行选择: "))

            if func_select == 1:
                word_select_1()
                break
            elif func_select == 2:
                words_2() # 未完成
                break
            else:
                print("未知错误!")
