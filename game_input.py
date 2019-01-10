import readchar

keys = {
    "\x1b[A": "up",
    "\x1b[B": "down",
    "\x1b[C": "right",
    "\x1b[D": "left",
    "\x1b\x1b": "exit",
}

def get_key():
    key = readchar.readkey()
    mapped_key = keys.get(key)
    return mapped_key
