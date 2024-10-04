def rotateRight(lst : list) -> None:
    lst.insert(0, lst.pop())

def rotateLeft(lst: list) -> None:
    lst.append(lst.pop(0))
    