# Author: [Chirag Khurana-100949693 and Saquib Ahmed Khan-100949697]
# Date: [27 September 2024]
# Description: This python code gives us a cloud resource allocating system that checks if requested resources are available.

# Define constants
TOTAL_CPU_CORES = 100  # total number of CPU cores available
TOTAL_MEMORY_GB = 1000.0  # total amount of memory available in GB

# Calculate 80% of total resources
CPU_CORES_THRESHOLD = TOTAL_CPU_CORES * 0.8
MEMORY_GB_THRESHOLD = TOTAL_MEMORY_GB * 0.8

# Input required resources from the user
required_cpu_cores = int(input("Enter the number of required CPU cores: "))
required_memory_gb = float(input("Enter the amount of required memory in GB: "))

# Check for invalid input and resource availability
if required_cpu_cores < 0 or required_memory_gb < 0:
    print("Invalid input. Resources cannot be negative.")
else:
    if required_cpu_cores > TOTAL_CPU_CORES or required_memory_gb > TOTAL_MEMORY_GB:
        print("Resource request exceeds capacity. Provisioning failed.")
        remaining_cpu_cores = TOTAL_CPU_CORES
        remaining_memory_gb = TOTAL_MEMORY_GB
    else:
        if required_cpu_cores > CPU_CORES_THRESHOLD or required_memory_gb > MEMORY_GB_THRESHOLD:
            print("Warning: Request exceeds 80% of total resources.")
        print("Resources provisioned successfully")
        remaining_cpu_cores = TOTAL_CPU_CORES - required_cpu_cores
        remaining_memory_gb = TOTAL_MEMORY_GB - required_memory_gb

# Display the total remaining available CPU cores and memory
print(f"Remaining CPU cores: {remaining_cpu_cores}")
print(f"Remaining memory: {remaining_memory_gb:.2f} GB")