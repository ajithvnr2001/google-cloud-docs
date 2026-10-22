---
url: https://docs.cloud.google.com/memorystore/docs/redis/manage-rdb-snapshots/
title: Manage RDB snapshots \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:39.646823+00:00
---

# Manage RDB snapshots  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/manage-rdb-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Manage RDB snapshots Stay organized with collections  Save and categorize content based on your preferences. 

The page explains how to perform common tasks for the RDB snapshots feature. For details on RDB snapshots feature, refer to [RDB snapshots overview](https://docs.cloud.google.com/memorystore/docs/redis/rdb-snapshots).

**Note:** During the Preview stage of the RDB Snapshots feature you cannot enable RDB Snapshots for existing Redis instances. You can only enable snapshots when creating a new Redis instance.

## Creating an instance that uses RDB snapshots

### Console

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Follow the instructions at [Create a Redis instance on a VPC network](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances#create_a_redis_instance_on_a_vpc_network), but return to these instructions when you reach the **Configuration** section.

  3. Expand the node next to this section.

  4. In the **Snapshots** pane, the **Schedule Redis Database (RDB) snapshot** checkbox is selected by default. This setting lets you establish a baseline level of data protection. Memorystore for Redis automatically takes RDB snapshots at a specified interval and recovers data from the last available RDB snapshot if the instance restarts. You can configure your snapshot schedule or opt out:

     1. From the **Start time** menu, select the time that Memorystore for Redis begins taking the snapshot.

Optional: If you want to take a snapshot as soon as the instance is created, then select **Immediately** from the menu.

     2. From the **Snapshot interval** menu, select the scheduled frequency at which Memorystore for Redis automatically saves a snapshot of your instance's data to disk.

**Important** : We recommend that you select a start time and interval that prevents Memorystore for Redis from taking snapshots during peak usage.
     3. Optional: If you don't want to use RDB snapshots, then clear the **Schedule Redis Database (RDB) snapshot** checkbox.

**Important** : We recommend that you don't clear this checkbox because scheduling RDB snapshots establishes a critical baseline of data protection. For Standard Tier instances, this provides an additional layer of protection beyond replication and automatic failover.
  5. Return to the [Create a Redis instance on a VPC network](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances#create_a_redis_instance_on_a_vpc_network) instructions for additional guidance on other Memorystore configurations, and click the **Create** button.




### gcloud

To enable RDB snapshots on an instance, enter the following command replacing variables with appropriate values:
    
    
    gcloud redis instances create instance-id --size=size --persistence-mode=rdb --rdb-snapshot-period=snapshot-interval --rdb-snapshot-start-time=time --region=region-id
    

Where:

  * snapshot-interval is your desired interval. Accepted values are: `1h`, `6h`, `12h`, and `24h`.
  * time is your desired start time in the ISO 1801 format. For example: `2021-01-02T03:00:00Z`.



## Enabling snapshots on an existing instance

### Console

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click the ID of the instance you want to add RDB snapshots to.

  3. Find the _Snapshots_ section.

  4. Select **Schedule Redis Database (RDB) snapshot**.

     1. Choose a start time.

     2. Choose a snapshot interval.

  5. Click the **Save** button.




### gcloud

Run the following command, replacing variables with appropriate values:
    
    
    gcloud redis instances update instance_id --region=region --persistence-mode=rdb --rdb-snapshot-period=snapshot-interval --rdb-snapshot-start-time=time
    

Where:

  * snapshot-interval is your desired interval. Accepted values are `1h`, `6h`, `12h`, and `24h`.
  * time is your desired start time in the ISO 1801 format. For example: `2021-01-02T03:00:00Z`.



## Adjusting snapshot schedule

### gcloud

To adjust the schedule of RDB snapshots, enter the following command replacing variables with appropriate values:
    
    
    gcloud redis instances update instance-id --rdb-snapshot-start-time=time --region=region
    

Where:

  * time is your desired start time in the ISO 1801 format. For example: `2021-01-02T03:00:00Z`.



## Adjusting snapshot interval

### Console

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click the **Instance ID** of the instance you'd like to edit.

  3. Click the **Edit** button

  4. Find the **Snapshots** section.

  5. Use the **Snapshot Interval** dropdown to select your desired interval.

  6. Click the **Save** button.




### gcloud

To change the snapshot interval, enter the following command replacing variables with appropriate values:
    
    
    gcloud redis instances update instance-id --rdb-snapshot-period=snapshot-interval
    --region=region
    

Where:

  * snapshot-interval is your desired interval. Acceptable values are: `1h`, `6h`, `12h`, and `24h`.



## Pausing snapshots

### gcloud

To pause snapshots, you must to set the snapshot schedule to a future time. When you want to unpause snapshots, you can re-adjust the time to when you want the next snapshot to occur. For example, to pause snapshots, enter the following command replacing variables with appropriate values:
    
    
    gcloud redis instances update instance-id --rdb-snapshot-start-time=2022-06-10T03:00:00Z
    --region=region
    

**Note:** Pausing snapshots will result in stale backups and can result in the instance being recovered with stale data. If you need to pause snapshots for a long period of time, consider disabling RDB snapshot instead.

## Disabling RDB snapshots

### Console

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click the **Instance ID** of the instance you'd like to edit.

  3. Click the **Edit** button

  4. Unselect **Schedule Redis Database (RDB) snapshot**.

**Note:** This action stops ongoing snapshots and deletes existing snapshots.
  5. Click the **Save** button.




### gcloud

To disable RDB snapshots for a Redis instance, enter the following command replacing variables with appropriate values:
    
    
    gcloud redis instances update instance-id --persistence-mode=disabled --region=region
    

**Note:** Running this command stops ongoing snapshots and deletes existing snapshots.

## Monitoring RDB snapshots

### Console

The **Instance details** page for Redis instance provides the following RDB snapshots metrics:

  * Frequency
  * Next snapshot
  * Last snapshot status
  * Time since last snapshot
  * Time of last restore



To view these details:

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click the **Instance ID** of your instance.

  3. View the snapshot information under the **RDB Snapshots** section.




### Cloud Monitoring

You can use [Cloud Monitoring](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances) to view metrics for RDB snapshots.

For a list of available metrics for RDB snapshots, see [RDB snapshots metrics](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-metrics#rdb_snapshots_metrics).

## What's next

  * See the overview of [RDB Snapshots](https://docs.cloud.google.com/memorystore/docs/redis/rdb-snapshots) for Memorystore.
  * Learn more about [importing and exporting](https://docs.cloud.google.com/memorystore/docs/redis/import-export-overview) data.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
