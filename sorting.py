import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from random import shuffle
import time


files_list = ['5.txt', '6.txt', '7.txt', 'The_Kite_Runner.txt', 'identity.txt', 'legacy.txt', 'ultimatum.txt', 'supremacy.txt', 'betrayal.txt', 'empire1.txt', 'empire2.txt', 'empire3.txt', 'shakespeare.txt', 'bishop.txt', 'bible.txt', 'IR.txt', 'lordofring1.txt', 'lordofring2.txt', 'lordofring3.txt']
words = []

for filename in files_list:
	print filename
	with open(filename) as f:
	    for line in f:
	        inner_list = [w.strip() for w in line.split(' ')]
	        words.extend(inner_list)
	print len(words)

shuffle(words)
words = filter(None, words)
nwords = []
for i in words:
	for k in range(0,21):
		nwords.append(i)
shuffle(nwords)
sizes = [1,10,100,1000,10000,100000,500000,1000000,2000000,5000000,7000000,10000000,20000000,40000000,60000000,80000000,100000000]
print "final", len(nwords)
tlist = []

for s in sizes:
	newl = nwords[:s]
	shuffle(newl)
	beg_ts = time.time()
	newl.sort()
	end_ts = time.time()
	tot = end_ts - beg_ts
	print s, tot
	tlist.append(tot)

plt.plot(sizes, tlist, "b*-")
plt.ylabel("Sorting Time")
plt.xlabel("Word Count")
plt.savefig("graph.png")