import sys

target = "out_backprop.txt"
if(len(sys.argv) > 1):
    target = sys.argv[1]
    
wx_flag = "W0_Idle"
L1D_flag = "L1D_total_cache"
L2_flag = "L2_total_cache"

wx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cache = [0,0,0,0]

f = open(target)
count = 0
for l in f:
    if (wx_flag in l):
        count += 1
        l = l.strip('\n')
        l = l.split('\t')
        for i in range(3, 35):
            temp = l[i].split(':')
            wx[i - 3] += int(temp[1])
    if (L1D_flag + "_accesses" in l):
        temp = l.split('=')
        cache[0] += int(temp[1].strip('\n'))
    if (L1D_flag + "_misses" in l):
        temp = l.split('=')
        cache[1] += int(temp[1].strip('\n'))
    if (L2_flag + "_accesses" in l):
        temp = l.split('=')
        cache[2] += int(temp[1].strip('\n'))
    if (L2_flag + "_misses" in l):
        temp = l.split('=')
        cache[3] += int(temp[1].strip('\n'))
               
f.close()

not_w32 = 0
for i in range(0, 31):
    not_w32 += wx[i]

print target
print ("# of Kernals: " + str(count))
#print wx
print ("# of !W32:    " + str(not_w32))
print ("# of W32:     " + str(wx[31]))
print ("# L1D access: " + str(cache[0]))
print ("# L1D miss  : " + str(cache[1]))
print ("# L2 access : " + str(cache[2]))
print ("# L2 miss   : " + str(cache[3]))
