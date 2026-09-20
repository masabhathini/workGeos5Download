#!/bin/bash

TO="${USER_EMAILS}"
SUBJECT="Globus task Error: ${CYLC_TASK_NAME} at cycle ${CYLC_TASK_CYCLE_POINT}"
# Check if task_id is set
#if [[ -z "$task_id" ]]; then
#  echo "❌ ERROR: task_id is not set." >&2
#  exit 1
#fi
# Safely capture task status output (assumes $task_id is set)
TASK_INFO=$($globus task show "$task_id" 2>&1)

{
echo "To: ${TO}"
echo "Subject: ${SUBJECT}"
echo "Content-Type: text/html"
echo "MIME-Version: 1.0"
echo
cat <<EOF
<html>
  <body>
    <p style="font-size:20px; font-weight:bold; color:black;">Hello team members,</p>
    <p>
      Globus Job Failed:
      <span style="font-size:32px; font-weight:bold; color:red;">${CYLC_TASK_NAME}</span> at cycle
      <b style="font-size:32px; font-weight:bold; color:black;">${CYLC_TASK_CYCLE_POINT}</b>
    </p>
    <p>
      <b>Globus Task ID:</b> $task_id<br><br>
      <b>Globus Task Details:</b><br>
      <pre style="background:#f5f5f5; padding:10px; border:1px solid #ccc;">${TASK_INFO}</pre>
    </p>
    <p>
      Contact: <b>sateesh.masabathini@kaust.edu.sa</b>
    </p>
    <p>Regards,<br>Automation Bot</p>
  </body>
</html>
EOF
} | /usr/sbin/sendmail -t
