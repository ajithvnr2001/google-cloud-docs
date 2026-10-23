---
url: https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows/
title: Find and set maintenance windows \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:49.019579+00:00
---

# Find and set maintenance windows  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Find and set maintenance windows Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Redis Cluster updates clusters routinely by performing maintenance on them to ensure that the service is reliable, performant, secure, up-to-date, and has a zero downtime impact. In addition to Memorystore for Redis Cluster performing maintenance on your clusters, you can customize maintenance schedules to align with your application's needs and to minimize disruptions. To customize your maintenance schedules, you can configure maintenance windows for your clusters.

This page provides instructions on how to complete the following tasks for customizing maintenance windows:

  * Create a cluster with maintenance windows
  * Set a preferred window for maintenance
  * Turn on maintenance notifications
  * Find the scheduled maintenance
  * Reschedule maintenance



For an overview of maintenance updates and maintenance windows, see [About maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance).

## Create a cluster with maintenance windows

You can create a cluster in Memorystore for Redis Cluster with maintenance windows by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important:** Before following the steps in this section, complete the steps in the [Before you begin](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances#before-you-begin) and [Set up networking](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances#set-up-networking) sections.

### Console

To create a cluster with maintenance windows, see [Create instances](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances).

### gcloud

To create a cluster with maintenance windows, use the [`gcloud redis clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/create) command:
    
    
    gcloud redis clusters create CLUSTER_ID \
    --project=PROJECT_ID \
    --region=REGION_ID \
    --network=NETWORK \
    --replica-count=REPLICA_COUNT \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT \
    --maintenance-window-day=MAINTENANCE_WINDOW_DAY \
    --maintenance-window-hour=MAINTENANCE_WINDOW_HOUR
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster that you're creating. The cluster ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.

  * PROJECT_ID: the project ID or number of the Google Cloud project where you want to create the cluster.

  * REGION_ID: the region where you want the cluster to be located.

**Note:** You can create clusters only in the [supported regions](https://docs.cloud.google.com/memorystore/docs/cluster/locations#supported_regions) for Memorystore for Redis Cluster.
  * NETWORK: the network that you want to use to create the cluster. It must use this format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The NETWORK_ID that you use here must match the network ID that the service connection policy uses. Otherwise, you can't create the cluster.

  * REPLICA_COUNT: the number of replicas (per shard). Accepted values are `0`-`5`.

  * NODE_TYPE: the [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) for the cluster.

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  * SHARD_COUNT: the number of shards in the cluster. The shard count determines the total memory capacity for storing cluster data. For more information about cluster specifications, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

  * MAINTENANCE_WINDOW_DAY: the day that you want maintenance to occur. Acceptable values are `MONDAY` \- `SUNDAY`.

  * MAINTENANCE_WINDOW_HOUR: the hour of the day (in UTC time) when the maintenance window starts. Acceptable values are `0` \- `23`.




For example:
    
    
    gcloud memorystore redis clusters my-cluster \
    --project=my-project \
    --region=us-central1 \
    --network=projects/my-network-project/global/networks/default \
    --replica-count=2 \
    --node-type=redis-highmem-medium \
    --shard-count=8 \
    --maintenance-window-day=MONDAY \
    --maintenance-window-hour=9
    

By default, when you create a cluster with maintenance windows, [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption) is deactivated and the authorized network is `default`.

## Set a preferred window for maintenance

You can set a maintenance window for a cluster in Memorystore for Redis Cluster by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the cluster for which you want to set a preferred window.

  3. On the **Cluster at a glance** page, scroll until the **Maintenance** card appears.

  4. Next to the **Maintenance window** field, click **Edit** (_edit_).

If a day and time appear next to the field, then you already set the maintenance window for the cluster.

  5. In the **Edit maintenance window** dialog, do the following:

     1. Select **Custom**.
     2. From the **Day** menu, select the day that you want maintenance to occur.
     3. From the **Time** menu, select the hour when you want the maintenance window to start.
     4. Click **Update cluster**.



### gcloud

To set a maintenance window for a cluster, use the [`gcloud redis clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/update) command:
    
    
    gcloud redis clusters update CLUSTER_ID \
    --project=PROJECT_ID \
    --region=REGION_ID \
    --maintenance-window-day=DAY
    --maintenance-window-hour=HOUR
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster.
  * PROJECT_ID: the project ID or number of the Google Cloud project that contains the cluster.
  * REGION_ID: the region where the cluster is located.
  * DAY: the day that you want maintenance to occur. Acceptable values are   
`MONDAY` \- `SUNDAY`.
  * HOUR: the hour of the day (in UTC time) when the maintenance window starts. Acceptable values are `0` \- `23`.



## Turn on maintenance notifications

If you schedule maintenance for a cluster in Memorystore for Redis Cluster, then you can use the Google Cloud console to turn on maintenance notifications for the cluster.

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the cluster for which you want to set a preferred window.

  3. On the **Cluster at a glance** page, scroll until the **Maintenance** card appears.

  4. Click **Edit notification preferences**.

If this link is deactivated, then you haven't scheduled maintenance for the cluster.

  5. Click **Product Notifications**.

  6. From the menu, select your Google Cloud project.

  7. In the row for Memorystore, toggle the email button to **ON**.




A maintenance notification email uses this title: `"Upcoming maintenance for your Cloud Memorystore cluster [your-cluster-name]"`. Each email address that needs to receive notifications must opt in separately.

You set maintenance notifications at the project level rather than on clusters. Memorystore for Redis Cluster sends notifications to the email address associated with your Google Account. You can't configure a custom email alias (for example, a team email alias).

## Find the scheduled maintenance

If you schedule maintenance for a cluster in Memorystore for Redis Cluster, then you can view the maintenance by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the cluster for which you want to find the scheduled maintenance.

  3. On the **Cluster at a glance** page, scroll until the **Maintenance** card appears.

Next to the **Maintenance window** field, the day and time of the scheduled maintenance appear.




### gcloud

To find the scheduled maintenance for a cluster, use the [`gcloud redis clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/describe) command.
    
    
    gcloud redis clusters describe CLUSTER_ID \
    --project=PROJECT_ID \
    --region=REGION_ID
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster
  * PROJECT_ID: the project ID or number of the Google Cloud project that contains the cluster
  * REGION_ID: the region where the cluster is located



The output for scheduled maintenance is as follows:
    
    
    maintenancePolicy:
    createTime: 'CREATE_DATE_AND_TIME_STAMP'
    updateTime: 'UPDATE_DATE_AND_TIME_STAMP'
    maintenanceWindow:
    - day: DAY
      duration: 60 minutes
      hour: HOUR
    maintenanceSchedule:
     endTime: 'END_DATE_AND_TIME_STAMP'
     startTime: 'START_DATE_AND_TIME_STAMP'
    

Where:

  * `maintenancePolicy` displays information about the creation time of the preferred maintenance policy and the last time the policy is updated. 
    * `CREATE_DATE_AND_TIME_STAMP` is when the maintenance policy is first created.
    * `UPDATE_DATE_AND_TIME_STAMP` is when the maintenance policy is last updated.
  * `maintenanceWindow` displays information about the maintenance window for the cluster. 
    * `DAY` is the day of the week when maintenance occurs.
    * `HOUR` is the hour (in UTC time) when maintenance begins.
  * `maintenanceSchedule` displays information about the scheduled maintenance for the cluster. 
    * `END_DATE_AND_TIME_STAMP` indicates when a scheduled maintenance update ends for the cluster.
    * `START_DATE_AND_TIME_STAMP` indicates when a scheduled maintenance update begins for the cluster.



## Reschedule maintenance

You can use either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to reschedule maintenance for a cluster in Memorystore for Redis Cluster. As a result, you can defer a maintenance update for up to two weeks from when the update is scheduled originally for the cluster.

**Caution:** Memorystore for Redis Cluster doesn't support rescheduling maintenance in bulk requests programmatically. We recommend that you limit the batch size to 100 clusters and wait for ample time between requests. Otherwise, you might have failed rescheduling events. For more information, see [Rescheduling maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance#rescheduling_maintenance).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the cluster for which you want to reschedule maintenance.

  3. On the **Cluster at a glance** page, scroll until the **Maintenance** card appears.

  4. Next to the **Upcoming maintenance** field, click **Edit** (_edit_).

If the **No maintenance scheduled right now** status appears next to this field, then maintenance isn't scheduled for the cluster.

  5. In the **Reschedule upcoming maintenance** dialog, do the following:

     1. From the **Choose a new time** menu, select **Specific time**.
     2. From the **Date** field, click **Calendar** (_date_range_), and then select the date that you want maintenance to occur.
     3. From the **Time** menu, designate a specific time for the update. This time must be no more than 14 days from the time of the original maintenance window.
     4. Click **Reschedule**.

You can also use the **Reschedule upcoming maintenance** dialog to have Memorystore for Redis Cluster perform maintenance on the cluster immediately. From this dialog, select **Update now** from the **Choose a new time** menu, and then click **Update now**.




### gcloud

To reschedule maintenance for a cluster, use the [`gcloud redis clusters reschedule-maintenance`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/reschedule-maintenance) command.
    
    
    gcloud redis clusters reschedule-maintenance CLUSTER_ID \
    --project=PROJECT_ID \
    --region=REGION_ID \
    --reschedule-type=RESCHEDULE_TYPE [--schedule-time=RESHEDULE_TIME]
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster.
  * PROJECT_ID: the project ID or number of the Google Cloud project that contains the cluster.
  * REGION_ID: the region where the cluster is located.
  * RESCHEDULE_TYPE: the type of rescheduled update. Available values are:

    * `IMMEDIATE`: start the maintenance update immediately.
    * `SPECIFIC_TIME`: designate a specific time for the update. This time must be no more than 14 days from the time of the original maintenance window.
  * RESCHEDULE_TIME: the date and time when Memorystore for Redis Cluster reschedules the maintenance update.

**Note:** To specify a value for the RESCHEDULE_TIME parameter, you must set the RESCHEDULE_TYPE parameter to `SPECIFIC_TIME`. This value uses the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) standard (for example, `2025-02-16T16:56:00.000Z`). The time is set in UTC time.



## What's next

  * View the [permissions](https://docs.cloud.google.com/memorystore/docs/cluster/access-control#permissions_and_their_roles) that you need to manage maintenance windows for a cluster in Memorystore for Redis Cluster.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
