---
url: https://docs.cloud.google.com/memorystore/docs/cluster/manage-persistence/
title: Manage persistence \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:12.339510+00:00
---

# Manage persistence  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/manage-persistence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Manage persistence Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to perform common tasks for AOF and RDB persistence.

For more information about persistence, see [Persistence overview](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview).

## RDB persistence tasks

This section gives instructions for common RDB persistence tasks.

### Create an instance that uses RDB persistence

### Console

  1. In the **Data persistence strategy** section, select the **Redis Database (RDB)** option when [Creating an instance](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances).

  2. Select a snapshot interval from the **Snapshot interval** menu.

  3. Select a start time from the **Start time (local time)** menu.




### gcloud

To create an instance that uses RDB persistence, run the `create` command:
    
    
    gcloud redis clusters create instance-id \
      --region=region-id \
      --network=network \
      --replica-count=replica-count \
      --node-type=node-type \
      --shard-count=shard-count \
      --persistence-mode=rdb \
      --rdb-snapshot-period=snapshot-interval \
      --rdb-snapshot-start-time=time
    

Replace the following:

  * instance-id is the ID of the Memorystore for Redis Cluster instance you're creating. Your instance ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.

  * region-id is the region where you want the instance placed.

  * network is the network used to create your instance. It must use the format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID used here must match the network ID used by the service connection policy. Otherwise, the `create` operation fails.

  * replica-count is the number of replicas (per shard). Accepted values are `0`-`5`.

  * node-type is the [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) for the cluster.

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  * shard-count determines the number of shards in your instance. Shard count determines the total memory capacity for storing cluster data. For more information about cluster specification, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

  * snapshot-interval is your chosen interval. Accepted values are `1h`, `6h`, `12h`, and `24h`. The default value is `24h`.

  * time is the start time of your RDB snapshot in the ISO 1801 format. For example: `2024-04-08T03:00:00Z`. If you don't choose a start time when creating an instance that uses RDB persistence, the first snapshot is taken immediately.




### Enable RDB persistence for an existing instance

**Note:** If you enable or disable persistence for an existing instance, then the instance might need to perform [maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance).

### Console

  1. Go to the **Memorystore for Redis Cluster** page in the Google Cloud console.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click your instance ID.

  3. In the **Configurations** section, click the pencil icon next to **Persistence**.

  4. Select the **Redis Database (RDB)** option.

  5. Select a snapshot interval from the **Snapshot interval** menu.

  6. Select a start time from the **Start time (local time)** menu.

  7. Click the **Update Cluster** button.




### gcloud

To enable RDB persistence for an existing instance, run the `update` command:
    
    
    gcloud redis clusters update instance-id \
      --region=region-id \
      --persistence-mode=rdb \
      --rdb-snapshot-period=snapshot-interval \
      --rdb-snapshot-start-time=time
    

Replace the following:

  * instance-id is the ID of the Memorystore for Redis Cluster instance you're creating. Your instance ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.

  * region-id is the region where you want the instance placed.

  * snapshot-interval is your chosen interval. Accepted values are `1h`, `6h`, `12h`, and `24h`. The default value is `24h`.

  * time is the start time of your RDB snapshot in the ISO 1801 format. For example: `2024-04-08T03:00:00Z`. If you don't choose a start time when enabling RDB persistence on an existing instance, the first snapshot is taken immediately.




### Adjust RDB snapshot interval

###  Console

  1. Go to the **Memorystore for Redis Cluster** page in the Google Cloud console.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click your instance ID.

  3. In the **Configurations** section, click the pencil icon next to **Persistence**.

  4. Select your chosen snapshot interval from the **Snapshot interval** menu.

  5. Click the **Update Cluster** button.




### gcloud

To adjust the RDB snapshot interval, run the `update` command:
    
    
    gcloud redis clusters update instance-id \
      --region=region-id \
      --rdb-snapshot-period=snapshot-interval
    

Replace the following:

  * snapshot-interval is your chosen interval. Accepted values are `1h`, `6h`, `12h`, and `24h`. The default value is `24h`.

  * time is your chosen start time in the ISO 1801 format. For example: `2024-04-08T03:00:00Z`.




### Adjust the RDB snapshot start time

###  Console

  1. Go to the **Memorystore for Redis Cluster** page in the Google Cloud console.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click your instance ID.

  3. In the **Configurations** section, click the pencil icon next to **Persistence**.

  4. Select your chosen start time from the **Start time (local time)** menu.

  5. Click the **Update Cluster** button.




### gcloud

To adjust the RDB snapshot start time, run the `update` command. Changing the start time also changes the snapshot alignment time. For example, if you change the start time from 6:00 AM to 6:30 AM, with a snapshot frequency of `1h`, future snapshots align at 7:30 AM, 8:30 AM, 9:30 AM and every hour after that.
    
    
    gcloud redis clusters update instance-id \
      --region=region-id \
      --rdb-snapshot-start-time=time
    

Replace the following:

  * time is your chosen start time in the ISO 1801 format. For example: `2024-04-08T03:00:00Z`.



### Pause RDB persistence

### gcloud

To pause RDB persistence, you must set the snapshot schedule to a future time. When you want to unpause snapshots, you can re-adjust the time to when you want the next snapshot to occur.

