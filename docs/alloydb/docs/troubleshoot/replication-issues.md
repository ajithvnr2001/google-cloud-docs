---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/replication-issues/
title: Troubleshoot replication issues \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:09.725687+00:00
---

# Troubleshoot replication issues  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/replication-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Troubleshoot replication issues Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB has an architecture that separates compute and storage, allowing each to scale independently. While the primary and read pool instances share the same underlying storage, replication is still a crucial process for maintaining data consistency and freshness across the read replicas. In an AlloyDB cluster, writes are performed on the primary instance and then recorded in the Write-Ahead Log (WAL). These changes are then replicated to the read pool nodes. Understanding the two main steps of this replication process is key to troubleshooting any issues:

  * WAL flush: the Write-Ahead Log (WAL), which contains the changes to the database, is sent from the primary to the replica. The replica then immediately persists the WAL to disk.
  * WAL apply (or replay): the persisted WAL is replayed on the replica, meaning the changes are applied to the replica's caches.



Delays in either of these steps contribute to what is known as replication lag. However, this term might be ambiguous. To be more precise, we can break down replication lag into the following two components:

  * Flush or network lag: this is the delay in the WAL flush step. It's the time it takes for the WAL to be sent from the primary and persisted on the replica.
  * Replay lag: this is the delay in the WAL apply step. It's the time it takes for the replica to apply the changes from the WAL.



Whether you must be more concerned about flush lag or replay lag depends on your use case:

  * If you are concerned about data loss, for example, with secondary clusters, then you must pay close attention to flush lag. If the WAL isn't yet persisted on the replica and the primary crashes, the changes are lost from the perspective of the replica.
  * If you are concerned about the freshness of data on your read replicas, then you must pay close attention to both flush lag and replay lag. A delay in either step — whether in transmitting the WAL or applying it — results in stale data on your read replicas.



## Check for replication lag

