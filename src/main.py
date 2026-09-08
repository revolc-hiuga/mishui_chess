import const

def main():
    print("欢迎来到祢水象棋。")
    print_version()

    mode = select_mode()

    com_depth = 0
    if mode != const.TWO_PLAYERS:
        com_depth = select_com_depth()

    print("mode =", mode, ", com_depth =", com_depth)


def print_version():
    print("祢水象棋 V1.0 build: 3")
    print("作者：Xack & 日向")
    print()

def select_mode() -> int:
    print("【模式选择】")
    print("1. 双人模式")
    print("2. 单人模式，人类先行")
    print("3. 单人模式，电脑先行")

    s = input("请选择你想要的模式（1~3, 默认为1）：").strip()
    if not s.isdigit():
        if s == "":
            print("没有输入。默认选择双人模式。\n")
        else:
            print("格式错误。默认选择双人模式。\n")
        return const.TWO_PLAYERS

    mode = int(s)
    if not (mode == const.TWO_PLAYERS 
         or mode == const.ONE_PLAYER_HUMAN_FIRST 
         or mode == const.ONE_PLAYER_COMPUTER_FIRST):
        print("格式错误。默认选择双人模式。")
        mode = const.TWO_PLAYERS

    print()
    return mode
        

def select_com_depth() -> int:
    depth_table = [3, 5, 7]

    print("【难度选择】")
    print("1. 简易 (depth=3)")
    print("2. 中等 (depth=5)")
    print("3. 困难 (depth=7)")

    print("难度越大，代表电脑走棋越智能，也代表电脑思考的时间越长。")
    s = input("请输入你想要的难度（1~3, 默认为1)：").strip()
    if not s.isdigit():
        if s == "":
            print("没有输入。默认选择简易模式。\n")
        else:
            print("格式错误。默认选择简易模式。\n")
        return depth_table[0]

    index = int(s)
    if index < 1 or index > 3:
        print("格式错误。默认选择简易模式。\n")
        return depth_table[0]
    else:
        print()
        return depth_table[index-1]

if __name__ == "__main__":
    main()