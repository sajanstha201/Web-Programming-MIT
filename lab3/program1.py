import statistics

def calculate_statistics(data):
    mean_value = statistics.mean(data)
    variance_value = statistics.variance(data)
    std_dev_value = statistics.stdev(data)
    print("Mean: ",mean_value,"\nVarience: ",variance_value,"\nStd: ",std_dev_value)
arr=list(map(int,input("Enter the list:").split()))
calculate_statistics(arr)