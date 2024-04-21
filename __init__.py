secret_word = input('Введите секретное слово: ').lower()
starred_word = ''.join(['*' for _ in secret_word])
remain_lives = 5
already_added = []


def check_word():
    global starred_word
    global remain_lives
    global already_added
    letter = input('Введите букву из слова: ').lower()
    if letter in already_added:
            print('Такая буква уже была!')
            check_word()
    elif letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                list_starred_word = list(starred_word)
                list_starred_word[i] = str(secret_word[i])
                starred_word = "".join(list_starred_word)
        print(starred_word)
    else:
        remain_lives -= 1
        if remain_lives == 4:
            draw_remain_four()
        if remain_lives == 3:
            draw_remain_three()
        if remain_lives == 2:
            draw_remain_two()
        if remain_lives == 1:
            draw_remain_one()
    already_added.append(letter)

def draw_remain_four():
    global remain_lives
    global starred_word
    print('''
        |
        |
        |
        |
    ''')
    print('Ошибка!')
    print(f'Осталось попыток: {remain_lives}')
    print(starred_word)

def draw_remain_three():
    global remain_lives
    global starred_word
    print('''
    |
    |
    |
    |  
    |
    |  
    |
    |
    ''')
    print('Ошибка!')
    print(f'Осталось попыток: {remain_lives}')
    print(starred_word)

def draw_remain_three():
    global remain_lives
    global starred_word
    print('''
    |-----
    | 
    | 
    |   
    | 
    |   
    |
    |
    ''')
    print('Ошибка!')
    print(f'Осталось попыток: {remain_lives}')
    print(starred_word)

def draw_remain_two():
    global remain_lives
    global starred_word
    print('''
    |-----
    |    |
    |    *
    |
    | 
    |   
    |
    |
    ''')
    print('Ошибка!')
    print(f'Осталось попыток: {remain_lives}')
    print(starred_word)

def draw_remain_one():
    global remain_lives
    global starred_word
    print('''
    |-----
    |    |
    |    *
    |   /|\\
    | 
    |   
    |
    |
    ''')
    print('Ошибка!')
    print(f'Осталось попыток: {remain_lives}')
    print(starred_word)

def draw_lose():
    print('''
    |-----
    |    |
    |    *
    |   /|\\
    |    |
    |   / \\
    |
    |
    ''')
    print('Вы проиграли!')
    print(f'Загаданное слово: {secret_word}')



while True:
    check_word()
    if secret_word == starred_word:
        print('Поздравляем! Вы отгадали слово')
        break
    if remain_lives == 0:
        draw_lose()
        break
