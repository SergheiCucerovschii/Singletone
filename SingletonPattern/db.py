from lockError import *

_lock = False


def loadCount():
    global _lock
    if _lock == False:
        file = open("data.txt", "r")
        count = int(file.read())
        file.close()
        _lock = True
        return count
    else:
        raise LockError("Position of lock is not correct")



def saveCount(count):
    global _lock
    if _lock == True:
        file = open("data.txt", "w")
        file.write(str(count))
        file.close()
        _lock = False
    else:
        raise LockError("Position of lock is not correct")
