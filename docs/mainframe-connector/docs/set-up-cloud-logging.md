---
url: https://docs.cloud.google.com/mainframe-connector/docs/set-up-cloud-logging/
title: Set up Cloud Logging \u00a0|\u00a0 Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:06.608807+00:00
---

# Set up Cloud Logging  |  Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/set-up-cloud-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-connector/docs/overview)



Send feedback 

#  Set up Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

Mainframe Connector can send JSON formatted log messages containing context information to Cloud Logging. The context includes job name, job ID, job date, step name, and other variables provided by z/OS.

This helps you find logs for specific jobs and create alerts. Additionally, when deploying Mainframe Connector on Cloud Run, Google Kubernetes Engine, or Compute Engine, the logs are collected by the Cloud Logging agent and appear in Logs Explorer.

## Configure Cloud Logging in JCL

To configure Mainframe Connector to write to Cloud Logging, set the `LOG_PROJECT` and `LOG_ID` environment variables in the JCL that launches the job.
    
    
    LOG_PROJECT=PROJECT_ID
    LOG_ID=LOG_ID
    

Replace the following:

  * `PROJECT_ID`: the name of the Google Cloud project where you want to store the logs. For example, `mainframe-connector-proj`.
  * `LOG_ID`: an identifier for your log stream. For example, `my-mfc`.



The log name (`LOG_NAME`) is derived from `LOG_PROJECT` and `LOG_ID`. In this example, the log name is:
    
    
    projects/mainframe-connector-proj/logs/my-mfc
    

The resource type is always _global_ because the log is a user-created log rather than a service-managed log. During startup, Mainframe Connector displays a message indicating whether Cloud Logging is configured.

## View logs in Logs Explorer

After configuring Cloud Logging, you can search and filter your logs in Logs Explorer:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the query pane, filter by resource type **Global** or by your log name:
         
         logName="projects/PROJECT_ID/logs/LOG_ID"
         




## What's next

  * [Monitor Mainframe Connector performance](https://docs.cloud.google.com/mainframe-connector/docs/monitor-performance)
  * [Publish messages to Pub/Sub from your mainframe](https://docs.cloud.google.com/mainframe-connector/docs/pub-sub)
  * [Run Cloud Run jobs using Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/run-jobs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
