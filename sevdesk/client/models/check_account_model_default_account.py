from enum import IntEnum


class CheckAccountModelDefaultAccount(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

    def __str__(self) -> str:
        return str(self.value)
