print ("salut")

def addition(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les arguments doivent être des nombres (int ou float).")
    return a + b