x = """anirudh:11
zabd:98
samarth:94
nihar:14"""


y = "\n".join(stu for stu in sorted(x.split("\n"), key=lambda x: x[0]))
print(y)
