from funtion import questions

i=0
money=0
for elems in questions:
    print(questions[i][0])
    print(questions[i][1])
    print(questions[i][2])
    print(questions[i][3])
    print(questions[i][4])
    c=int(input('enter your answer between 0 to 4'))
    if c==questions[i][-1]:
        print(f'you won {money+1000} rupees/nnow this is your next question')
        i+=1
        money+=1000
    else:
        if money==3000:
            print('sorry you gave wrong answer youa r etaking only 3000 rupees')
        else:
            print('sorry you lost and won 0 rupees')
        break