You can monitor the replication lag of your read pool instances in the Google Cloud console. For more information, see [Monitor instances](https://docs.cloud.google.com/alloydb/docs/monitor-instance). You can also monitor your read pool replication lag and receive alerts at a specified threshold using [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

## Common causes of replication lag

Here are some common causes of replication lag and how to address them.

### Resource contention

Replication might also be slowed down by contention for system resources, such as CPU and memory.

  * CPU and memory pressure: a heavy read workload on a read pool instance can compete with the replication process for CPU and memory resources. You can check the CPU and memory usage of your instances in the Google Cloud console. If you see high resource utilization, you might need to scale up or scale out your read pool instances.
  * Read pool node size: if your primary instance is much larger than your read pool nodes, it might generate replication logs faster than the read nodes can process them. In such cases, it is recommended to use larger-sized read nodes to give the replicas more resources.



### Replication conflicts

Read queries can sometimes block the replication process because they hold on to resources that the replication process is waiting for. If a read query holds a lock on a database object that the replay process needs to update, this results in a _lock conflict_. If a query holds a pin on a data buffer that replay needs to modify, this results in a _buffer pin conflict_. In both cases, replay is blocked until the query releases the resource.

You can identify these conflicts by looking for `canceling statement due to conflict with recovery` messages in the `postgres.log` file in the Logs Explorer.

To mitigate replication conflicts, you can do the following:

  * Reduce `max_standby_streaming_delay`: this parameter determines how long the replay process waits before canceling queries that are blocking it. The default value is 30 seconds. Reducing this value can help to reduce replication lag, but it might also cause more read queries to be canceled. You can tune this parameter to find the best balance for your application.

  * Avoid long-running queries: long-running queries on read pools can increase the likelihood of replication conflicts. Consider moving long-running queries to a different read pool where low replication lag is not as critical.

  * Verify `alloydb.promote_cancel_to_terminate` is active: this flag, which is on by default, lets AlloyDB forcefully terminate query backends that are unresponsive to cancellation requests. This can help to prevent unresponsive backends from blocking replication for extended periods.




### Lag-based read query throttling

AlloyDB also gives you the control on whether to enable lag-based throttling of read queries on read nodes using the flag `google_storage.log_replay_throttle_read_transactions`. If the parameter is set to its default value of `on`, then the read queries are throttled by pausing new queries from starting as well as reading new buffers for up to one minute when replication lag exceeds one second. This feature makes a trade-off that improves replication lag by giving replay more resources to catch up faster, at the cost of potentially increasing read query latency. If your application is not sensitive to replication lag, you can prioritize improving read query latency by setting `google_storage.log_replay_throttle_read_transactions` to `off`.

You can monitor the impact of query throttling using the following methods:

  * Logs: search for `Delayed.*due to replica lag` messages in the `postgres.log` file in the Logs Explorer to identify when queries are delayed due to replica lag.

  * Cloud monitoring: use the `alloydb.googleapis.com/instance/postgresql/wait_count` metric to see how many queries have been throttled. To do this, filter the metric by the `wait_event_name` and look for `HighLagThrottle`. To see the total time queries were throttled, you can use the `alloydb.googleapis.com/instance/postgresql/wait_time` metric with the same filter. For more information, see the [System insights metrics reference](https://docs.cloud.google.com/alloydb/docs/reference/system-insights-metrics).

  * Query insights: in the **Query insights** dashboard, the **Active queries** view shows the `HighLagThrottle` wait event in the **Wait event** column when a query is being throttled due to replication lag. For more details, see [Monitor active queries](https://docs.cloud.google.com/alloydb/docs/monitor-active-queries).




### Heavy workload

A sudden increase in the write workload on the primary instance can generate a large amount of replication logs, which can overwhelm the read pool instances and cause replication lag. You can monitor the write traffic on your primary instance in the Google Cloud console.

### Heavy Write-Ahead-Logs volume due to ScaNN index build

Building the ScaNN index may generate large amounts of full-page-writes WAL records. This can cause delay in sending WAL records from your primary instance to read instances. If replication lag corresponds to building the ScaNN index on large numbers of embeddings, you can turn on `wal_compression` on the primary instance to save network and disk IO and reduce replication lag. This may incur a small amount of extra CPU overhead.

`wal_compression` only compresses full-page-writes records and doesn't have effect on most WAL records. Changing this flag doesn't require a restart and has zero downtime.

### Large transactions

Transactions that modify a large number of rows — for example, by deleting multiple tables or large tables — generate exceptionally large `COMMIT` or `ABORT` records in the Write-Ahead Log (WAL). These records can take a significant amount of time to be replayed on the read pool nodes, leading to a temporary increase in replication lag.

To mitigate this, avoid performing very large batch operations, such as deletes, in a single transaction. Instead, break these operations into smaller, more frequent transactions. This reduces the size of individual `COMMIT` and `ABORT` records, allowing the replication stream to remain more fluid and reducing peak replication lag.

## Troubleshoot issues that prevent replication

Before you can have replication lag, you must have a functioning read pool. The following issues might prevent replication from occurring altogether, either by preventing the creation of a read pool or by causing a read replica to crash.

### Read pool instance crashes

In PostgreSQL 14, a long-running transaction on the primary instance that holds a long list of exclusive locks might cause the memory usage of a read replica to grow, which might eventually lead to the read pool instance crashing.

To mitigate this issue, you can terminate the long-running transaction on the primary instance.

## Impact of instance resizing on replication lag

AlloyDB's storage architecture ensures that read pool flush lag is not impacted by instance resizing. However, the same doesn't apply to the replay. The replica's ability to replay depends on the load it has. If you update your instance configuration, for example, by resizing it, depending on the workload, the replica may not have a fully warmed cache when the operation completes. This means that it is slower to replay or process records that it hasn't cached yet. In that case, this might mean that replay lag increases temporarily.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
