
def chatbot(chat):

    database = ['name', 'old','age', 'movie', 'show', 'destination','country', 'color', 'food', 'superpower', 'pet', 'cook', 'book', 'hobby', 'person', 'season','yes','no']
    checker_user = ['i', 'my', 'mine']
    checker_bot = ['your', 'you', 'you\'re']
    option = -1
    dbcount = -1
    for word in chat.split():
        if word in database:
            dbcount = database.index(word)

    for word in chat.split():
        if word in checker_bot:
            option = 1
    for word in chat.split():
        if word in checker_user:
            option = 0

    answer_bot = [
        'My name is Timmy',
        'I was born on 01/09/24 you can find out my age :)',
        'I was born on 01/09/24 you can find out my age :)',
        'I like to watch Deadpool x Wolverine',
        'My favorite tv show is Young Sheldon',
        'Japan',
        'India',
        'My favorite color is green',
        'My favorite food is Cake',
        'I would love to see your future',
        'I love Dogs, Cats and Hamsters',
        'I dont cook, I only know to eat',
        'I read all kinds of books, personally i prefer what you like to read',
        'I love to chat with you',
        'I am a night owl and prefer to morning persons',
        'my favorite season is Summer, wow hey there Ice Cream',
        'Thats great',
        'That also great your opinion matters',
    ]

    answer_user = [
        'I dont know but i know its good',
        'I bet you are older than me',
        'I bet you are older than me',
        'You like Avengers?',
        'You like Young Sheldon',
        'I think you\'ll love to see japan',
        'You love India right?',
        'I think its black, am I right?',
        'My favorite food is Cake, yours should be Cake also. Cuz we have similar intrests',
        'You have life',
        'I know you love Dogs and Cats',
        'Make me a dish. I\'ll tell you if you do or not',
        'I guess you like fiction',
        'Chatting with me. I am should be correct, shouldn\'t I?',
        'Hey There night owl',
        'Your favorite season is Summer, cuz you eat too much Ice Cream',
        'Thats great',
        'That also great haha',
    ]

    bot = {}
    for i in range(len(database)):
        bot[i]=answer_bot[i]

    user = {}
    for i in range(len(database)):
        user[i] = answer_user[i]

    if (dbcount == -1):
        print('I am sorry but, I am just a child please dont me something so hard (╥_╥)')
        print('ask me on name, old ,age ,movie ,show ,destination ,country ,color ,food ,superpower ,pet ,cook ,book ,hobby ,person ,season')
        print('And I\'ll tell you')
    if(option == -1 and dbcount != -1):
        choice = input('about whom, me or you')
        if choice == 'me':
            option = 1
        elif choice == 'you':
            option = 0
        else:
            print('Incorect choice, try again')
            return 0
    if(option == 1):
        print(bot.get(dbcount, 'okay'))
    if (option == 0):
        print(user.get(dbcount, 'okay'))

print('Enter end to exit')
print('Enter "my" to ask about you and "your" to ask about me')
print('ask me on name, old ,age ,movie ,show ,destination ,country ,color ,food ,superpower ,pet ,cook ,book ,hobby ,person ,season')
while(1):
    user = input('ask: ')
    chat = user.lower()
    if(chat == 'end'):
        break
    chatbot(chat)