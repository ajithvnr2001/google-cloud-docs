---
url: https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence/
title: About RDB persistence \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:22.683333+00:00
---

# About RDB persistence  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  About RDB persistence Stay organized with collections  Save and categorize content based on your preferences. 

This page gives an overview of RDB persistence on Memorystore for Valkey.

To learn how to enable, disable, and monitor RDB persistence, see [Manage persistence](https://docs.cloud.google.com/memorystore/docs/valkey/manage-persistence).

For information about best practices for RDB persistence, see [Persistence best practices](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#persistence_best_practices).

The RDB persistence feature protects your data by saving snapshots of your data on durable storage. You choose the frequency of these snapshots by selecting a snapshot interval ranging from a minimum of 1 hour to a maximum of 24 hours. If node failures occur, data is recovered even in cases where failover is not possible.

Nodes with replicas prioritize data recovery from the replica. However, if both the primary and replica fail simultaneously, nodes recover from the most recent snapshot.

  * Shards that are added by horizontally scaling up your instance aren't included in snapshots until the next scheduled snapshot time.
  * If you [enable or disable persistence](https://docs.cloud.google.com/memorystore/docs/valkey/manage-persistence#enable_rdb_persistence_for_an_existing_instance) for an existing instance, then the instance might need to perform [maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance).



RDB persistence adds no additional cost to your instance billing. This feature is ideal for use cases where a small degree of data staleness after recovery is acceptable. Because Memorystore uses snapshots for automated recovery, snapshots aren't available for manual restores. You should also note that only the most recent successful snapshot is retained.

Memorystore for Valkey also supports AOF persistence, but you must choose either the AOF or RDB persistence mode, because both can't be enabled at the same time. For information about choosing between the two persistence modes, see [Persistence overview](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview). For the best possible availability, we recommend using [a highly available instance](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas) in addition to enabling persistence.

## Schedule snapshots

Scheduling snapshots is determined by two settings: the snapshot start time, and the snapshot interval. The intervals you can set are `1h`, `6h`, `12h`, and `24h`. For example, if you set the start time to 4 AM and the interval to one hour, the snapshots start at 4 AM on the day they are enabled, and continue every hour after that.

Snapshot schedules are evaluated in the UTC time zone, therefore local time zones with daylight savings shifts will expereince schedule adjustments. For example, at the beginning and end of DST in the US, the local start times of your snapshot schedule jobs move forward or backward by an hour if your time zone honors DST changes.

### Pause snapshots

You may run into scenarios where you want to temporarily pause taking RDB snapshots for a certain period of time. This could be to ensure there are no performance impacts during critical events or to temporarily disable snapshots to troubleshoot performance issues.

To pause snapshots, you must set the start time to the future. If you do this, the last snapshot is retained and is used in the event of a recovery. To resume snapshots, adjust the snapshot schedule to when you want the next snapshot to occur. To learn more about adjusting snapshot schedules, see [Adjust RDB snapshot interval](https://docs.cloud.google.com/memorystore/docs/valkey/manage-persistence#adjust_rdb_snapshot_interval).

## Recovery behavior

Memorystore for Valkey nodes failover to replicas as the primary recovery mechanism, rather than loading from a snapshot. However, if a node fails and can't recover from a replica, the node recovers from a snapshot.

### Data consistency on recovery

**Important:** An RDB snapshot is a point in time snapshot of node data based on the snapshot interval you set. Your application must be able to tolerate some staleness of data on recovery.

When enabled, RDB persistence makes a best effort to ensure backups are taken on the specified interval. Snapshots can fail for a number of reasons. If the snapshot fails consecutively on multiple intervals, the last available backup can be arbitrarily stale.

The worst case data staleness for a recovery from a snapshot is the sum of the specified interval since the last good snapshot started and the time to save the next snapshot to storage. In the case of a recovery incident, use the [`rdb_last_success_ages`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#persistence_metrics) metric to view the timeframe for data staleness.

### Recovery time

If a node fails and needs to recover data from a snapshot, the node is unavailable during recovery. Recovery time depends on the size of the snapshot.

### Snapshot failures

Any failed snapshot is retried immediately with exponential backoff from 5 to 300 seconds. Consecutive snapshot failures increase data staleness in the event of a recovery.

### Recovery failures

Recovery failures are rare but can happen. If a recovery failure occurs, the node retries repeatedly until it recovers successfully.

## Monitor snapshots

It's important to monitor snapshots and set alerts for failed snapshots. For information about best practices for RDB persistence, see [RDB persistence best practices](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#persistence_best_practices). Failed snapshots can indicate overloaded nodes that may continue to have difficulty recovering from the snapshot.

For a list of metrics available for monitoring snapshots, see [Persistence metrics](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#persistence_metrics).

### Manage a snapshot's performance impact

You can monitor the performance impact that a snapshot has on your Memorystore instance by viewing the metrics available through [Cloud Monitoring](https://docs.cloud.google.com/memorystore/docs/valkey/monitor-instances) such as CPU usage and memory usage.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
