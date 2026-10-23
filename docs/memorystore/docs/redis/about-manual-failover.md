---
url: https://docs.cloud.google.com/memorystore/docs/redis/about-manual-failover/
title: About manual failover \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:12.909951+00:00
---

# About manual failover  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/about-manual-failover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  About manual failover Stay organized with collections  Save and categorize content based on your preferences. 

This page gives an overview of **manual failover** for Memorystore for Redis. To learn how to perform a failover, see [Initiating a manual failover](https://docs.cloud.google.com/memorystore/docs/redis/initiating-manual-failover).

## What is a manual failover?

A standard tier Memorystore for Redis instance uses a replica node to back up the primary node. A normal failover occurs when the primary node becomes unhealthy, causing the replica to be designated as the new primary. A manual failover differs from a normal failover because you initiate it yourself. For more information on how Memorystore for Redis replication works, see [High availability](https://docs.cloud.google.com/memorystore/docs/redis/high-availability).

During a manual failover for Standard Tier instances, data is preserved. When you perform a manual failover, the instance undergoes a short connection reset of a couple of minutes or less. We recommend that applications incorporate retry logic in the code so that they can reconnect to the instance. The IP address and connection string remain the same.

To provide an additional layer of data protection beyond replication and failovers, RDB snapshots are enabled by default when you create a Memorystore for Redis instance using the Google Cloud console.

## Why initiate a manual failover?

Initiating a manual failover lets you test how your application responds to a failover. This knowledge can ensure a smoother failover process if an unexpected failover occurs later on.

## Optional data protection mode

The two available data protection modes are:

  * `limited-data-loss` mode (default).
  * `force-data-loss` mode.



To set the data protection mode, use one of the following commands:
    
    
    gcloud redis instances failover INSTANCE_NAME --data-protection-mode=limited-data-loss
    

or
    
    
    gcloud redis instances failover INSTANCE_NAME --data-protection-mode=force-data-loss
    

## How data protection modes work

The `limited-data-loss` mode minimizes data loss by verifying that the difference in data between the primary and replica is below 30 MB before initiating the failover. The offset on the primary is incremented for each byte of data that must be synchronized to its replicas. In the `limited-data-loss` mode, the failover will abort if the greatest offset delta between the primary and each replica is 30MB or greater. If you can tolerate more data loss and want to aggressively execute the failover, try setting the data protection mode to `force-data-loss`.

The `force-data-loss` mode employs a chain of failover strategies to aggressively execute the failover. It does not check the offset delta between the primary and replicas before initiating the failover; you can potentially lose more than 30MB of data changes.

## Bytes pending replication metric

The **bytes pending replication** metric tells you how many remaining bytes the replica needs to copy before the primary is fully backed up. You may observe an increase in bytes pending as the primary replicates to the replica during a failover. If the failover is triggered by hardware error, you may observe empty in bytes pending replication as the offset value could not be obtained until the new replica repaired from host error.

You can access this metric in the Google Cloud console on the instance details page. To view the instance details page, click the instance id in your project's [instances list](http://console.cloud.google.com/memorystore/redis/instances?memorystore=true) page.

Alternatively, access the Metrics Explorer for your project, and search for the **redis.googlapis.com/replication/offset_diff** metric.

## When to run a manual failover

Manual failovers using the default `limited-data-loss` protection mode only succeed if the **bytes pending replication** metric is less than 30MB. If you want to run a manual failover with **bytes pending replication** higher than 30MB, use the `force-data-loss` protection mode.

If you are trying to preserve as much data as possible, temporarily stop your application from writing to the Redis instance, and wait to run your manual failover until the **bytes pending replication** metric is as low as you deem acceptable.

## Potential issues blocking a manual failover

  * Running a manual failover on a Basic Tier instance does not work because Basic Tier instances do not have replicas to which the primary can failover.

  * If your Redis instance is unhealthy, then a limited-data-loss manual failover operation fails because it is blocked for data-loss minimization.

  * If you are running a Lua script that is executing indefinitely, then you must use `force-data-loss` to initiate a failover. In this situation a limited-data-loss failover operation will not complete successfully.

  * If your instance has incomplete operations pending, such as scaling or updating, the manual failover operation is blocked. You must wait until your instance is in the `READY` state to run a manual failover.




## Client application connection

When your primary node fails over to the replica, existing connections to Memorystore for Redis are dropped. However, on reconnect, your application is automatically redirected to the new primary node using the same connection string or IP address.

## Verifying a manual failover

You can verify the success of a manual failover operation with the Google Cloud console or `gcloud`.

### Google Cloud console verification

Before you start a manual failover, go to the Memorystore for Redis [instances list page](http://console.cloud.google.com/memorystore/instances?memorystore=true), and click the name of your instance.

Then, in the **Configuration** tab, next to **Primary Location** , view which zone your primary node is in. Make a note of the zone. Check this page again when you complete your manual failover to confirm that the primary node switched zones.

### Cloud Monitoring verification

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Node role` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Cloud Memorystore Redis**.
     2. In the **Active metric categories** menu, select **replication**.
     3. In the **Active metrics** menu, select **Node role**. 
     4. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



The Cloud Monitoring chart represents the primary and replica nodes with two lines. When a node's line has a value of zero on the chart, it is the replica node. When a node's line has a value of one on the chart, it is the primary node. The chart represents a failover by showing how the lines switch from one to zero, and zero to one, respectively.

### `gcloud` verification

Before you initiate a manual failover, use the following command to check which zone your primary node is in:
    
    
    gcloud redis instances describe [INSTANCE_ID] --region=[REGION]

Your primary node is in the zone labeled `currentLocationId`. Make a note of the zone.

After you complete a manual failover, you can confirm that your primary node switched to a new zone by running the `gcloud redis instances describe` command again and checking that the `currentLocationId` changed zones.

Additionally, the `locationId` label tells you the zone in which you originally provisioned your primary node. The `alternativeLocationId` label tells you the zone in which system originally provisioned your replica node. Each time a failover occurs the primary and replica switch between these two zones. However, the zones associated with `locationId` and `alternativeLocationId` do not change.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
