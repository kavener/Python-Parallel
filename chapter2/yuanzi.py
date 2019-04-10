import dis
def add(total):
    total += 1
def desc(total):
    total -= 1
total = 0
print(dis.dis(add))
print(dis.dis(desc))
# 运行结果：
#   3           0 LOAD_FAST                0 (total)
#               3 LOAD_CONST               1 (1)
#               6 INPLACE_ADD
#               7 STORE_FAST               0 (total)
#              10 LOAD_CONST               0 (None)
#              13 RETURN_VALUE
# None
#   5           0 LOAD_FAST                0 (total)
#               3 LOAD_CONST               1 (1)
#               6 INPLACE_SUBTRACT
#               7 STORE_FAST               0 (total)
#              10 LOAD_CONST               0 (None)
#              13 RETURN_VALUE
# None
