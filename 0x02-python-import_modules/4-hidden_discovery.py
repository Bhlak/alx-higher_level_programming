#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    arr = dir(hidden_4)
    for name in arr:
        if name[0] == "_" and name[1] == "_":
            continue
        print(f"{name}")