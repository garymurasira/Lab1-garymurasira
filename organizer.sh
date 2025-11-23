#!/bin/bash   # Shebang: tells the system to run this script with Bash

# Check if "archive" directory exists; if not, create it
if [ ! -d "archive" ]; then
    mkdir archive
fi

# Loop through all CSV files in the current directory
for file in *.csv; do
    # If no CSV files exist, skip the loop
    [ -e "$file" ] || continue

    # Generate a timestamp (YYYYMMDD-HHMMSS format)
    timestamp=$(date '+%Y%m%d-%H%M%S')

    # Create a new filename by appending the timestamp before .csv
    newname="${file%.csv}-$timestamp.csv"

    # Write entry log details to organizer.log
    echo "========ENTRY LOG========" >> organizer.log
    echo "$(date '+%Y-%m-%d %H:%M:%S'): Renamed $file as $newname" >> organizer.log
    echo "$(date '+%Y-%m-%d %H:%M:%S'): Moved $newname to archive Directory" >> organizer.log
    echo "----- Contents Of The File -----" >> organizer.log
    cat "$file" >> organizer.log   # Append the contents of the CSV file to the log
    echo "========END OF ENTRY LOG========" >> organizer.log
    echo "" >> organizer.log       # Add a blank line for readability

    # Move the original file into the archive directory with the new name
    mv "$file" "archive/$newname"
done

# Final message after processing all files
echo "Archiving complete. Check organizer.log for details."