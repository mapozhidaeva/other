import random

def file_reading(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')

terminology = file_reading('Terminology.tsv')
definitions = file_reading('Definitions.tsv')


#for i  in range(len(definitions)):
#    print (i + 1, definitions[i])

the_dictionary = dict(zip(terminology, definitions))

#for key, value in the_dictionary.items():
#    print (key.upper(), ' - ', value, '\n')

'''for i in range(3):
    dic_len = len(the_dictionary)
    a = random.randint(0, dic_len)
    b = random.randint(0, dic_len)
    while a == b:
        b = random.randint(0, dic_len)

    c = random.randint(0, dic_len)
    while a == c or b == c:
        c = random.randint(0, dic_len)'''

print ('Let\s start the test!')

#while input() != '':
    #one, two, three = the_dictionary.values[a], the_dictionary.values[b], \
#                      the_dictionary.values[c]
    #options = random.shuffle([one, two, three])

random_term = random.choice(list(the_dictionary.keys()))
print ('\n', random_term.upper() + ':\n')
# print (the_dictionary[random_term])
one = random.choice(list(the_dictionary.keys()))
while one == random_term:
    one = random.choice(list(the_dictionary.keys()))
two = random.choice(list(the_dictionary.keys()))
while two == one or two == random_term:
    two = random.choice(list(the_dictionary.keys()))
# print ('\n', the_dictionary[one], '\n\n', the_dictionary[two], '\n')

answers = [random_term, one, two]
right_answer = the_dictionary[random_term]
random.shuffle(answers)

n = 1
for i in answers:
    print ('{}) '.format(n), the_dictionary[i], '\n')
    n += 1

answer = int(input('Введите ответ: 1, 2 или 3: '))


if the_dictionary[random_term] == the_dictionary[answers[int(answer) - 1]]:
    print ('Правильно')
else:
    print ('Неверно! Правильный ответ - ', the_dictionary[random_term])
