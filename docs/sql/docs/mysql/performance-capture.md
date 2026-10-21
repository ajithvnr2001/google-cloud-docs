---
url: https://docs.cloud.google.com/sql/docs/mysql/performance-capture/
title: Cloud SQL performance capture overview \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:27.737448+00:00
---

# Cloud SQL performance capture overview  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/performance-capture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Cloud SQL performance capture overview Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

Cloud SQL for MySQL performance capture helps you diagnose and resolve complex and transient performance issues in your MySQL database that are caused by evolving system demand. As application workloads scale and the surrounding infrastructure grows more complex, databases are subjected to increasing and unpredictable demands. These external system pressures can cause database slowdowns or stalls.

When your database experiences performance degradation, standard metrics can be insufficient for identifying the root cause in the context of your larger infrastructure. Performance capture solves this issue by capturing detailed, point-in-time snapshots of the database at the moment when a problem is detected. You can use configurable triggers to take system-wide snapshots when transient issues occur. Triggers can also detect long-running transactions, which can be the root causes of performance issues. You can configure triggers to end long-running transactions automatically.

## Example use cases

This section lists example use cases for how you can use performance capture after you enable it for your instance.

Use case | Trigger condition | Diagnosistic insight  
---|---|---  
System-wide slowdown due to undo log accumulation  | History list length  | Identifies when the InnoDB purge process is falling behind due to long-running reads or large data manipulation language (DML) operations. The delay can lead to increased storage pressure and performance degradation.  
Database stall caused by internal engine contention  | Semaphore waits  | Helpful for diagnosing an unresponsive database. This trigger can detect mutex or read-write lock contention within the InnoDB storage engine, such as Adaptive Hash Index (AHI) or buffer pool contention.  
Application- level lock contention or unindexed queries | Transaction lock waits  | Triggers when a high number of transactions are in a `LOCK WAIT` state, pointing to row-level contention or long-running idle transactions.  
Instance overload from complex sorting or aggregation | High CPU utilization  | Captures state during high : container CPU usage, often caused by inefficient queries or massive concurrency spikes.   
Risk of Out-of-Memory (OOM) restarts  | High memory usage  | Helps you diagnose issues like oversized per-thread buffers or memory leaks before they lead to an instance crash.  
Sudden traffic spikes or bottlenecked client apps | Running threads  | A general indicator of instance load, useful for identifying sudden surges in concurrent active connections.  
Stale data on the replica due to heavy write workloads | Seconds behind source  | Monitors replication lag on read replicas to help diagnose delays in syncing data from the primary instance.   
Long-running queries blocking purge  | Long-running transactions  | Identifies transactions that have been open too long and that might be holding critical locks. In addition, you can [end long-running transactions automatically](https://docs.cloud.google.com/sql/docs/mysql/configure-performance-capture#end-transactions).  
  
## How performance data is captured

Performance capture operates as an agent-based service that monitors your instance. When you [enable performance capture](https://docs.cloud.google.com/sql/docs/mysql/configure-performance-capture#enable-performance-capture), your Cloud SQL instance does the following to capture performance data:

  1. The agent probes your instance configuration to read the threshold-based triggers that you've defined. The agent then probes the metrics of your instance at a configurable interval, `probingIntervalSeconds`, which is set to 30 seconds by default.

  2. If a problem is detected and the threshold of a trigger has been exceeded, then the agent continues to compare the instance's live state to your rules. To prevent any false alarms from temporary spikes, the agent triggers a full performance capture. A capture is triggered _only_ if the condition is met during consecutive probes for the configured `probeThreshold`, which defaults to `3`. This consecutive threshold prevents captures due to transient spikes.

For example, the agent might trigger a performance capture if it detects that the number of threads are high for three probes in a row.

If multiple trigger conditions are configured, then Cloud SQL initiates a capture if _any_ of the conditions are met.

  3. When a capture is triggered, performance capture connects to the database and runs a series of diagnostic commands to capture a detailed snapshot.

  4. The captured information is formatted into log entries and sent directly to the project's Cloud Logging for the Cloud SQL instance under a specific log stream named `mysql-performance-capture.log`.




### Cooldown and adaptive backoff periods

To prevent excessive logging and system overhead, performance capture implements a cooldown period after a capture.

#### Standard cooldown

After a successful capture, performance capture starts a **30-minute standard cooldown**. During this time, the agent doesn't trigger new captures even if the instance is in an extended problem state.

#### Adaptive cooldown and backoff

If an instance repeatedly triggers captures for the same violation, then performance capture uses an **adaptive cooldown backoff mechanism**. This mechanism helps limit the logging volume and cost of misconfigured thresholds.

Under this mechanism:

  * The cooldown extends to **24 hours**.
  * Performance capture enters a **sleep mode** , which suspends all trigger checks and diagnostic captures.
  * The instance is limited to a single performance capture per day.



## Performance capture triggers

This section lists the triggers that are available for MySQL performance capture. All triggers listed in the table, except where noted, use the probe configuration values `probingIntervalSeconds` and `probeThreshold` to validate sustained trigger conditions.

**Trigger** **condition** **name** | **API name** | **Description** | **Default** **value** | **Configuration** **range**  
---|---|---|---|---  
High CPU  
utilization  | `cpuUtilizationThresholdPercent` | Triggers a capture when the overall CPU utilization of the database instance consistently exceeds this percentage. This helps detect instance overload, often caused by inefficient queries with massive sorting and aggregation, insufficient indexing, or very high concurrency. To avoid captures on minor spikes, configure the default to be in the higher percentage range for your instance. | `0` (disabled)  | `0`, or   
`10`-`99` (%)   
High memory  
usage  | `memoryUsageThresholdPercent` | Triggers a capture when the memory usage of the database container consistently exceeds this percentage of the instance's allocated memory. This trigger can help diagnose potential out-of-memory problems, memory leaks, or inefficient memory configuration. To avoid the capture of minor spikes, set the default on the higher end of the range for your instance. | `0` (disabled)  | `0`, or   
`10`-`99` (%)   
High temp  
files usage  | Not configurable. This trigger is enabled automatically for MySQL 8.0 and later.  | Automatically triggers a capture when there's a significant increase in disk usage from the temporary files created by the MySQL process. Often temporary files are deleted but are still held open by a MySQL process.  
  
The threshold for this trigger uses a progressive escalation model for difference thresholds. It begins at 100 GB and doubles sequentially to 200 GB, 400 GB, up to 1.6 TB after every cooldown. By using a progressive escalation model, performance capture occurs only if the difference in temp file usage increases at a high level. | Enabled  | n/a   
History list  
length  | `historyListLengthThresholdCount` | Triggers a capture when the InnoDB History List Length (HLL) grows beyond the configured value. A persistently high HLL indicates that the InnoDB purge process is unable to keep up and the count of unpurged transactions is increasing, often due to long-running transactions. This high number can lead to increased storage consumption and performance issues.  
  
This threshold is workload-dependent. Some instances can operate sufficiently even with consistently high HLL. However, you can still use this trigger to highlight potential issues such as long-running reads, large data manipulation language (DML) statements, or purge thread bottlenecks. | `0` (disabled)  | `0`, or   
`10000`-`10000000`  
Long-running  
transactions  | `transactionDurationThreshold` | A transaction is logged if the transaction runs longer than the configured duration in seconds. This trigger is useful for identifying operations that might be holding locks for excessive periods or consuming resources for too long.  
  
Transactions that exceed `transactionDurationThreshold` are evaluated after each interval specified in the `probingIntervalSeconds` configuration (default 30 seconds). However, to manage log volume, the details of up to 10 of these long-running transactions are sent to Cloud Logging at most once every cooldown period (30 minutes). The full query text of up to 1024 bytes from `INFORMATION_SCHEMA.INNODB_TRX` is included in each log entry for the top 10 transactions. | `3600` (seconds)  | `60` or more   
Replica SQL/IO  
thread error  | Not configurable. This trigger is enabled by default automatically on all replica instances and can't be disabled.  | Triggers a capture immediately if the replication SQL thread or IO thread on a replica instance encounters any error and stops. This trigger is critical for maintaining replica integrity and identifying replication failures.  
  
This trigger doesn't use any probe configuration settings such as `probingIntervalseconds` or `probeThreshold` to validate performance capture conditions. | Enabled  | n/a   
Running threads  | `runningThreadsThreshold` | Triggers a capture when the number of active threads running based on the `threads_running` status variable exceeds the specified value. For example, you might configure the threshold to run performance capture if the number of active running threads goes higher than 100.  
  
This trigger is required for performance capture. If you don't configure this trigger explicitly, then the default is calculated based on the number of vCPUs that belong to instance. | `MIN(600,` `cpuCount * 20)` | `10` or more   
Seconds behind  
source  | `secondsBehindSourceThreshold` | Triggers a capture when the replication lag on the read replica instance, measured in seconds exceeds the specified value. You can use this trigger to monitor and diagnose delays in replication. This trigger is enabled automatically for replica instances. If you don't configure the trigger explicitly, then the default is 900 seconds. We recommend that you configure the value on the higher end to avoid excessive captures and frequent cooldowns. | `900` (seconds)  | `1` or more   
Semaphore waits  | `semaphoreWaitThresholdCount` | Triggers a capture when the number of threads waiting on internal InnoDB semaphores exceeds the configured value of this trigger. This advanced metric indicates contention, using either a mutex or a read-write lock, within the InnoDB storage engine itself. The usual contentions that are observed are Adaptive Hash Index (AHI) contention, buffer pool contention, and disk IO contention.  
  
A capture is also triggered if the maximum wait time for any single semaphore exceeds 200 seconds, regardless of the configured value of this trigger. | `0` (disabled)  | `0`, or   
`10`-`10000`  
Transaction  
lock waits  | `transactionLockWaitThresholdCount` | Triggers a capture when the number of transactions in a `LOCK WAIT` state surpasses the configured count. A small number of transactions in lock wait state can be normal in a busy system, but a consistently high number of lock waits are a strong indicator of application-level lock contention, unindexed DMLs, long idle transactions, and high concurrency row contentions which can severely degrade performance and throughput. | `0` (disabled)  | `0`, or   
`10`-`10000`  
  
## Pricing

Performance capture is available in all Cloud SQL regions at no additional costs. Standard charges apply only for underlying database resources. Performance capture stores logs in Cloud Logging, which can incur additional Cloud Logging storage costs.

For more information about the pricing for storing logs in Logging, see [Pricing](https://cloud.google.com/logging#pricing).

## Limitations

  * You must [enable query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights) to use performance capture. If you disable query insights, then performance capture is also disabled.
  * Performance capture is available only for Cloud SQL for MySQL 5.7 and later.



## What's next

  * [Configure performance capture](https://docs.cloud.google.com/sql/docs/mysql/configure-performance-capture)
  * [View performance capture logs](https://docs.cloud.google.com/sql/docs/mysql/view-performance-capture-logs)
  * [Monitor instances](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
