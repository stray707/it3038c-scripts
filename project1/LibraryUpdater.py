import os
import shutil
from datetime import datetime

print('As a DJ, I have my main library of music files on my laptop, which is the device I usually use to DJ with. However, sometimes I will download music to my desktop, and I forget which songs to put back on my laptop, and vice versa.')
print('\nThis script is usually run from my laptop as the primary source, but I can also run it on my desktop as well.')
print('\nUsually, I have this scheduled to run automatically as a scheduled Windows task. For the sake of the project, I have modified this script to ask the user for the network drive paths.')
print('\nCurrently, this script is assuming the user is on Windows and has already set up their folders through network drive mapping in File Explorer.\n')

def getFilePath(promptMessage):
# Prompts the user for a file path
    return input(promptMessage)

# Paths
DESTINATION_PATH = getFilePath("Enter the destination path ('\\\\MACHINE_NAME\\SHARED_FOLDER'): ")
SOURCE_PATH = getFilePath("Enter the source path ('C:\\LOCAL\\LIBRARY\\PATH'): ")
LOG_FILE_PATH = getFilePath("Enter the path and file name for the log ('C:\\path_to_directory\\synclog.txt'): ")

# Get list of music files from the destination
destinationFiles = {
    f for _, _, files in os.walk(DESTINATION_PATH) 
    for f in files if f.endswith(('.mp3', '.flac', '.wav', '.m4a'))
    }

# Get list of music files from the source
sourceFiles = {
    f for _, _, files in os.walk(SOURCE_PATH) 
    for f in files if f.endswith(('.mp3', '.flac', '.wav', '.m4a'))
    }

# Determine which files are missing in the source
filesToCopy = destinationFiles - sourceFiles

def logMessage(message):
    # Print to console
    print(message)
    
    # Write to log file
    with open(LOG_FILE_PATH, 'a') as logFile:
        logFile.write(message + '\n')

# Log the current date and time
logMessage(f"\n--- Synchronization started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")

# Copy missing files from destination to source
for file in filesToCopy:
    for dirpath, _, filenames in os.walk(DESTINATION_PATH):
        if file in filenames:
            shutil.copy2(os.path.join(dirpath, file), SOURCE_PATH)
            logMessage(f"Transferred: {file}")
            break
