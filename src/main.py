import const

def main():
    print("欢迎来到祢水象棋。")
    print_version()

    mode = select_mode()
    print()

    print("mode = ", mode)

def print_version():
    print("祢水象棋 V1.0 build: 2")
    print("作者：Xack & 日向")
    print()

# 难办的问题。如果一定要在这个函数下满足末尾输出换行的话，
# 就要多次插入换行语句，不美观。
def select_mode() -> int:
    print("1. 双人模式")
    print("2. 单人模式，人类先行")
    print("3. 单人模式，电脑先行")

    s = input("请选择你想要的模式（1~3, 默认为1）：").strip()
    if not s.isdigit():
        if s == "":
            print("没有输入。默认选择为双人模式。")
        else:
            print("格式错误。默认选择为双人模式。")
        return const.TWO_PLAYERS

    mode = int(s)
    if mode == 1:
        return const.TWO_PLAYERS
    elif mode == 2:
        return const.ONE_PLAYER_HUMAN_FIRST
    elif mode == 3:
        return const.ONE_PLAYER_COMPUTER_FIRST
    else:
        print("格式错误。默认选择为双人模式。")
        return const.TWO_PLAYERS
        

if __name__ == "__main__":
    main()