---
url: https://docs.cloud.google.com/dataproc-metastore/docs/logging/
title: Cloud Logging \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:19.248788+00:00
---

# Cloud Logging  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

You can view, search, filter, and archive Dataproc Metastore job logs in [Cloud Logging](https://docs.cloud.google.com/logging/docs).

  * See [Google Cloud Observability Pricing](https://cloud.google.com/stackdriver/pricing) to understand your costs.

  * See [Logs retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods) for information on log retention.

  * See [Logs Exclusions](https://docs.cloud.google.com/logging/docs/exclusions) to disable all logs or exclude logs from Logging.

  * See [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview) to route logs from Logging to Cloud Storage, BigQuery, or Pub/Sub.




## Access job logs in Logging

When you run Dataproc Metastore, a Hive metastore process output is streamed to the Logging.

You can access Logging using the [Logging console](https://console.cloud.google.com/logs/query), the [gcloud logging](https://docs.cloud.google.com/sdk/gcloud/reference/logging) command, or the [Logging API](https://docs.cloud.google.com/logging/docs/apis).

### Console

  1. In the Google Cloud console, go to the **Cloud Logging > Logs** (Logs Explorer) page:

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

  2. Select an existing Dataproc Metastore Google Cloud project.

  3. Under the **Resources** menu, select `Dataproc Metastore Service`.

  4. Under the **All logs** menu, select the log type that you want to see.




### gcloud

The Google Cloud CLI has a group of commands, `gcloud logging`, that provide a command-line interface to the Cloud Logging API. To read your log entries, run the following command:
    
    
    gcloud logging read \
        'resource.type="metastore.googleapis.com/Service"
        resource.labels.location=LOCATION
        resource.labels.service_id=SERVICE_ID'
    

### REST

Follow the Logging API instructions to list log entries ([entries.list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list)) by using the API Explorer.

## Dataproc Metastore service logs in Logging

Dataproc Metastore exports request and system logs to Cloud Logging.

Log Type | Log Name | logName query  
---|---|---  
Request logs | metastore.googleapis.com/requests | logName=(projects/$PROJECT_ID/logs/metastore.googleapis.com%2Frequests)  
System logs | metastore.googleapis.com/system | logName=(projects/$PROJECT_ID/logs/metastore.googleapis.com%2Fsystem)  
  
## What's next

  * [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
