# log_analyzer.py

# Sample log data
log_data = """
INFO: System started
WARNING: High memory usage detected
ERROR: Unable to connect to database
INFO: Process completed
ERROR: Timeout occurred
"""

# Function to count occurrences of each log level
def count_log_entries(logs):
    log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    
    for line in logs.split("\n"):
        for key in log_counts.keys():
            if key in line:
                log_counts[key] += 1
    
    return log_counts

# Analyze the log data
results = count_log_entries(log_data)

# Print results
print("Log Summary:")
for log_type, count in results.items():
    print(f"{log_type}: {count}")
