a=input()
N=len(a)
english=0#英文字符个数
numbers=0#数字个数
space=0#空格个数
extra=0#其他字符个数
a=a.lower()
for i in range(0,N):
    if a[i]>="a"and a[i]<="z":#此行也可以改成：if a[i].islower():
        english+=1
    elif a[i].isnumeric():
        numbers+=1
    elif a[i].isspace():
        space+=1
    else:
        extra+=1
print(f"英文字符：{english}")
print(f"数字：{numbers}")
print(f"空格：{space}")
print(f"其他字符：{extra}")
