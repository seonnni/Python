# 10769
m = input()
if m.count(":-)") == 0 and m.count(":-(") == 0:
    print("none")
elif m.count(":-)") == m.count(":-("):
    print("unsure")
elif m.count(":-)") > m.count(":-("):
    print("happy")
else:
    print("sad")