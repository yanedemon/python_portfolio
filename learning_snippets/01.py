import random
secretNumber = random.randint(1, 20)
print('Загадано число от 1 до 10. Угадайте.')

for guessesTaken in range (1, 7):
    print('Ваш вариант: ')
    guess = int(input())

    if guess < secretNumber:
        print('Предложенное число меньше задуманного.')
    elif guess > secretNumber:
        print('Предложенное число больше задуманного.')
    else:
        break

if guess == secretNumber:
    print('Верно! Количество попыток: ' + str(guessesTaken))
else:
    print('Нет. Было задумано число ' + str(secretNumber))
