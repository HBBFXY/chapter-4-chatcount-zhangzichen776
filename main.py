# 从键盘输入一行字符
input_str = input("请输入一行字符: ")

# 初始化计数器
letter_count = 0  # 英文字符计数器
digit_count = 0   # 数字计数器
space_count = 0   # 空格计数器
other_count = 0   # 其他字符计数器

# 遍历输入的每个字符
for char in input_str:
    # 判断字符类型并增加对应的计数器
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        other_count += 1

# 按照指定格式输出结果
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
