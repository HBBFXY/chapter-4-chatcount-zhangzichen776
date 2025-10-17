letter_count = 0
digit_count = 0
space_count = 0
other_count = 0

input_str = input()

for char in input_str:
    if char.isalpha() and not '\u4e00' <= char <= '\u9fff':  # 英文字符（排除中文）
        letter_count += 1
    elif char.isdigit():  # 数字
        digit_count += 1
    elif char.isspace():  # 空格
        space_count += 1
    else:  # 其他字符（包含中文、标点、特殊符号等）
        other_count += 1

print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
