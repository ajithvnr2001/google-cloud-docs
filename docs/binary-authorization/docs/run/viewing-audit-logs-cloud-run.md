---
url: https://docs.cloud.google.com/binary-authorization/docs/run/viewing-audit-logs-cloud-run/
title: View audit logs for Cloud Run events \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:19.646536+00:00
---

# View audit logs for Cloud Run events  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/run/viewing-audit-logs-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  View audit logs for Cloud Run events Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to view Binary Authorization for Cloud Run in Cloud Audit Logs.

## Blocked deployment events in Cloud Logging

###  Logs Explorer 

To view bocked deployment events in the Cloud Logging Logs Explorer, do the following:

  1. Go to the Cloud Audit Logs Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer).

  2. In the **Project Selector** at the top of the page, select the Google Cloud project ID of the project in which you run Cloud Run.

  3. Enter the following query in the _search-query_ box:
         
         resource.type="cloud_run_revision"
         logName:"cloudaudit.googleapis.com%2Fsystem_event"
         protoPayload.response.status.conditions.reason="ContainerImageUnauthorized"
         

  4. Select the time range in the _time-range selector_.




To search within the log entries, click **Expand nested fields**.

###  gcloud 

To view policy violation events from the past week in Cloud Logging using the Google Cloud CLI, do the following:
    
    
    gcloud logging read --order="desc" --freshness=7d \
      'resource.type="cloud_run_revision" AND
       logName:"cloudaudit.googleapis.com%2Fsystem_event" AND
       protoPayload.response.status.conditions.reason="ContainerImageUnauthorized"'
    

## Breakglass events in Cloud Logging

[Breakglass](https://docs.cloud.google.com/binary-authorization/docs/run/using-breakglass-cloud-run) enables you to override Binary Authorization policy enforcement and deploy a container image that violates the policy.

## Query Cloud Logging for revisions with breakglass specified

###  Logs Explorer 

To view breakglass events in the Cloud Logging Logs Explorer, do the following:

  1. Go to the Cloud Audit Logs Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer).

  2. In the **Project Selector** at the top of the page, select the project ID of the project in which you run Cloud Run.

  3. Enter the following in the _search-query_ box:
         
         resource.type="cloud_run_revision"
         logName:"cloudaudit.googleapis.com%2Fsystem_event"
         "breakglass"
         

To further refine your search, add the following lines:
         
         resource.labels.service_name = SERVICE_NAME
         resource.labels.location = LOCATION
         

[View breakglass deployments in Cloud Logging](https://console.cloud.google.com/logs/viewer?advancedFilter=resource.type%3D%22cloud_run_revision%22%0AlogName%3A%22cloudaudit.googleapis.com%252Factivity%22%0A%22breakglass%22)

  4. Select the time range in the _time-range selector_.




To search within the log entries, click **Expand nested fields**.

###  gcloud 

To view breakglass events from the past week in Cloud Logging using the gcloud CLI, do the following:
    
    
    gcloud logging read --order="desc" --freshness=7d \
      'resource.type="cloud_run_revision" AND
       logName:"cloudaudit.googleapis.com%2Fsystem_event" AND
       "breakglass"'
    

## Query Cloud Logging fail open events

###  Logs Explorer 

To view fail open events in the Cloud Logging Logs Explorer, do the following:

  1. Go to the Cloud Audit Logs Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer).

  2. In the **Project Selector** at the top of the page, select the project ID of the project in which you run Cloud Run.

  3. Enter the following in the _search-query_ box:
         
         resource.type="cloud_run_revision"
          logName:"cloudaudit.googleapis.com%2Fsystem_event"
          "encountered an error"
         

  4. Select the time range in the _time-range selector_.




To search within the log entries, click **Expand nested fields**.

###  gcloud 

To view fail open events from the past week in Cloud Logging using the gcloud CLI, do the following:
    
    
    gcloud logging read --order="desc" --freshness=7d \
      'resource.type="cloud_run_revision" AND
        logName:"cloudaudit.googleapis.com%2Fsystem_event" AND
        "encountered an error"'
    

## Query Cloud Logging for dry run events

###  Logs Explorer 

To view dry run events in the Cloud Logging Logs Explorer, do the following:

  1. Go to the Cloud Audit Logs Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer).

  2. In the **Project Selector** at the top of the page, select the project ID of the project in which you run Cloud Run.

  3. Enter the following in the _search-query_ box:
         
         resource.type="cloud_run_revision"
         logName:"cloudaudit.googleapis.com%2Fsystem_event"
         "dry run"
         

  4. Select the time range in the _time-range selector_.




To search within the log entries, click **Expand nested fields**.

###  gcloud 

To view dry run deployment events from the past week in Cloud Logging using the gcloud CLI, do the following:
    
    
    gcloud logging read --order="desc" --freshness=7d \
      'resource.type="cloud_run_revision" AND
       logName:"cloudaudit.googleapis.com%2Fsystem_event" AND
       "dry run"'
    

## What's next

  * Configure the Binary Authorization policy using the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console) or the [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli).

  * [Use attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations) to deploy only signed container images.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
