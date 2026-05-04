#!/bin/bash

TO="${USER_EMAILS}"
SUBJECT="Operational Job Success: ${CYLC_TASK_NAME} at cycle ${CYLC_TASK_CYCLE_POINT}"
LOG_SNIPPET=$(tail -n 10 "${CYLC_TASK_LOG_ROOT}.out" 2>/dev/null)

{
echo "To: ${TO}"
echo "Subject: =?UTF-8?B?4pyFIA==?= ${SUBJECT}"
echo "Content-Type: text/html"
echo "MIME-Version: 1.0"
echo
cat <<EOF
<html>
  <body>
    <p style="font-size:20px; font-weight:bold; color:black;">Hello team members,</p>
    <p>
      Operational Job Succeeded:
      <span style="font-size:32px; font-weight:bold; color:green;">${CYLC_TASK_NAME}</span> at cycle
      <b style="font-size:32px; font-weight:bold; color:black;">${CYLC_TASK_CYCLE_POINT}</b>
      <br>Contact: <b>sateesh.masabathini@kaust.edu.sa</b>
    </p>
    <p style="font-size:18px; font-weight:bold; color:black;">The task completed successfully.</p>
    <p style="font-size:18px; font-weight:bold; color:black;">Logfile: ${CYLC_TASK_LOG_ROOT}.out</p>
    <p>This logfile contains output information.</p>

    <hr>
    <p>Here are the last few lines of the Output file:</p>
    <pre style="color:green;">${LOG_SNIPPET}</pre>

    <hr>
    <p style="font-size:20px; font-weight:bold; color:black;">Workflow Info:</p>
    <pre>
WHOAMI                            : $(whoami)
HOSTNAME                          : $HOSTNAME
HOME                              : $HOME
PWD                               : $(pwd)
CYLC_VERSION                      : ${CYLC_VERSION}
CYLC_WORKFLOW_INITIAL_CYCLE_POINT : ${CYLC_WORKFLOW_INITIAL_CYCLE_POINT}
CYLC_WORKFLOW_ID                  : ${CYLC_WORKFLOW_ID}
CYLC_WORKFLOW_NAME                : ${CYLC_WORKFLOW_NAME}
CYLC_WORKFLOW_NAME_BASE           : ${CYLC_WORKFLOW_NAME_BASE}
CYLC_TASK_JOB                     : ${CYLC_TASK_JOB}
CYLC_TASK_CYCLE_POINT             : ${CYLC_TASK_CYCLE_POINT}
CYLC_TASK_NAME                    : ${CYLC_TASK_NAME}
CYLC_TASK_ID                      : ${CYLC_TASK_ID}
CYLC_TASK_SUBMIT_NUMBER           : ${CYLC_TASK_SUBMIT_NUMBER}
CYLC_TASK_TRY_NUMBER              : ${CYLC_TASK_TRY_NUMBER}
CYLC_TASK_FLOW_NUMBERS            : ${CYLC_TASK_FLOW_NUMBERS}
CYLC_TASK_LOG_DIR                 : ${CYLC_TASK_LOG_DIR}
CYLC_TASK_LOG_ROOT                : ${CYLC_TASK_LOG_ROOT}
CYLC_TASK_WORK_DIR                : ${CYLC_TASK_WORK_DIR}
CYLC_TASK_NAMESPACE_HIERARCHY     : ${CYLC_TASK_NAMESPACE_HIERARCHY}
    </pre>

    <p>Regards,<br>Automation Bot</p>
  </body>
</html>
EOF
} | /usr/sbin/sendmail -t
