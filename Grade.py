name1 = "Jacky"
t1 = 23
t2 = 64
t3 = 23
t4 = 12
t5 = 42


def grade(name, test1, test2, test3, test4, test5):
    x = (test1 + test2 + test3 + test4 + test5) / 5
    if x >= 80:
        print(name + " got a Grade A")
    elif 60 <= x < 80:
        print(name + " got a Grade B")
    elif 50 <= x < 60:
        print(name + " got a Grade C")
    elif 50 > x:
        print(name + " you failed badly")


grade(name1, t1, t2, t3, t4, t5)