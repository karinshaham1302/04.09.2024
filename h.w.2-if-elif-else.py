# start

score: int = int(input('what is the test score?'))

if 0 <= score <= 40:
    print('try harder next time...')
elif 41 <= score <= 60:
    print('you are getting there, need some more work')
elif 61 <= score <= 80:
    print('pretty good')
elif 81 <= score <= 95:
    print('awesome!')
elif 96 <= score <= 100:
    print('excellent!!! you are a star!')
else:
    print('illegal grade')

# stop

