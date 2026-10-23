---
url: https://docs.cloud.google.com/memorystore/docs/redis/about-importing-exporting/
title: About importing and exporting data \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:57.075437+00:00
---

# About importing and exporting data  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/about-importing-exporting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  About importing and exporting data Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how imports and exports work in Memorystore for Redis.

The import and export feature uses the native RDB snapshot feature of Redis to import data into or export data out of a Memorystore for Redis instance. The use of the native RDB format prevents lock-in and makes it very easy to move data within Google Cloud or outside of Google Cloud. Import and export uses Cloud Storage buckets to store RDB files.

The behavior of a Memorystore for Redis instance during export is very similar to the `BGSAVE` command in open source Redis. Memorystore for Redis imports by copying your RDB file into your instance's data directory.

For instructions on how to import and export RDB files, see [Importing data to a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/import-data) and [Exporting data from a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/export-data).

## Import feature behavior

  * For optimal performance, you should import from Cloud Storage buckets located in the same region as your Redis instance.

  * Your Redis instance is unavailable during an import operation. Your instance becomes available after the import operation finishes.

  * If an import is successful, the existing data in the instance is overwritten by the data in the RDB file.

  * If an import fails for any reason, the instance is brought online, but the data may be fully flushed. You can retry the import using the same RDB file, or you may use another RDB file to restore data.

  * Your Memorystore for Redis instance can import RDB files from the same Redis version and from a previous Redis version, but it cannot import RDB files from a newer version.

  * An import operation can be cancelled, but you should note that the cancellation results in your instance recovering with a fully flushed cache. This is the case for both Basic Tier and Standard Tier instances.

  * An instance can only import backups from older Redis versions. An instance running Redis 5.0 can import an RDB exported from Redis 4.0, but an instance running Redis 4.0 cannot import an RDB from Redis 5.0.




## Export feature behavior

  * You can read and write data to your Redis instance during an export operation; however, you cannot perform any admin operations like scaling, updating, or configuring your instance.

  * Your instance may experience increased latency during the export.

  * For optimal performance, you should export your RDB backups to Cloud Storage buckets located in the same region as your Redis instance.

  * During an export, the RDB file is saved to a Cloud Storage bucket of your choice.

  * You can cancel an export operation at any time. Cancelling does not impact the data or availability of an instance.

    * Cancelling an export deletes the RDB file being written to the Cloud Storage bucket, and frees up memory used by the `BGSAVE` process.
  * An export can overwrite an existing file with the same name with no extra permissions when using the Google Cloud console. To export over an existing file with `gcloud`, the user account needs the `storage.objects.delete` permission.




## Exporting under high write load

