from CDMS import cdms
from Controllers.Encryption import Encryption
from Models.Priviledges import Priviledge as pv


def split_list(alist):
    length = len(alist)
    wanted_parts = len(alist) // 3
    return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts] for i in range(wanted_parts)]


if __name__ == '__main__':
    system = cdms()
    while not system.Stop:
        system.execute()
