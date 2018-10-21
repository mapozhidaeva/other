import random

def file_reading(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')

terminology = file_reading('Terminology.tsv')
definitions = file_reading('Definitions.tsv')


the_dictionary = dict(zip(terminology, definitions))

print ('Let\'s start the test! (press Enter to end the game)')

answer = 1
while answer != '':
    random_term = random.choice(list(the_dictionary.keys()))
    print ('\n', the_dictionary[random_term] + ':\n')

    one = random.choice(list(the_dictionary.keys()))
    while one == random_term:
        one = random.choice(list(the_dictionary.keys()))
    two = random.choice(list(the_dictionary.keys()))
    while two == one or two == random_term:
        two = random.choice(list(the_dictionary.keys()))


    answers = [random_term, one, two]
    right_answer = random_term
    random.shuffle(answers)

    n = 1
    for i in answers:
        print ('{}) '.format(n), i, '\n')
        n += 1

    answer = int(input('Введите ответ: 1, 2 или 3: '))


    if right_answer == answers[int(answer) - 1]:
        print ('Правильно')
    else:
        print ('Неверно! Правильный ответ - ', random_term)