If you run an export during a period of high write-load your instance memory usage can increase up to 2X, causing the export operation to fail. You should perform export operations during periods of low writes. To monitor how much Redis data is stored in your instance you can [create a dashboard to monitor your memory usage](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances#memory-monitoring-dashboard) and monitor the [instance memory usage metrics](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#instance_memory_usage_metrics) with Cloud Monitoring.

Memorystore for Redis export uses the `BGSAVE` feature of Redis to take a snapshot of the data in an instance. When executing `BGSAVE`, Redis forks a new child process to take the snapshot. Redis utilizes [copy-on-write](https://redis.io/topics/persistence) during this process.

This means that the initial fork allocates minimal extra memory, but any pages changed by Redis server write traffic are duplicated. Therefore, under periods of high writes, in the worst case, the memory footprint of Redis doubles, causing the export operation to fail.

## Exporting during a BGSAVE operation

You cannot export while a `BGSAVE` operation is running. Standard Tier Memorystore for Redis instances sometimes run full resynchronization operations, or 'full syncs', to keep the primary and the replica synchronized. A full resynchronization uses the `BGSAVE` command, which prevents Memorystore from performing an export.

To verify if a `BGSAVE` operation is ongoing, view the `redis.googleapis.com/persistence/rdb/bgsave_in_progress` API endpoint with Metrics Explorer.

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the **Metric** element, expand the **Select a metric** menu, and then select a resource type and metric type. For example, to chart the CPU utilization of a virtual machine, do the following: 
     1. (Optional) To reduce the menu's options, enter part of the metric name in the **Filter bar**. For this example, enter `utilization`.
     2. In the **Active resources** menu, select **VM instance**.
     3. In the **Active metric categories** menu, select **Instance**.
     4. In the **Active metrics** menu, select **CPU utilization** and then click **Apply**.
  3. To filter which time series are displayed, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  4. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.




Alternatively, you can use your own command line API tools.

## Required permissions for importing and exporting

A user needs to configure sufficient IAM permissions to import or export RDB files. The simplest permissions setup is to apply the **Cloud Memorystore Redis Admin** and **Storage Admin** IAM roles to the user account. However, this setup might be inappropriate for some user accounts because it gives them permissions to create, edit, or delete resources they shouldn't have access to. For instructions on setting minimally restricted permissions, see [Granting restricted permissions for import and export](https://docs.cloud.google.com/memorystore/docs/redis/import-export-restricted-permissions).

## Duration of imports and exports

The duration of the import or export depends on the instance size and the size of the data set in the instance. Depending on the size, the imports and exports can take anywhere from a few minutes to a few hours.

For example, if you import or export a 10 GB instance with 8 GB of used memory, the operation can take 5 minutes. If you import or export a 120 GB instance with 100 GB of used memory, the operation can take an hour.

## Stopping an import or export

To stop an import or export, refer to the following pages:

  * [Stopping an ongoing import operation](https://docs.cloud.google.com/memorystore/docs/redis/import-data#stop_an_ongoing_import_operation).

  * [Stopping an ongoing export operation](https://docs.cloud.google.com/memorystore/docs/redis/export-data#stop_an_ongoing_export_operation).




## Monitoring progress of the operation

The time estimate for completion is not available while doing import and export. You can check whether the operation is in progress by checking the instance details page. To view the instance details page, click your instance ID on the Memorystore for Redis [instances list](http://console.cloud.google.com/memorystore/redis/instances?memorystore=true) page.

You can also monitor the progress of an import operation by running the following command:
    
    
    gcloud redis instances describe [INSTANCE_ID] --region=[REGION]
    

Where:

  * `[INSTANCE_ID]` is the ID for your Memorystore for Redis instance.
  * `[REGION]` is the region your instance is in.



The command outputs `state: IMPORTING` or `state: READY` as one of the description fields.

## Unsupported Cloud Storage buckets

Requester Pays Cloud Storage buckets are not supported for Memorystore imports and exports.

## Securing your Cloud Storage buckets

You should ensure that your Cloud Storage bucket has the right restrictions to prevent unauthorized access to the Redis RDB backup it contains. Please refer to Cloud Storage [Access Control Options](https://docs.cloud.google.com/storage/docs/access-control) on how to secure your Cloud Storage buckets.

## Ensuring sufficient memory to complete an export

To prevent export from causing memory starvation, you should have 50% free memory in the instance during the export process. This may not be required all the time, depending on your write load, but having 50% free memory ensures that there is enough free space to accommodate copy-on-write overhead, if many pages are touched during the export process.

To understand the current memory usage of your instance, [set up an alert](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances#create-stackdriver-alert) to notify you when your memory usage reaches a customizable threshold. Additionally you should [set up a memory monitoring dashboard](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances#memory-monitoring-dashboard) with Cloud Monitoring. These measures allow you to understand your instances memory usage patterns. Understanding memory usage patterns enables you to size your instance correctly when exporting at regular intervals.

## Exporting and importing to instances with read replicas

For all Redis instances, including read replica enabled instances, data is exported from the primary node.

For read [replica enabled instances](https://docs.cloud.google.com/memorystore/docs/redis/read-replicas), exporting can increase the CPU load and memory footprint on the primary node.

When importing data into a read replica enabled instance, the primary restarts during the import operation, and the instance is unavailable until the new data is fully loaded into the database.

## What's next

  * Follow the guide for [Importing data to a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/import-data).

  * Follow the guide for [Exporting data from a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/export-data).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
