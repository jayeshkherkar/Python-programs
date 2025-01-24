# process scheduling simulation#
class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority


def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0                            # turn around time - burst time
    for i in range(0, n-1):
        waiting_time[i] = processes[i].burst_time + waiting_time[i]

    for i in range(n):
        turnaround_time[i] = processes[i].burst_time-waiting_time[i]

    return waiting_time, turnaround_time


def round_robin(processes, time_quantum):
    n = len(processes)
    remaining_time = [process.burst_time for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_burst_time = sum(process.burst_time for process in processes)
    current_time = 0

    while total_burst_time > 0:
        for i in range(n):
            if remaining_time[i] > 0:
                if remaining_time[i] <= time_quantum:
                    current_time += remaining_time[i]
                    turnaround_time[i] = current_time - processes[i].arrival_time
                    waiting_time[i] = turnaround_time[i] - processes[i].burst_time
                    remaining_time[i] = 0
                    total_burst_time -= processes[i].burst_time
                else:
                    current_time += time_quantum
                    remaining_time[i] -= time_quantum
                    total_burst_time -= time_quantum

    return waiting_time, turnaround_time


def priority_scheduling(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    sorted_processes = sorted(processes, key=lambda x: x.priority)

    waiting_time[0] = 0
    for i in range(1, n):
        waiting_time[i] = sorted_processes[i - 1].burst_time + waiting_time[i - 1]

    for i in range(n):
        turnaround_time[i] = sorted_processes[i].burst_time + waiting_time[i]

    return waiting_time, turnaround_time


def display_results(processes, waiting_time, turnaround_time):
    n = len(processes)
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print("Process Arrival Time Burst Time Waiting Time Turnaround Time")
    for i in range(n):
        print(
            f"{processes[i].pid}\t\t{processes[i].arrival_time}\t\t{processes[i].burst_time}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}"
        )

    print("\nAverage Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)


def main():
    # Example processes (you can modify or take input from the user)
    processes = [
        Process(1, 0, 6, 2),
        Process(2, 2, 4, 1),
        Process(3, 4, 2, 3),
        Process(4, 6, 5, 4),
    ]

    # FCFS Scheduling
    print("FCFS Scheduling:")
    fcfs_waiting_time, fcfs_turnaround_time = fcfs(processes)
    display_results(processes, fcfs_waiting_time, fcfs_turnaround_time)

    print("\n---")

    # Round Robin Scheduling
    print("Round Robin Scheduling:")
    time_quantum = 2
    rr_waiting_time, rr_turnaround_time = round_robin(processes, time_quantum)
    display_results(processes, rr_waiting_time, rr_turnaround_time)

    print("\n---")

    # Priority Scheduling
    print("Priority Scheduling:")
    priority_waiting_time, priority_turnaround_time = priority_scheduling(processes)
    display_results(processes, priority_waiting_time, priority_turnaround_time)


if __name__ == "__main__":
    main()
