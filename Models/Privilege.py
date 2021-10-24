from enum import Enum


class Privilege(Enum):
    SUPER_ADMINISTRATOR = 1
    SYSTEM_ADMINISTRATOR = 2
    ADVISOR = 3
    CLIENT = 4
