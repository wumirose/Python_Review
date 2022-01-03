# def (n):
import random

n = int(input('What limit of random number would you like to guess eg 10 to infinity?: '))
r_num = random.randint(0, n)
trial = int(input('How many trial would you like to have?: '))
num = ''
guess_no = 0
is_guess_limit = False

print('Attempt', guess_no + 1, '/', trial, ':', 'Guess a number between 0 and ', n, '**', r_num, '**', sep = '')
while num != r_num and not(is_guess_limit):
    num = int(input())
    guess_no += 1 
    if guess_no < trial:
        if num < r_num:
            print('Attempt {}/{}: Your guess is too small, guess a larger number:'.format(guess_no + 1, trial))
        if num > r_num:
            print('Attempt {}/{}: Your guess is too large, guess a smaller number:'.format(guess_no + 1, trial)) 
    else:
        is_guess_limit = True
if is_guess_limit and num != r_num :
    print('You have exhaused {}/{} Guesses. You lose!!!'.format(guess_no, trial))
else:
    print('Your Won the guess {}={} in {}/{} trial'.format(r_num, num, guess_no, trial))