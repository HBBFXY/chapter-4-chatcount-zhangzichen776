# 从键盘输入一行字符
s = input()

# 初始化各类字符的计数器
letter_count = 0  # 英文字符（字母）计数器
digit_count = 0   # 数字计数器
space_count = 0   # 空格计数器
other_count = 0   # 其他字符计数器

# 遍历字符串中的每个字符
for char in s:
    if char.isalpha():  # 判断是否为英文字母（大小写均可）
        letter_count += 1
    elif char.isdigit():  # 判断是否为数字
        digit_count += 1
    elif char.isspace():  # 判断是否为空格
        space_count += 1
    else:  # 以上都不是，则为其他字符
        other_count += 1

# 按照要求格式输出结果
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
