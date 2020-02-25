# fruits = {"apple", "banana", "cherry", "orange", "kiwi"}
# if "apple" in fruits:
#     print("Yes")
# else:
#     print("No")
#
# fruits.add("")
# print(fruits)
#


fseq = open("/home/gntech/Documents/Familia/Nilton/sequence.fasta", "r")
first_line = fseq.readline(1)
for x in fseq:
    print(x)

fseq.close()

