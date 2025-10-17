# 初始化计数器
letter_count = 0    # 英文字符计数
digit_count = 0     # 数字计数
space_count = 0     # 空格计数
other_count = 0     # 其他字符计数

# 获取输入
input_str = input()

# 遍历每个字符进行分类统计
for char in input_str:
    # 判断是否为英文字符（a-z, A-Z）
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        letter_count += 1
    # 判断是否为数字（0-9）
    elif '0' <= char <= '9':
        digit_count += 1
    # 判断是否为空格
    elif char.isspace():
        space_count += 1
    # 其余均为其他字符（包括中文、标点、特殊符号等）
    else:
        other_count += 1

# 按要求格式输出结果
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
