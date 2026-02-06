import re
from statistics import mean

# Read log data from file
with open('output.log', 'r', encoding='utf-8') as file:
    log_data = file.read()

# Extract response times and session keys
response_times = []
session_keys = set()

response_pattern = re.compile(r'OpenAI response in (\d+)ms for (\w+)')

for match in response_pattern.finditer(log_data):
    response_time_ms = int(match.group(1))
    session_key = match.group(2)
    response_times.append(response_time_ms)
    session_keys.add(session_key)

# Results
average_response_time = mean(response_times) if response_times else 0
unique_sessions = len(session_keys)

print(f"Average Response Time: {average_response_time:.2f} ms")
print(f"Unique Session Keys: {unique_sessions}")
