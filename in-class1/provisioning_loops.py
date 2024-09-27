# Author: [Chirag Khurana-100949693 and Saquib Ahmed Khan-100949697]
# Date: [27 September 2024]
# Description: This python code gives us a cloud resource allocating system that checks if requested resources are available.


# Define constants
TOTAL_CPU_CORES = 100  # total number of CPU cores available
TOTAL_MEMORY_GB = 1000.0  # total amount of memory available in GB

# Calculate 90% of total resources
CPU_CORES_THRESHOLD = TOTAL_CPU_CORES * 0.9
MEMORY_GB_THRESHOLD = TOTAL_MEMORY_GB * 0.9

# Initialize empty lists
allocated_resources = []
pending_requests = []

# Initialize available resources
available_cpu_cores = TOTAL_CPU_CORES
available_memory_gb = TOTAL_MEMORY_GB

while True:
    # Ask the user for a request
    username = input("Enter your username: ")
    required_cpu_cores = int(input("Enter the number of required CPU cores: "))
    required_memory_gb = float(input("Enter the amount of required memory in GB: "))

    # Check for invalid input
    if required_cpu_cores < 0 or required_memory_gb < 0:
        print("Invalid input. Resources cannot be negative.")
        continue

    # Check if the required resources are available
    if required_cpu_cores <= available_cpu_cores and required_memory_gb <= available_memory_gb:
        if required_cpu_cores > CPU_CORES_THRESHOLD or required_memory_gb > MEMORY_GB_THRESHOLD:
            print("Warning: Request exceeds 90% of total resources.")
        allocated_resources.append({
            "username": username,
            "cpu_cores": required_cpu_cores,
            "memory_gb": required_memory_gb
        })
        available_cpu_cores -= required_cpu_cores
        available_memory_gb -= required_memory_gb
        print("Resources provisioned successfully")
    else:
        pending_requests.append({
            "username": username,
            "cpu_cores": required_cpu_cores,
            "memory_gb": required_memory_gb
        })
        print("Resource request exceeds capacity. Provisioning failed.")

    # Ask the user if they want to make another request
    response = input("Do you want to make another request? (yes/no): ")
    if response.lower() != "yes":
        break

# Display the list of allocated resources and pending requests
print("Allocated Resources:")
print("Username\tCPU Cores\tMemory (GB)")
for resource in allocated_resources:
    print(f"{resource['username']}\t{resource['cpu_cores']}\t{resource['memory_gb']:.2f}")

print("\nPending Requests:")
print("Username\tCPU Cores\tMemory (GB)")
for request in pending_requests:
    print(f"{request['username']}\t{request['cpu_cores']}\t{request['memory_gb']:.2f}")

# Calculate total allocated resources
total_allocated_cpu_cores = sum(resource['cpu_cores'] for resource in allocated_resources)
total_allocated_memory_gb = sum(resource['memory_gb'] for resource in allocated_resources)

# Calculate total pending requests
total_pending_cpu_cores = sum(request['cpu_cores'] for request in pending_requests)
total_pending_memory_gb = sum(request['memory_gb'] for request in pending_requests)

# Display the total allocated resources and pending requests
print("\nSummary:")
print(f"Total Allocated CPU Cores: {total_allocated_cpu_cores}")
print(f"Total Allocated Memory (GB): {total_allocated_memory_gb:.2f}")
print(f"Total Pending CPU Cores: {total_pending_cpu_cores}")
print(f"Total Pending Memory (GB): {total_pending_memory_gb:.2f}")

# Calculate remaining available resources
remaining_cpu_cores = TOTAL_CPU_CORES - total_allocated_cpu_cores
remaining_memory_gb = TOTAL_MEMORY_GB - total_allocated_memory_gb

# Display the remaining available resources
print(f"\nRemaining Available Resources:")
print(f"CPU Cores: {remaining_cpu_cores}")
print(f"Memory (GB): {remaining_memory_gb:.2f}")