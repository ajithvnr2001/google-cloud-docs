---
url: https://docs.cloud.google.com/looker/docs/looker-core-logging/
title: View instance logs for Looker (Google Cloud core) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:54.923514+00:00
---

# View instance logs for Looker (Google Cloud core)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  View instance logs for Looker (Google Cloud core) Stay organized with collections  Save and categorize content based on your preferences. 

You can use Cloud Logging to view and query logs for your Looker (Google Cloud core) instance. Monitoring these logs helps you troubleshoot issues, track usage, and ensure the health and security of your Looker environment, providing reliable data for your operations. For more details on Cloud Logging, see the [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs).

## Required roles

To understand the required roles for Cloud Logging, visit the [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control) page of the Cloud Logging documentation.

## View logs

To view logs for your Looker (Google Cloud core) instance log entries, select one of the following options:

### console

  1. In the Google Cloud console, go to **Logging > Logs Explorer**
  2. Select an existing Looker (Google Cloud core) project at the top of the page.
  3. In the Query builder, add the following:
     * Resource: Select **Looker instance**. In the dialog, select a Looker (Google Cloud core) instance ID.
     * Log names: Scroll to the Looker section and select appropriate log files for your instance. For example: 
       * looker.googleapis.com%2FContentAccess
       * looker.googleapis.com%2FUserLogin
     * Severity: Select a log level.
     * Time range: Select a preset or create a custom range.



###  gcloud 

Use the [`gcloud logging`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command to view log entries.
    
    
    gcloud logging read "resource.type=looker.googleapis.com/Instance" \
    --project=PROJECT_ID \
    --limit=10 \
    --format=json

Replace the following:

  * PROJECT_ID: the ID of the Google Cloud project in which the Looker (Google Cloud core) instance resides.



You may also include the following flags:

  * The [`limit`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--limit) flag is an optional parameter that indicates the maximum number of entries to return.



## Troubleshoot

Issue | Troubleshooting | Log files are incomplete. | Check the [severity level](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity) at which your logging is configured. Log messages below the level configured will be dropped.   
---|---  
Operations information is not found in logs. | You want to find more information about an operation. For example, a user was deleted but you can't find out who did it. The logs show the operation started but don't provide any more information. You must [enable audit logging](https://docs.cloud.google.com/logging/docs/audit) for detailed and personal identifying information (PII) like this to be logged.  
Log files are hard to read. | You'd rather view the logs as JSON or text. You can use the [ `gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command along with Linux post-processing commands to download the logs. To download the logs as JSON, use the following code:
    
    
    gcloud logging read \
    "resource.type=looker.googleapis.com/Instance \
    AND logName=projects/PROJECT_ID \
    /logs/looker.googleapis.com%2FLOG_NAME" \
    --format json \
    --project=PROJECT_ID \
    --freshness="1d" \
    > downloaded-log.json
        

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project in which the Looker (Google Cloud core) instance resides
  * `LOG_NAME`: the resource name of the log

To download the logs as text, use the following code:
    
    
    gcloud logging read \
    "resource.type=looker.googleapis.com/Instance \
    AND logName=projects/PROJECT_ID \
    /logs/looker.googleapis.com%2FLOG_NAME" \
    --format json \
    --project=PROJECT_ID \
    --freshness="1d"| jq -rnc --stream 'fromstream(1|truncate_stream(inputs)) \
    | .textPayload' \
    --order=asc
    > downloaded-log.txt
       

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project in which the Looker (Google Cloud core) instance resides
  * `LOG_NAME`: the resource name of the log

  
  
## What's next

  * [Looker (Google Cloud core) audit logging](https://docs.cloud.google.com/looker/docs/looker-core-audit-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
