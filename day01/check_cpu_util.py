import psutil

threshold_cpu = int(input("Enter the CPU threshold value: "))

def get_cpu_utilization(threshold_cpu):
    cpu_util = psutil.cpu_percent()
    print("Current CPU utilization: ",cpu_util)
    if cpu_util > threshold_cpu:
        print("Send an alert on the email!!!!!!!")
    else:
        print("System is safe")


get_cpu_utilization(threshold_cpu)