caminho = "/home/gntech/Documents/Familia/Nilton/dna.fasta"

f = open(caminho)
s = f.read()

print str(s.count('A')) + " " + str(s.count('C')) + " " + str(s.count('G')) + " " + str(s.count('T'))
f.close()
