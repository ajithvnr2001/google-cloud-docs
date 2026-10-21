---
url: https://docs.cloud.google.com/scheduler/docs/viewing-logs/
title: View logs \u00a0|\u00a0 Cloud Scheduler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:58.054315+00:00
---

# View logs  |  Cloud Scheduler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/viewing-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback 

#  View logs Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Scheduler publishes logs at the start of each execution and at the end of each execution. You can retrieve, view, and analyze the logs for a specific job, including the [audit logs that are available for Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/audit-logging).

To view logs, follow these steps:

  1. In the Google Cloud console, go to the **Cloud Scheduler** page.

[Go to Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

  2. In the row of the job that you want to view the logs for, click more_vert **Actions** > **View logs**.

The Logs Explorer page opens and lets you display log entries, parse and analyze them, and specify query parameters.

To learn more about viewing logs in Logging, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).




### Sample queries

Query description | Expression  
---|---  
Cloud Scheduler type and method | 
    
    
        resource.type="audited_resource"
        protoPayload.methodName=~"google.cloud.scheduler.v1.CloudScheduler.*"  
  
Cloud Scheduler log name | 
    
    
        logName=("projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
        OR "projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access"
        OR "projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
        OR "projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fpolicy")
        protoPayload.serviceName="cloudscheduler.googleapis.com"
          
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
