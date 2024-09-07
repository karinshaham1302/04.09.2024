# start

score: int = int(input('what is the test score?'))

match score:
    case score if 0 <= score <= 41:
        print('try harder next time...')
    case score if 41 <= score <= 60:
        print('you are getting there, need some more work')
    case score if 61 <= score <= 80:
        print('pretty good')
    case score if 81 <= score <= 95:
        print('awesome!')
    case score if 96 <= score <= 100:
        print('excellent!!! you are a star')
    case score_:
        print('illegal grade')


#stop
