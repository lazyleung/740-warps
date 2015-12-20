target = "out_bfs.txt"
flag = "W0_Idle"

total = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

f = open(target)
count = 0
for l in f:
    if (flag in l):
        count += 1
        l = l.strip('\n')
        l = l.split('\t')
        for i in range(3, 35):
            temp = l[i].split(':')
            total[i - 3] += int(temp[1])
        
f.close()

not_w32 = 0
for i in range(0, 31):
    not_w32 += total[i]

print target
print ("# of Kernals: " + str(count))
#print total
print ("# of !W32:    " + str(not_w32))
print ("# of W32:     " + str(total[31]))
