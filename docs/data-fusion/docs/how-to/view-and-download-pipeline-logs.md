---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/view-and-download-pipeline-logs/
title: View and download pipeline logs \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:21.830592+00:00
---

# View and download pipeline logs  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/view-and-download-pipeline-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  View and download pipeline logs Stay organized with collections  Save and categorize content based on your preferences. 

This page explains pipeline logging in Cloud Data Fusion.

For each data pipeline run, Cloud Data Fusion generates logs to help you monitor data pipeline runs and debug issues. As soon as a pipeline run begins, you can view the logs and filter them by log level.

You can access the logs in the Cloud Data Fusion Studio on the **Preview** page and the **Pipeline details** page. To monitor the progress of a pipeline, click **Logs** while the pipeline is running.

## Filter logs by level

When viewing the pipeline log messages, you can filter them by type, or _log level_ :

  * Error
  * Warning
  * Informational
  * Debug
  * Trace



To set the log level, go to the Cloud Data Fusion Studio's **Preview** page or **Pipeline details** page, and click **Logs** > **Level**. Select the types of messages you want to appear in the log.

## View basic or advanced logs

For each pipeline run, you can view _basic_ or _advanced_ logs. Basic logs include messages about the stages of the pipeline. Advanced logs include all basic log messages, and information about cluster health and the execution engine.

To view advanced logs during a pipeline preview or run, go to the Cloud Data Fusion Studio's **Preview** page or **Pipeline details** page, and click **Logs** > **View advanced logs**.

To return to viewing basic logs, click **Hide Advanced Logs**.

## View the most recent log messages

If you have a pipeline run with a large number of messages, you can go to the bottom of the page for the latest messages. Go to the Cloud Data Fusion Studio's **Preview** page or **Pipeline details** page, and click **Logs** > **Scroll**.

## Downloading logs

For debugging issues, after a pipeline run completes, you can download a log file that includes all of the advanced log and stack trace messages.

  * To download the log file, go to the Cloud Data Fusion Studio's **Preview** page or **Pipeline details** page, and click **Logs** > **Download all**.

  * To view the raw log as plain text in a new browser tab, click **Download all** > **View raw logs**.




## What's next

  * Learn more about [orchestrating pipelines](https://docs.cloud.google.com/data-fusion/docs/concepts/orchestrate-pipelines).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
