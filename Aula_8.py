### Write a program which will find all such number which are divisible
### by 7 are not a multiple of 5, between 2000and 3250 (both included).
###The numbers obtained should be saved in a comma-separated file on a sigle line.

# Um numero sera divisivel por 7

lista=[]

for x in range(2000, 3201):
    if x%7==0 and x%5!=0:
        lista.append(str(x))

#print(lista)

with open("/home/gntech/Documents/Familia/Nilton/aula8.txt", "w") as f:
    f.write(",".join(lista))

