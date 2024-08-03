a = input(str())
a_ = list(a)
for i in range(len(a)):
    if 'a' == a_[i]:
        _1 = a_[i].upper()
        _12 = ''.join(_1)
        print(_12, end='')
    elif 'a'!= a_[i]:
        _2= a_[i].lower()
        _3 = ''.join(_2)
        print(_3, end='')