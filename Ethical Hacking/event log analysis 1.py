import os
import matplotlib.pyplot as plt
import time

# Define the name of the file to be analyzed
File = 'analysis_log_02_Jan_2020.txt'

# Define the directory where the file is located
directory = "H:\Desktop"

# Construct the full path to the file
Path = os.path.join(directory, File)

# Define a nested dictionary to store event IDs and their counts
nested_dictionary = {
    "1102": {"count": 0},
    "4611": {"count": 0},
    "4624": {"count": 0},
    "4634": {"count": 0},
    "4648": {"count": 0},
    "4661": {"count": 0},
    "4662": {"count": 0},
    "4663": {"count": 0},
    "4672": {"count": 0},
    "4673": {"count": 0},
    "4688": {"count": 0},
    "4698": {"count": 0},
    "4699": {"count": 0},
    "4702": {"count": 0},
    "4703": {"count": 0},
    "4719": {"count": 0},
    "4732": {"count": 0},
    "4738": {"count": 0},
    "4742": {"count": 0},
    "4776": {"count": 0},
    "4798": {"count": 0},
    "4799": {"count": 0},
    "4985": {"count": 0},
    "5136": {"count": 0},
    "5140": {"count": 0},
    "5142": {"count": 0},
    "5156": {"count": 0},
    "5158": {"count": 0},
}

# Create a dictionary comprehension to duplicate the structure of nested_dictionary
eventIDs = {event_id: {"count": 0} for event_id in nested_dictionary}

# Open the file for reading
with open(Path, 'r') as file:
    # Iterate through each line in the file
    for line in file:
    # Check if the line contains "MATCHED Event ID:"
        if "MATCHED Event ID:" in line:
        # Extract the event ID from the line
            eventID = line.strip("MATCHED Event ID: \n")
# Check if the extracted event ID exists in the eventIDs dictionary
            if eventID in eventIDs:
                eventIDs[eventID]["count"] += 1

# Define the folder path for storing logs
log_folder = os.path.join(directory, 'CI5235_k2121774_Mohamud', 'CI5235_logs')

# Create the log folder if it doesn't exist
os.makedirs(log_folder, exist_ok=True)

# Construct the file path for the log file with timestamp
log_file_path = os.path.join(log_folder, f'visdata_log_{time.strftime("%Y%m%d-%H%M%S")}.txt')

# Open the log file for writing
with open(log_file_path, 'w') as log_file:
# Write event IDs and their counts to the log file
    for event_id, data in eventIDs.items():
        log_file.write(f'Event ID: {event_id}, Total Count: {data["count"]}\n')

# Plotting the data
plt.barh(list(eventIDs.keys()), [data["count"] for data in eventIDs.values()])
plt.xlabel('Count')
plt.ylabel('Event ID')
plt.title('Event ID Counts')
plt.show()
