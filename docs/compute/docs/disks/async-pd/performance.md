---
url: https://docs.cloud.google.com/compute/docs/disks/async-pd/performance/
title: Review Asynchronous Replication performance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:37.977999+00:00
---

# Review Asynchronous Replication performance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/async-pd/performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Review Asynchronous Replication performance Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view performance metrics for Asynchronous Replication.

To learn more about Asynchronous Replication, see [About Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#performance).

## Metrics

You can view the following Asynchronous Replication metrics in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview):

Metric | Description  
---|---  
**Async replication sent bytes count**   
`(disk/async_replication/sent_bytes_count)`  
| The delta number of bytes sent through the cross-region network.  
**Async replication time since last replication**   
`(disk/async_replication/time_since_last_replication)`  
| The number of seconds since the last replication was done, also known as the recovery point objective (RPO).  
  
## Monitor sent byte counts

Use the **Async replication sent bytes count** metric to graph the average number of byte sent, sampled every minute. The number of sent bytes represents the data your workload writes to block storage, which affects the speed of replication.

  1. In the Google Cloud console, go to the **Cloud Monitoring > Metrics Explorer** page.

[Go to the Metrics Explorer page](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. In the **Select a metric** section, click the **Metric** menu.

  3. Select **Disk** (`disk`).

  4. Select the **Disk** active metric category list, and then select **Async replication sent bytes count** (`disk/async_replication/sent_bytes_count`).

  5. Click **Apply**.

  6. In the **Transform** menu, select one of the following:

     * To view the total number of sent bytes, select **None**.
     * To view the number of bytes sent per second, select **Rate**.
  7. In the **Filters** section, do the following:

     1. Click **Add filter**.
     2. Click inside the **Label** box to view the list of available labels. Under the heading **Resource labels** , select **project_id**. Leave the **Comparison** value set to `= (equals)`. In the **Value** field, type or select your project ID. Click **Done**.
     3. Click **Add filter**.
     4. In the **Label** box, select **disk_id**. Leave the **Comparison** value set to `= (equals)`. In the **Value** field, type or select the ID of the primary disk that is replicating.
     5. Click **Done**.
  8. Click **More options**.

  9. In the **Alignment function** menu select an alignment function. The **Mean** alignment function shows the average number of bytes sent per minute, while the **Max** alignment function shows the highest number of bytes sent per minute.

  10. In the **Min alignment period** menu, select an alignment period. The alignment period must be at least one minute.




## Monitor RPO

Use the **Async replication time since last replication** metric to graph the number of seconds since the last replication was done (RPO).

  1. In the Google Cloud console, go to the **Cloud Monitoring > Metrics Explorer** page.

[Go to the Metrics Explorer page](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. On the **Metrics Explorer** page, click **Add query**.

  3. In the **Select a metric** section, click the **Metric** menu.

  4. Select **Disk** (`disk`).

  5. Select the **Disk** active metric category list, and then select **Async replication time since last replication** (`disk/async_replication/time_since_last_replication`).

  6. Click **Apply**.

  7. In the **Filters** section, add filters for your project ID and disk ID:

     1. Click **Add filter**.
     2. Click inside the **Label** box to view the list of available labels. Under the heading **Resource labels** , select **project_id**. Leave the **Comparison** value set to `= (equals)`. In the **Value** field, type or select your project ID. Click **Done**.
     3. Click **Add filter**.
     4. In the **Label** box, select **disk_id**. Leave the **Comparison** value set to `= (equals)`. In the **Value** field, type or select the ID of the primary disk that is replicating.
     5. Click **Done**.
  8. Click **More options**.

  9. In the **Alignment function** menu, select an alignment function. The **Mean** alignment function shows the average number of seconds since the last replication was done , while the **Max** alignment function shows the highest number of seconds since the last replication was done .

  10. In the **Min alignment period** menu, select the select an alignment period. The alignment period must be at least one minute.

  11. Optional: Save the chart.




## What's next

  * Learn how to customize Asynchronous Replication chats with [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).
  * Learn more about [Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
