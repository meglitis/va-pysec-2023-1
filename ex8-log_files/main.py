import re

# filtering log file by line, records containing usb

with open('syslog') as log_file:
    for line in log_file:
        if line.__contains__('usb'):
            print(line)

# parsing log line and finding kernel perf details

pattern = r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}) (\w+) (\w+): \[(\s*\d+\.\d+)\] (\w+): (.*)'

with open('syslog', 'r') as file:
    log = file.read()

matches = re.findall(pattern, log, re.MULTILINE)
for match in matches:
    timestamp, hostname, kernel, time, stream, message = match
    if stream == 'perf':
        print(f"Timestamp: {timestamp}")
        print(f"Hostname: {hostname}")
        print(f"Kernel: {kernel}")
        print(f"Time: {time}")
        print(f"Stream: {stream}")
        print(f"Message: {message}")
        print()
