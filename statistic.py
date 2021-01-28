import numpy as np
from matplotlib import pyplot as plt
import sys

def plot_cpu_load():
    CpuFile = "cpu.txt"
    CpuData = np.loadtxt(CpuFile, dtype = str)
    CpuLoadStr = CpuData[:, 1]
    CpuLoad=[]
    Times = []
    for i in range(np.size(CpuLoadStr)):
        temp = CpuLoadStr[i][0:-5]
        CpuLoad.append(int(temp))
        Times.append(i)
    print(CpuLoad)
    plt.scatter(Times, CpuLoad, color = 'r')
    plt.plot(Times, CpuLoad, color = 'r', linestyle = '--', label = "CPU Load")
    plt.xlabel("times")
    plt.ylabel("xx%")

def plot_available_mem():
    MemFile = "mem.txt"
    MemData = np.loadtxt(MemFile, dtype = str)
    MemTotal = MemData[:, 1]
    MemFree = MemData[:, 5]
    MemBuff = MemData[:, 7]

    SwapFile = "swap.txt"
    SwapData = np.loadtxt(SwapFile, dtype = str)
    MemSwap = SwapData[:, 7]

    if np.size(MemTotal) != np.size(MemSwap):
        print("error!")
        sys.exit()
    
    Total = []
    Free = []
    Buff = []
    Swap = []
    Avaible = []
    Percent = []

    for i in range(np.size(MemTotal)):
        temp = MemTotal[i][:-1]
        Total.append(int(temp))
        temp = MemFree[i][:-1]
        Free.append(int(temp))
        temp = MemBuff[i][:-1]
        Buff.append(int(temp))
        temp = MemSwap[i][:-1]
        Swap.append(int(temp))

    Times = []
    for i in range(np.size(Total)):
        percent = (Free[i] + Buff[i] + Swap[i]) * 100.0 / Total[i]
        Percent.append(percent)
        Times.append(i)
    print(Percent)

    plt.scatter(Times, Percent, color = 'k', marker = 'x')
    plt.plot(Times, Percent, color = 'k', ls = '-', label = "Availble RAM")
   
def main():
    plot_cpu_load()
    plot_available_mem()
    plt.legend(loc = "best")
    plt.savefig("zen_statistic.png")
    plt.show()

if __name__ == "__main__":
    main()
