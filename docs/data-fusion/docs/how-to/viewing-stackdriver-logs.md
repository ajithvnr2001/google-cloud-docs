---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/viewing-stackdriver-logs/
title: View advanced pipeline logs in Cloud Logging \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:35.969707+00:00
---

# View advanced pipeline logs in Cloud Logging  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/viewing-stackdriver-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  View advanced pipeline logs in Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable Cloud Logging for your Cloud Data Fusion Managed Service for Apache Spark clusters and access advanced pipeline logs.

## Enable Managed Service for Apache Spark Cloud Logging

To view pipeline and cluster issues in Cloud Logging, enable advanced logs in new or existing Cloud Data Fusion instances. To enable advanced logs in an existing instance, do the following:

  1. In the Google Cloud console, go to the Cloud Data Fusion **Instances** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click the instance name.

  3. In the **Advanced monitoring and logging** section, for **Dataproc Cloud Logging** , click edit **Edit**.

  4. In the **Cloud Logging** window, select the **Enable Cloud Logging** checkbox.

  5. Click **Save**.




## View logs

Every Cloud Data Fusion pipeline run is assigned a unique `RunID`. After you deploy and run your pipeline, find its `RunID`. Then, in Logging, use the `RunID` to view your pipeline logs.

### Get the pipeline's RunID

  1. Go to your instance: 
     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click **List**.
  3. Click the pipeline for which you want to get the Run ID.
  4. Click **Summary**.
  5. In the **Run history** section, click **Table**.
  6. To copy the Run ID, right-click the **RunID** , and click **Copy**.



### View the logs in Logs Explorer

  1. In the Google Cloud console, go to the **Cloud Logging > Logs Explorer** page:

[Go Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **All resources** drop-down, select **Cloud Dataproc Cluster > **`cdap- PIPELINE_NAME-YOUR_RUNID`****.




### Optional: Filter the logs

Use the filter menus to filter your logs. You can filter by various log severity levels or by components such as `datafusion-pipeline-logs`.

### Optional: Download the logs

Click **Download logs**.

For more information, see [downloading log entries](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#download_logs).

## What's next

  * Learn how to [view audit logs](https://docs.cloud.google.com/data-fusion/docs/how-to/audit-logging).
  * Learn how to [view pipeline logs from the Cloud Data Fusion Pipeline Studio](https://docs.cloud.google.com/data-fusion/docs/how-to/view-and-download-pipeline-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
