# Initialize the lists
tasks = ["Planning", "Design", "Coding", "Testing"]
time_spent = [0.0] * len(tasks)  # Initialize with zeros

def log_time(task_name, amount_of_time):
    """Logs the time spent on a given task."""
    if task_name in tasks:
        index = tasks.index(task_name)
        time_spent[index] += amount_of_time
    else:
        print("Task not found.")

# Main loop to log time
while True:
    # Get user input
    task_name = input("Enter a task (or type 'exit' to finish): ")
    if task_name.lower() == 'exit':
        break
    try:
        amount_of_time = float(input("Enter the time spent on this task (in hours): "))
        log_time(task_name, amount_of_time)
    except ValueError:
        print("Please enter a valid number for time.")

# Print summary of time spent on each task
print("\nSummary of time spent on tasks:")
for task, time in zip(tasks, time_spent):
    print(f"{task}: {time} hours")
