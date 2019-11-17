from datetime import time

def time(t1, t2):
    t1 = datetime.strptime (t1, 6, 1, 30)
    t2 =datetime.strptime (t2, 6, 2, 10)
    t3 = (t2 - t1)
    print(t3)
