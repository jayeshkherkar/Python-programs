top = 0
temp1 = 0
temp2 = 0
a_tat = 0.0   # Average Turn around time
a_wt = 0.0    # Average Waiting time
at = []       # Arrival time
bt = []       # Burst time
n = int(input("Enter the process = "))
for i in range(n):
    pro = int(input("p%d Arrival Time : "%(i+1)))
    at.append(pro)
    pro = int(input("p%d Burst Time : "%(i+1)))
    bt.append(pro)

ct = []    # Completion time
tat = []   # Turn around time
wt = []    # waiting time
# Calculation of completion time

for i in range(n):
    if i==0:
        top = top+bt[i]
        ct.append(top)
    elif i>0:
        if top<at[i]:
            top = at[i]+bt[i]
            ct.append(top)
        else:
            top = top+bt[i]
            ct.append(top)

print("completion is calculated = ..........")
print(ct)

# Calculation for Turn around and waiting time

for i in range(n):
    var = ct[i]-at[i]
    tat.append(var)
    var = tat[i]-bt[i]
    wt.append(var)

print("Turn around time is calculated .......")
print("Waiting time is calculated .......")

print("Pid", "AT","BT","CT","TAT","WT")
for i in range(n):
    print(str((i+1)) + "\t" + str((at[i])) + "\t"+ str((bt[i])) + "\t"+ str((ct[i])) + "\t"+ str((tat[i])) + "\t"+ str((wt[i])) + "\t")
    temp1 = tat[i]+ temp1
    temp2 = wt[i]+temp2
a_tat = temp1/n
a_wt = temp2/n
print("Average Turn around time is calculated = ",a_tat)
print("Average waiting time is calculated = ",a_wt)

