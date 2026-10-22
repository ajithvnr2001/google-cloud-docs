---
url: https://docs.cloud.google.com/batch/docs/write-task-logs/
title: Write task logs \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:26.401517+00:00
---

# Write task logs  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/write-task-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Write task logs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to write task logs and how to create and run a Batch job that has task logs.

When logging is enabled for a job, _task logs_ are generated from messages that the job's runnables print during run time. By configuring your runnables to write task logs, you can surface custom information in Cloud Logging, which can help make your jobs easier to analyze and troubleshoot. To learn more about logs, see [Analyze a job using logs](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job that writes logs, ask your administrator to grant you the following IAM roles: 

     * To create a job: 
       * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
       * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)
     * To view logs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Create and run a job that has task logs

To create and run a job that you want to have task logs, do the following when you are [creating the job](https://docs.cloud.google.com/batch/docs/create-run-basic-job):

  1. [Enable logs for the job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs). This allows any logs written for the job to be generated.
  2. For each task log that you want the job to have, add a command that writes a task log to a runnable. When the job runs, a task log gets generated whenever a command to write a task log is executed.

To learn how to write task logs, see Write task logs in this document.




## Write task logs

A task log is written for any content that a job's runnables print to the [standard output (`stdout`) stream or standard error (`stderr`) stream](https://en.wikipedia.org/wiki/Standard_streams) during run time. For example, you can write task logs by using the [`echo` command](https://en.wikipedia.org/wiki/Echo_\(command\)). The structure of the resulting task log varies based on how you formatted the printed content. Specifically, you can write each task log using one of the following options:

  * Write an unstructured log by printing a string. Unstructured logs are simple and only let you define the log's `textPayload` field.

  * Write a structured log by printing JSON. Structured logs require JSON formatting, which lets you define multiple fields, including some standard log fields, custom fields, and custom status events.

For example, you can use structured task logs to define the log's severity, which you can use as a filter when [viewing logs for a job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs#view-job-logs).




### Write an unstructured log by printing a string

Unstructured logs let you define a message, which is a string that appears in the log's `textPayload` field.

To write an unstructured log, print an unformatted string as demonstrated in the following sections.

#### Example unstructured log

For example, suppose that you want a task log that contains the following string:
    
    
    MESSAGE
    

Printing this example string results in a task log that's similar to the following:
    
    
    insertId: ...
    labels: ...
    logName: projects/PROJECT_ID/logs/batch_task_logs
    receiveTimestamp: ...
    resource: ...
    severity: INFO
    textPayload: MESSAGE
    timestamp: ...
    

Replace the following:

  * `MESSAGE`: the message, which is a string that summarizes the purpose of the task log—for example, `The summary for a task log.`.
  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.



#### Print a string

You can print a string using a variety of methods, such as by including the following `echo` command in a runnable:
    
    
    echo MESSAGE
    

For comprehensive examples of jobs that use the `echo` command to write unstructured task logs, see [Create and run a basic job](https://docs.cloud.google.com/batch/docs/create-run-basic-job).

### Write a structured log by printing a JSON object

Structured logs let you define any of the following:

  * [Standard fields supported by the Cloud Logging agent](https://docs.cloud.google.com/logging/docs/structured-logging#structured_logging_special_fields)
  * Custom fields
  * Custom status events



To write a structured log, print a JSON object. The following sections demonstrates how to define a log with some of the standard fields and custom fields. If you want to learn how to define a log with custom status events, also see [Configure custom status events](https://docs.cloud.google.com/batch/docs/create-run-job-custom-status-events).

#### Example structured log

For example, suppose you want a task log that contains the information in the following JSON object, which defines a message, severity, and two custom fields.
    
    
    {
      "message": "MESSAGE"
      "severity": "SEVERITY"
      "CUSTOM_FIELD_1": CUSTOM_VALUE_1
      "CUSTOM_FIELD_2": CUSTOM_VALUE_2
    }
    

Printing this JSON object results in a task log that's similar to the following:
    
    
    insertId: ...
    jsonPayload:
      "CUSTOM_FIELD_1": CUSTOM_VALUE_1
      "CUSTOM_FIELD_2": CUSTOM_VALUE_2
      message: MESSAGE
    labels: ...
    logName: projects/PROJECT_ID/logs/batch_task_logs
    receiveTimestamp: ...
    resource: ...
    severity: SEVERITY
    timestamp: ...
    

Replace the following:

  * `MESSAGE`: the message, which is a string that summarizes the purpose of the task log—for example, `The summary for a task log.`.
  * `SEVERITY`: the severity of the log, which you can use as a filter when [viewing logs for a job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs#view-job-logs). The severity must be one of the [`LogSeverity` enums](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity) converted to a string with only the first letter capitalized. For example, for the `ERROR` enum, specify `Error`.
  * `CUSTOM_FIELD_1` and `CUSTOM_FIELD_2`: the names of custom fields for the task log—for example, `custom_field_1` and `custom_field_2`.
  * `CUSTOM_VALUE_1` and `CUSTOM_VALUE_2`: the values of custom fields for the task log, which can be various data types and might need quotes—for example, `"the first custom field"` and `2`.
  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.



#### Print a JSON object

You can print this example JSON object using a variety of methods. For example, the following samples demonstrate some of the possible methods for printing the example JSON object:

  * Print an equivalent string using the `echo` command.
  * Print an equivalent [dictionary](https://en.wikipedia.org/wiki/Associative_array) using Python.




### echo command

To print the example JSON object by using the `echo` command and an equivalent string, include the following command in a runnable:
    
    
    echo '{\"message\":\"MESSAGE\", \"severity\":\"SEVERITY\", \"CUSTOM_FIELD_1\":CUSTOM_VALUE_1, \"CUSTOM_FIELD_2\":CUSTOM_VALUE_2}'
    

For example, suppose you create and run a job with the following runnable:
    
    
    "script": {
      "text": "echo '{\"message\":\"The message for a structured log.\", \"severity\":\"Error\", \"custom_field_1\":\"the first custom field\", \"custom_field_2\":2}'"
    }
    

Then, the resulting task log is similar to the following:
    
    
    insertId: ...
    jsonPayload:
      custom_field_1: the first custom field
      custom_field_2: 2
      message: The summary for a structured task log with error severity.
    labels: ...
    logName: projects/PROJECT_ID/logs/batch_task_logs
    receiveTimestamp: ...
    resource: ...
    severity: ERROR
    timestamp: ...
    

### Python

To print the example JSON object using Python and an equivalent dictionary, include the following sample in a runnable:
    
    
    #!/usr/bin/env python3
    
    import json
    
    entry = dict(
        severity="SEVERITY",
        message="MESSAGE",
        CUSTOM_FIELD_1=CUSTOM_VALUE_1,
        CUSTOM_FIELD_2=CUSTOM_VALUE_2,
    )
    print(json.dumps(entry))
    

For example, suppose you create and run a job with the following runnable:
    
    
    "script": {
      "text": "#!/usr/bin/env python3\n\nimport json\n\nentry = dict(\nseverity=\"Error\",\nmessage=\"The summary for a structured task log with error severity.\",\ncustom_field_1=\"the first custom field\",\ncustom_field_2=2,\n)\nprint(json.dumps(entry))"
    }
    

Then, the resulting task log is similar to the following:
    
    
    insertId: ...
    jsonPayload:
      custom_field_1: the first custom field
      custom_field_2: 2
      message: The summary for a structured task log with error severity.
    labels: ...
    logName: projects/PROJECT_ID/logs/batch_task_logs
    receiveTimestamp: ...
    resource: ...
    severity: ERROR
    timestamp: ...
    

## What's next

  * For more information about formatting logs, see [Structured logging](https://docs.cloud.google.com/logging/docs/structured-logging) in the Cloud Logging documentation.
  * Learn how to [write structured task logs that include custom status events](https://docs.cloud.google.com/batch/docs/create-run-job-custom-status-events).
  * Learn how to [view the task logs for a job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs#view-job-logs).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
