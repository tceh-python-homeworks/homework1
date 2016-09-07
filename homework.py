# -*- coding: utf-8 -*-

import sys  # importing the standart library `sys`.

__author__ = 'denis_chinin'

# which function to use?
if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

# main homework code
correct_answers = 0

# all questions
questions = [
    {
        "text": 'Which programming language will we learn?',
        "answer": "python"
    },
    {
        "text": 'Everything in python is an ...',
        "answer": "object"
    },
    {
        "text": 'Please enter "nothing" type in python',
        "answer": "None"
    },
    {
        "text": 'What is the name of our teacher?',
        "answer": "Nikita"
    },
    {
        "text": 'How much is the fish?',
        "answer": "big"
    }
]

# get user name
user_name = input_function('What\'s your name bro?\n')
print('Hi, {}. I have some questions for you.'.format(user_name))

for question in questions:
    answer = input_function('%s\n' % question['text'])

    if (answer == question['answer']):
        correct_answers += 1
        print('You\'re right!. Correct answers count: %d\n' % correct_answers)
    else:
        print('Ouch... This is a wrong answer. Right answer is %s\n' % question['answer'])


print('Total correct answers: %d' % correct_answers);

