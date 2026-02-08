log_file = "/var/log/system_monitor.log"

cpu_values = []
memory_values = []
disk_values = []

with open(log_file, "r") as f:
    for line in f:
        parts = line.split("|")

        cpu = float(parts[1].split(":")[1].replace("%",""))
        memory = float(parts[2].split(":")[1].replace("%",""))
        disk = float(parts[3].split(":")[1].replace("%",""))

        cpu_values.append(cpu)
        memory_values.append(memory)
        disk_values.append(disk)

def analyze_trend(values, metric):
    if len(values) < 5:
        print(f"Not enough data for {metric}")
        return
    
    if values[-1] > values[0]:
        print(f"{metric} usage is trending UP ⚠️")
    else:
        print(f"{metric} usage is stable ✅")

analyze_trend(cpu_values, "CPU")
analyze_trend(memory_values, "Memory")
analyze_trend(disk_values, "Disk")
