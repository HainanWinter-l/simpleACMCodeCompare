from cyaron import *
from os import system

# 选择程序 按 ctrl + / 来切换注释。可以混用，比如 Python 测试，C++ 标程
TEST = "./build/test.exe"               # C/C++
STANDARD = "./build/standard.exe"       # C/C++
# TEST = "python ./src/test.py"  # Python
# STANDARD = "python ./src/standard.py"  # Python

# 启用 C++ 自动编译（需要声明到 g++ 到环境变量，且支持 C++17）
ENABLE_AUTO_COMPILE = True # 其实也可以改编译参数，在下面就有

# 鼠标挪到 # 前面可以折叠 region (VScode/PyCharm)
# region 这些代码都不要改了

# C++ 编译
if ENABLE_AUTO_COMPILE and "exe" in TEST:
    system("g++ -o ./build/test.exe -std=c++17 ./src/test.cpp")
if ENABLE_AUTO_COMPILE and "exe" in STANDARD:
    system("g++ -o ./build/standard.exe -std=c++17 ./src/standard.cpp")


# 一次评测对拍
def isAccepct(input_data: IO):
    try:
        Compare.program(TEST, input=input_data, std_program=STANDARD)
    except:
        return False
    return True


# 显示输入数据
def exhabitInput(input_data: IO):
    with open("error_input", "w") as file:
        file.writelines(input_data.input_file.readlines())


# endregion

# 死循环评测就好了
while True:
    # 造数据
    data_file = IO() # 不需要改
    a, b = randint(-(10**9), 10**9), randint(-(10**9), 10**9)
    data_file.input_writeln(a, b)





    # 对拍
    if isAccepct(data_file):  # 通过就证明没有找到
        continue
    # 没有通过，展示数据并退出程序（数据在 error_input）文件中
    exhabitInput(data_file)
    break

# 恭喜你找到一个错误数据
print("Congratulations! You found a error example!")