To pause RDB snapshots, run the `update` command:
    
    
    gcloud redis clusters update instance-id \
      --region=region-id \
      --rdb-snapshot-start-time=time
    

Replace the following:

  * time is your chosen start time in the ISO 1801 format. For example: `2024-04-08T03:00:00Z`.

**Note:** Pausing snapshots will result in stale backups and can result in the instance being recovered with stale data. If you need to pause snapshots for a long period of time, consider disabling RDB snapshot instead.

### Disable RDB persistence

###  Console

  1. Go to the **Memorystore for Redis Cluster** page in the Google Cloud console.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click your instance ID.

  3. In the **Configurations** section, click the pencil icon next to **Persistence**.

  4. Select the **No persistence** option.

  5. Click the **Update Cluster** button.




### gcloud

To disable RDB persistence, run the `update` command:
    
    
    gcloud redis clusters update instance-id \
      --region=region-id \
      --persistence-mode=disabled
    

**Note:** Disabling persistence disables both backup and restore. Nodes will not load from older snapshots created before persistence was disabled.

### Monitor RDB persistence

You can use [Cloud Monitoring](https://docs.cloud.google.com/memorystore/docs/cluster/monitor-instances) to view metrics for RDB persistence.

For a list of available metrics for RDB persistence, see [persistence metrics](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#persistence_metrics).

## AOF persistence tasks

This section gives instructions for common AOF persistence tasks.

### Create an instance that uses AOF persistence

### Console

  1. In the **Data persistence strategy** section, select the **Append Only File (AOF)** option when [Creating an instance](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances).

  2. Select a sync setting from the **AOF Fsync mode** menu.




### gcloud

To create an instance that uses AOF persistence, run the `create` command:
    
    
    gcloud redis clusters create instance-id \
      --region=region-id \
      --network=network \
      --replica-count=replica-count \
      --node-type=node-type \
      --shard-count=shard-count \
      --persistence-mode=aof \
      --aof-append-fsync=fsync-frequency
    

Replace the following:

  * instance-id is the ID of the Memorystore for Redis Cluster instance you're creating. Your instance ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.

  * region-id is the region where you want the instance placed.

  * network is the network used to create your instance. It must use the format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID used here must match the network ID used by the service connection policy. Otherwise, the `create` operation fails.

  * replica-count is the number of replicas (per shard). Accepted values are `0`-`5`.

  * node-type is the [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) for the cluster.

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  * shard-count determines the number of shards in your instance. Shard count determines the total memory capacity for storing cluster data. For more information about cluster specification, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

  * fsync-frequency is your [sync setting](https://docs.cloud.google.com/memorystore/docs/cluster/about-aof-persistence#sync_setting). Accepted values are `always`, `everysec`, and `no`. `everysec` is the default for this parameter.




### Enable AOF persistence for an existing instance

**Note:** If you enable or disable persistence for an existing instance, then the instance might need to perform [maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance).

### Console

  1. Go to the **Memorystore for Redis Cluster** page in the Google Cloud console.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click your instance ID.

  3. In the **Configurations** section, click the pencil icon next to **Persistence**.

  4. Select the **Append Only File (AOF)** option.

  5. Select a sync setting from the **AOF Fsync mode** menu.

  6. Click the **Update Cluster** button.




### gcloud

To enable AOF persistence on an instance, run the `update` command:
    
    
    gcloud redis clusters update instance-id \
      --region=region-id \
      --persistence-mode=aof \
      --aof-append-fsync=fsync-frequency
    

Replace the following:

  * fsync-frequency is your [sync setting](https://docs.cloud.google.com/memorystore/docs/cluster/about-aof-persistence#sync_setting). Accepted values are `always`, `everysec`, and `no`. `everysec` is the default for this parameter.



### Adjust the AOF sync setting for your instance

### Console

  1. Go to the **Memorystore for Redis Cluster** page in the Google Cloud console.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click your instance ID.

  3. In the **Configurations** section, click the pencil icon next to **Persistence**.

  4. Select your chosen sync setting from the **AOF fsync mode** menu.

  5. Click the **Update Cluster** button.




### gcloud

To adjust the sync setting for an instance that uses AOF persistence, run the `update` command:
    
    
    gcloud redis clusters update instance-id \
      --region=region-id \
      --aof-append-fsync=fsync-frequency
    

Replace the following:

  * fsync-frequency is your [sync setting](https://docs.cloud.google.com/memorystore/docs/cluster/about-aof-persistence#sync_setting). Accepted values are `always`, `everysec`, and `no`. `everysec` is the default for this parameter.



### Disable AOF persistence

### Console

  1. Go to the **Memorystore for Redis Cluster** page in the Google Cloud console.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click your instance ID.

  3. In the **Configurations** section, click the pencil icon next to **Persistence**.

  4. Select the **No persistence** option.

  5. Click the **Update Cluster** button.




### gcloud

To disable AOF persistence, run the `update` command:
    
    
    gcloud redis clusters update instance-id \
      --region=region-id \
      --persistence-mode=disabled
    

**Note:** Disabling persistence disables both backup and restore. Nodes will not load from older snapshots created before disable.

### Monitor AOF persistence

You can use [Cloud Monitoring](https://docs.cloud.google.com/memorystore/docs/cluster/monitor-instances) to view metrics for AOF persistence.

For a list of available metrics for AOF persistence, see [persistence metrics](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#persistence_metrics).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
