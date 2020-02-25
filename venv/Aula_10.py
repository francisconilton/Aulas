# def printyellow():
#     print("verde")

def media(n1, n2):
    md = (n1+n2)/2
    return md

md = media(2,6)
print(md)
#
# def formatacpf(n):
#     p1 = n[0:3]
#     p2 = n[3:6]
#     p3 = n[6:9]
#     p4 = n[9:]
#     return f"{p1}.{p2}.{p3}-{p4}"
#
# print(formatacpf("33789877824"))

def formatacpf(n):
    p1 = n[0:3]
    p2 = n[3:6]
    p3 = n[6:9]
    p4 = n[9:]
    return f"{p1}.{p2}.{p3}-{p4}"

print(formatacpf("12345678987"))

