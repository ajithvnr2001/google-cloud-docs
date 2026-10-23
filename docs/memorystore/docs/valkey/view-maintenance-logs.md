---
url: https://docs.cloud.google.com/memorystore/docs/valkey/view-maintenance-logs/
title: View maintenance logs \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:49.346001+00:00
---

# View maintenance logs  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/view-maintenance-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  View maintenance logs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to find and use [Cloud Logging](https://docs.cloud.google.com/logging/docs) to query and view maintenance logs for a Memorystore for Valkey instance.

## View logs for scheduled maintenance

You can use the Google Cloud console to query and view logs for scheduled maintenance.

### Console

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Logs Explorer](https://console.cloud.google.com/logs/query)

  2. At the top of the page, select your Google Cloud project.

  3. From the time-range menu, select a range for which you want to query maintenance logs. For example, you can query for logs that Memorystore for Valkey captured over the past 30 days.

  4. In the Query builder, add the following lines of code:
         
         logName="projects/PROJECT_NAME/logs/maintenance.googleapis.com%2Factivity_log"
         labels.activity_type_name="CloudMemorystoreRolloutAdvanced"
         

Replace PROJECT_NAME with the name of your Google Cloud project.

  5. Click **Run query**. The logs appear for scheduled maintenance.




## View logs for in-progress maintenance

You can use the Google Cloud console to query and view logs for maintenance that's in progress.

### Console

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Logs Explorer](https://console.cloud.google.com/logs/query)

  2. At the top of the page, select your Google Cloud project.

  3. From the time-range menu, select a range for which you want to query maintenance logs. For example, you can query for logs that Memorystore for Valkey captured over the past 30 days.

  4. In the Query builder, add the following lines of code:
         
         logName="projects/PROJECT_NAME/logs/maintenance.googleapis.com%2Factivity_log"
         labels.activity_type_name="CloudMemorystoreRolloutInProgress"
         labels.is_completed="false"
         

Replace PROJECT_NAME with the name of your Google Cloud project.

  5. Click **Run query**. The logs appear for maintenance that's in progress.




## View logs for completed maintenance

You can use the Google Cloud console to query and view logs for maintenance that's completed.

### Console

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Logs Explorer](https://console.cloud.google.com/logs/query)

  2. At the top of the page, select your Google Cloud project.

  3. From the time-range menu, select a range for which you want to query maintenance logs. For example, you can query for logs that Memorystore for Valkey captured over the past 30 days.

  4. In the Query builder, add the following lines of code:
         
         logName="projects/PROJECT_NAME/logs/maintenance.googleapis.com%2Factivity_log"
         labels.activity_type_name="CloudMemorystoreRolloutInProgress"
         labels.is_completed="true"
         

Replace PROJECT_NAME with the name of your Google Cloud project.

  5. Click **Run query**. The logs appear for maintenance that's completed.




## View logs for canceled maintenance

You can use the Google Cloud console to query and view logs for maintenance that's canceled.

### Console

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Logs Explorer](https://console.cloud.google.com/logs/query)

  2. At the top of the page, select your Google Cloud project.

  3. From the time-range menu, select a range for which you want to query maintenance logs. For example, you can query for logs that Memorystore for Valkey captured over the past 30 days.

  4. In the Query builder, add the following lines of code:
         
         logName="projects/PROJECT_NAME/logs/maintenance.googleapis.com%2Factivity_log"
         labels.activity_type_name="CloudMemorystoreRolloutCanceled"
         

Replace PROJECT_NAME with the name of your Google Cloud project.

  5. Click **Run query**. The logs appear for maintenance that's canceled.




## Troubleshoot

This section lists issues that you might encounter when you try to view maintenance logs and provides guidance for resolving these issues.

### You deactivate the _Default sink in Cloud Logging

In [Logging](https://docs.cloud.google.com/logging/docs), every project, folder, and organization has the following [sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks):

  * **`_Required`** : capture [audit logs](https://docs.cloud.google.com/memorystore/docs/valkey/audit-logging) and store them in the `_Required` bucket.

You can't deactivate or delete this sink. Also, the logs in the bucket have a default retention period of 400 days.

  * **`_Default`** : route any Memorystore for Valkey logs, including maintenance logs, that the `_Required` sink doesn't capture. The `_Default` sink stores these logs in the `_Default` bucket.

Although you can't delete the `_Default`sink, you can deactivate it to stop it from routing logs to the `_Default` bucket. Also, the logs in the bucket have a default retention period of 30 days.




If you deactivate the `_Default` sink, then Logging drops all logs in the sink, including the `maintenance.googleapis.com/activity_log`, which is associated with all maintenance activities in Logging. As a result, Logging can't store the logs in the sink.

To check if you deactivated the `_Default` sink, do the following:

  1. Use the [`gcloud logging sinks describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/describe) command.
         
         gcloud logging sinks describe _Default --project=PROJECT_ID
         

Replace PROJECT_ID with the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the sink.

  2. In the output, look at the value of the `disabled` parameter. If the value is `true`, then you deactivated the sink and you must re-enable it.




To re-enable the sink, do the following:

  1. Use the [`gcloud logging sinks update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/update) command.
         
         gcloud logging sinks update _Default --no-disabled --project=PROJECT_ID
         

  2. To verify that the sink is enabled, use the [`gcloud logging sinks describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/describe) command.
         
         gcloud logging sinks describe _Default --project=PROJECT_ID
         

  3. In the output, confirm that the value of the `disabled` parameter is `false`. You re-enabled the sink.




### You don't configure sink filters correctly

In Logging, you can customize sinks to control which logs are stored in a Google Cloud project. To do this, create filters to specify the types of logs that you want the sinks to contain.

If you don't configure a filter for at least one sink to include logs with the log ID of `maintenance.googleapis.com/activity_log`, then Logging drops these logs. Because these logs are associated with all maintenance activities in Logging, you can't view the maintenance logs.

To check if the sink filters are configured correctly, do the following:

  1. Use the [`gcloud logging sinks list`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/list) command.
         
         gcloud logging sinks list --project=PROJECT_ID
         

Replace PROJECT_ID with the ID or project number of the Google Cloud project that contains the sink.

  2. Examine the `FILTER` column to see if it includes the `LOG_ID("maintenance.googleapis.com/activity_log")` filter. If either this filter doesn't appear or there's a broader filter that excludes this log (for example, `(NOT LOG_ID("cloudaudit.googleapis.com/activity_log)")`), then you customized all sinks to drop logs with the log ID of `maintenance.googleapis.com/activity_log`.

To resolve this, you must either [create](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/create) or [update](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/update) a sink to include the maintenance logs. For the `--log-filter` parameter, specify `LOG_ID("maintenance.googleapis.com/activity_log")` as the filter.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
