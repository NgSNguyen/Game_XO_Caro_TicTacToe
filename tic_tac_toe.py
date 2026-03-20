b = {
    "11": " ¹¹ ",
    "12": " ¹² ",
    "13": " ¹³ ",
    "21": " ²¹ ",
    "22": " ²² ",
    "23": " ²³ ",
    "31": " ³¹ ",
    "32": " ³² ",
    "33": " ³³ ",
}


def check_winner(character):
    if (
        b["11"] == b["22"] == b["33"]
        or b["13"] == b["22"] == b["31"]
        or b["11"] == b["21"] == b["31"]
        or b["21"] == b["22"] == b["23"]
        or b["12"] == b["22"] == b["32"]
        or b["13"] == b["23"] == b["33"]
        or b["11"] == b["12"] == b["13"]
        or b["31"] == b["32"] == b["33"]
    ):
        print(f"{character.strip()} win!😝")
        print_board()
        exit()


def print_board():
    print(f"""|{b["11"]}|{b["12"]}|{b["13"]}|
|{b["21"]}|{b["22"]}|{b["23"]}|
|{b["31"]}|{b["32"]}|{b["33"]}|""")


print("Input m×n or mn to chose")
for i in range(1, 3):
    while True:
        print_board()
        index = input("X's turn, m×n: ").replace("×", "").strip()
        if index not in b or b[index] in ["  X ", "  O "]:
            print("Invalid!")
            continue
        b[index] = "  X "
        break
    while True:
        print_board()
        index = input("O's turn, m×n: ").replace("×", "").strip()
        if index not in b or b[index] in ["  X ", "  O "]:
            print("Invalid!")
            continue
        b[index] = "  O "
        break
for i in range(3, 6):
    while True:
        print_board()
        index = input("X's turn, m×n: ").replace("×", "").strip()
        if index not in b or b[index] in ["  X ", "  O "]:
            print("Invalid!")
            continue
        b[index] = "  X "
        check_winner(b[index])
        break
    while i < 5:
        print_board()
        index = input("O's turn, m×n: ").replace("×", "").strip()
        if index not in b or b[index] in ["  X ", "  O "]:
            print("Invalid!")
            continue
        b[index] = "  O "
        check_winner(b[index])
        break
print("Draw!!😂")
print_board()
