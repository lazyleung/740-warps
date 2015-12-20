import xlsxwriter

workbook = xlsxwriter.Workbook('740.xlsx')
worksheet = workbook.add_worksheet()
metrics = ["Benchmark","Scheduler","CTAs","Instructions","Cycles","IPC","Stalls","!W32","W32","% Scheduled < 32","L1D Accesses", "L1D Misses", "L1D Miss Rate", "L1D Access / Core Cycle", "L2 Accesses", "L2 Misses", "L2 Miss Rate", "L2 Miss / L1D Access", "Memory Access per Load Store", "Average Mem Latency", "Total Stall Shd Mem"]

benchmarks = ["b+tree","backprop","bfs","cfd","gaussian0","gaussian1","heartwall","hotspot","kmeans","leukocyte","lud","myocyte","nw","particlefilter_float","pathfinder","srad","streamcluster"]

configs = ["lrr1","lrr2","2L","GTO","CAWA","PRO","DAWS"]

ix_flag = ""
wx_flag = "W0_Idle"
L1D_flag = "L1D_total_cache"
L2_flag = "L2_total_cache"

# Setup headers
row = 0
col = 0
for m in metrics:
    worksheet.write(row, col, m)
    col += 1
row = 1
col = 0

# Parse file
for b in benchmarks:
    for c in configs:
        ctas = 0
        insts = 0
        cycles = 0
        ipc = 0.0
        l1d_a = 0
        l1d_m = 0
        l1d_mr = 0.0
        l2_a = 0
        l2_m = 0
        l2_mr = 0.0
        mem_inst = 0;
        stalls = 0;
        average_count = 0;
        total_average_latency = 0;
        stall_mem = 0;

        wx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ix = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        target = r"S:\Lazyleung\Dropbox\School\5_Master\18740\Results\run_" + c + "\out_" + b +".txt"
        #target = r"C:\Users\Jonathan\Dropbox\School\5_Master\18740\Results\run_" + c + "\out_" + b +".txt"
        f = open(target)

        for l in f:
            if (wx_flag in l):
                l = l.strip('\n')
                l = l.split()
                temp = l[0].split(':')
                stalls += int(temp[1])
                for i in range(3, 35):
                    temp = l[i].split(':')
                    wx[i - 3] += int(temp[1])
            if (L1D_flag + "_accesses" in l):
                temp = l.split('=')
                l1d_a += int(temp[1].strip('\n'))
            if (L1D_flag + "_misses" in l):
                temp = l.split('=')
                l1d_m += int(temp[1].strip('\n'))
            if (L2_flag + "_accesses" in l):
                temp = l.split('=')
                l2_a += int(temp[1].strip('\n'))
            if (L2_flag + "_misses" in l):
                temp = l.split('=')
                l2_m += int(temp[1].strip('\n'))
            if ("gpu_tot_issued_cta" in l):
                temp = l.split('=')
                ctas = int(temp[1].strip('\n'))
            if ("gpu_tot_sim_insn" in l):
                temp = l.split('=')
                insts = int(temp[1].strip('\n'))
            if ("gpu_tot_sim_cycle" in l):
                temp = l.split('=')
                cycles = int(temp[1].strip('\n'))
            if ("gpu_tot_ipc" in l):
                temp = l.split('=')
                ipc = float(temp[1].strip('\n'))
            if ("load/store instructions" in l):
                temp = l.split()
                mem_inst = int(temp[2])
            if ("Warp Occupancy Distribution" in l):
                l = l.strip('\n')
                l = l.split()
                j = 0
                for i in range(0, 64):
                    if (i % 2 != 0):
                        ix[j] += int(l[i])
                        j += 1
            if ("averagemflatency" in l):
                average_count += 1;
                temp = l.split("=")
                total_average_latency += int(temp[1].strip('\n'))
            if ("gpgpu_n_stall_shd_mem" in l):
                temp = l.split("=")
                stall_mem += int(temp[1].strip('\n'))
                       
        f.close()

        not_w32 = 0
        for i in range(0, 32):
            not_w32 += wx[i]

        tot_ix = 0
        for i in range(0, 32):
            tot_ix += ix[i] * i

        worksheet.write(row, 0, b)
        worksheet.write(row, 1, c)
        worksheet.write(row, 2, ctas)
        worksheet.write(row, 3, insts)
        worksheet.write(row, 4, cycles)
        worksheet.write(row, 5, ipc)
        worksheet.write(row, 6, stalls)
        worksheet.write(row, 7, not_w32)
        worksheet.write(row, 8, wx[31])
        if (not_w32 + wx[31] != 0):
            worksheet.write(row, 9, not_w32/float(not_w32 + wx[31]))
        worksheet.write(row, 10, l1d_a)
        worksheet.write(row, 11, l1d_m)
        worksheet.write(row, 12, l1d_mr)
        if (cycles != 0):
            worksheet.write(row, 13, float(l1d_a)/cycles/15.0)
        worksheet.write(row, 14, l2_a)
        worksheet.write(row, 15, l2_m)
        worksheet.write(row, 16, l2_mr)
        if (l1d_a != 0):
            worksheet.write(row, 17, float(l2_m)/l1d_a)
        if (mem_inst != 0):
            worksheet.write(row, 18, float(tot_ix)/mem_inst/15)
        if (average_count != 0):
            worksheet.write(row, 19, float(total_average_latency)/average_count)
        worksheet.write(row, 20, stall_mem)

        row += 1

workbook.close()
