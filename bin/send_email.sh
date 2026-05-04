#!/bin/bash
# Arguments
TASK_NAME=$1
TASK_STATE=$2
LOG_PATH=$3

# Create a formatted table (example)
TABLE="$(printf 'Status\tTask\n%s\t%s' "$TASK_STATE" "$TASK_NAME")"

# Fetch log content (tail for last 20 lines for example)
LOG_CONTENT=$(tail -n 20 "$LOG_PATH")

# Compose email
SUBJECT="Cylc Task Notification: $TASK_NAME"
BODY="Hello,\n\nTask $TASK_NAME has changed state to $TASK_STATE.\n\nLogs:\n$LOG_CONTENT\n\nDetails:\n$TABLE"

# Send email (using mailx here, ensure it is configured on your server)
echo -e "$BODY" | mailx -s "$SUBJECT" your-email@example.com

# Ensure this script is executable
chmod +x send_email.sh

