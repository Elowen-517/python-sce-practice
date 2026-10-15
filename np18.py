s = input().split()#读取一行，按空格切开，得到字符串列表。split切出来全是字符串，必须逐个转int.
res = [int(i) for i in s]#
print(res)
