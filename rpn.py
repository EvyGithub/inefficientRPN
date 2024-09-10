s = []

def push(v) -> None:
    global s; s += [v]

def pop(v) -> float:
    global s; return s.pop(-1)

while 1:
    userInput = input()
    break # finish later Im too lazy D: