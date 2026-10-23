---
url: https://docs.cloud.google.com/memorystore/docs/redis/supported-monitoring-metrics/
title: Supported monitoring metrics \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:53.682383+00:00
---

# Supported monitoring metrics  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/supported-monitoring-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Supported monitoring metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page lists metrics that are available for Memorystore for Redis and describes what each metric measures.

To learn how to view these metrics, see [Monitor instances](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances).

## Cloud Monitoring metrics

This section lists and describes Monitoring metrics that are available for Memorystore for Redis.

Metric name | Description  
---|---  
`redis.googleapis.com/keyspace/avg_ttl` | This metric measures the average time to live (TTL), in milliseconds, of all keys in a Redis database that have an expiration set. You can use the metric to understand the lifecycle of your cached data and identify if keys are expiring sooner or later than expected across your instances.   
`redis.googleapis.com/clients/blocked` | This metric tracks the number of client connections that are waiting for data to become available because blocking commands are running in an instance. These blocking commands include [`BLPOP`](https://redis.io/docs/latest/commands/blpop/), [`BRPOP`](https://redis.io/docs/latest/commands/brpop/), and [`BRPOPLPUSH`](https://redis.io/docs/latest/commands/brpoplpush/). A high number of blocked clients might indicate that your application is waiting on certain events or keys to be populated. You can monitor this metric to understand the behavior of your application, especially if you see unexpected increases in latency that might be tied to clients waiting on blocking operations.  
`redis.googleapis.com/replication/master/slaves/lag` | This metric measures the number of seconds that a replica lags behind a primary instance. Memorystore for Redis calculates the value for the metric by taking the current time and subtracting the time at which the replica acknowledges receiving the message of incoming bytes. You can use the metric to identify if a replica falls behind the primary instance.  
`redis.googleapis.com/replication/offset_diff` | This metric tracks the number of bytes that aren't replicated to a replica. The metric represents the difference between the replication byte offset of a primary instance and the replication byte offset of the replica. If there's no difference between these offsets, then the replica is fully in synchronization with the primary instance. As the primary instance replicates data to the replica during a failover process, you might notice an increase in these pending bytes.  
`redis.googleapis.com/stats/cache_hit_ratio` | This metric represents the ratio of successful Redis database calls to unsuccessful calls. A call is successful when the Redis database returns the value that the caller requested. A higher cache-to-hit ratio means that the cache is more fully utilized. This is beneficial for the performance of your application.  
`redis.googleapis.com/commands/calls` | This metric measures the number of Redis commands that are run each minute on a primary instance. These include all open source Redis commands, including [`SET` ](https://redis.io/docs/latest/commands/set/), [`GET`](https://redis.io/docs/latest/commands/get/), and [`HSET` ](https://redis.io/docs/latest/commands/hset/). The metric doesn't count Memorystore for Redis commands such as `create` or `update`. **Important** : To measure your instance's latency, use this metric with the Time per Call (`usec_per_call`) and Total Time of Calls (`total_time`) metrics. These metrics let you compare the speed of Redis commands at different points in time, indicating changes in instance latency. A discrepancy in latency lets you research what might cause latency at a given time.  
`redis.googleapis.com/clients/connected` | This metric displays the number of clients that are connected to an instance. You can monitor the metric to identify the load on the instance. If the number of connected clients approaches the `maxclients` limit, then the server might reject new connection attempts.  
`redis.googleapis.com/stats/cpu_utilization` | This metric measures the CPU usage time per minute that the Redis server uses. This time is broken down by the system-user space and the parent-child relationships. The value for CPU seconds shows the total CPU seconds for all threads of the Redis server's main process. If you want to see the CPU usage for the main thread only, then view the Main Thread CPU Seconds (`cpu_utilization_main_thread`) metric. High CPU utilization is a common cause for increased latency in Redis instances because it can lead to delays in command processing. By monitoring this metric, you can identify if a high load from numerous clients drives the CPU usage.   
`redis.googleapis.com/stats/evicted_keys` | This metric shows the number of keys that Memorystore for Redis evicts from an instance because the instance reaches the [`maxmemory`](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#maxmemory_configuration) limit. By monitoring this metric, you can determine if the instance's memory size is sufficient for your workload. If frequently accessed data is removed from the cache, then the key evictions can impact your application's performance.  
`redis.googleapis.com/keyspace/keys_with_expiration` | This metric tracks the number of keys in an instance that have an expiration configured. If no keys have an expiration, then "no data" is displayed in the chart for the metric.  
`redis.googleapis.com/keyspace/keys` | This metric shows the total number of keys that are stored in a database. If no keys are stored, then "no data" is displayed in the chart for the metric.  
`redis.googleapis.com/stats/cpu_utilization_main_thread` | This metric measures the CPU-seconds that the Redis server's main thread uses. This measurement is broken down by the system-user space and the parent-child relationship. You can monitor the metric to identify CPU usage spikes that occur on the main thread.  
`redis.googleapis.com/stats/memory/maxmemory` | This metric represents the maximum amount of memory ([`maxmemory`](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#maxmemory_configuration)) that keys can use in an instance. After this limit is reached, Memorystore for Redis evicts keys from the instance. This eviction process occurs in accordance with the eviction policy that's configured for the instance.  
`redis.googleapis.com/stats/memory/usage_ratio` | This metric shows the current memory usage of an instance that's expressed as a ratio of its maximum memory limit. You can monitor the metric to determine how close the instance is to its capacity. Based on the instance's configuration, reaching this limit triggers the key eviction process.  
`redis.googleapis.com/stats/keyspace_misses` | This metric tracks the number of failed lookups of keys in the main dictionary. Every time a client attempts to access a key that doesn't exist in the database, the metric increments. The metric is used to calculate the cache-to-hit ratio, which measures how effectively your application uses the cache. A high number of keyspace misses often indicates that the application is requesting data that isn't present in the cache. If the application has to fetch that data from a slower, backend datastore, then this can lead to increased latency.  
`redis.googleapis.com/replication/role` | This metric returns a value that identifies the role of a node in a replication group. A value of `1` indicates that the node is a primary; a value of `0` signifies that the node is a replica.  You can use the metric to monitor the status of nodes, especially during failover events where roles might switch. In addition, you can track the health and topology of Standard Tier instances, which support high availability through replication.  
`redis.googleapis.com/persistence/rdb/bgsave_in_progress` | This metric returns a value that identifies whether a background save (`BGSAVE`) operation of the Redis database (RDB) is active. A value of `1` indicates that a background RDB save is active; a value of `0` signifies that no background save is running. You can use the metric to track automated RDB snapshots or manual exports. In addition, by monitoring the metric, you can correlate transient spikes in memory usage or latency with ongoing persistence tasks.  
`redis.googleapis.com/stats/pubsub/channels` | This metric tracks the global number of Pub/Sub channels that have active client subscriptions in an instance. The metric measures the total count of unique channels to which clients are subscribed by using the [ `SUBSCRIBE`](https://redis.io/docs/latest/commands/subscribe/) or [`PSUBSCRIBE`](https://redis.io/docs/latest/commands/psubscribe/) commands.  
`redis.googleapis.com/stats/pubsub/patterns` | This metric tracks the global number of Pub/Sub patterns that have active client subscriptions in an instance. The metric measures the total count of unique patterns to which clients are subscribed. Clients typically create these subscriptions by using the [`PSUBSCRIBE`](https://redis.io/docs/latest/commands/psubscribe/) command.  
`redis.googleapis.com/stats/reject_connections_count` | This metric tracks the number of connection attempts that an instance rejects because of the following reasons:

  * The `maxclients` limit: the server reaches the maximum allowed number of concurrent client connections.
  * Memory pressure: the instance rejects new connections because of high memory utilization.
  * An invalid TLS connection: an instance where [ in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption) is enabled has TLS-related issues.

By monitoring the metric, you can identify capacity issues. If the number of rejected connections increases, then you might either need to scale the instance to handle more connections or increase the instance's memory capacity. In addition, when encryption is enforced, you can use the metric to help debug client-side connection issues.  
`redis.googleapis.com/replication/master_repl_offset` | This metric represents the total number of bytes that a primary instance produces and sends to a replica. By subtracting the Replication Byte Offset of the replica from this offset, you can calculate the size of the replication delay. When there's no difference between these offset values, then the replica is fully synchronized with the primary instance.   
`redis.googleapis.com/replication/master/slaves/offset` | This metric indicates the total number of bytes that a replica receives from a primary instance. By subtracting this offset from the Replication Byte Offset of the primary instance, you can calculate the size of the replication delay. When there's no difference between these offset values, then the replica is fully synchronized with the primary instance.  
`redis.googleapis.com/stats/memory/system_memory_usage_ratio` | This metric represents the amount of memory that's in use, expressed as a ratio of the total memory that's available for the system. The total available system memory is the memory that you provision for an instance plus additional memory that Memorystore for Redis provides to manage overhead processes.  
`redis.googleapis.com/stats/memory/system_memory_overload_duration` | This metric measures the total amount of time (in microseconds) that an instance is in system memory overload mode. You can use the metric to track periods where the instance's memory usage exceeds safe operating thresholds for the system. Persistent values in the metric might indicate that the instance is at risk of performance degradation or instability because of insufficient memory for overhead processes.  
`redis.googleapis.com/commands/usec_per_call` | This metric represents the average time spent for each Redis command call over one minute. This time is measured in microseconds. The metric is broken down by individual commands. This lets you monitor the performance of specific operations, such as [`GET`](https://redis.io/docs/latest/commands/get/), [`SET`](https://redis.io/docs/latest/commands/set/), and [`HSET`](https://redis.io/docs/latest/commands/hset/).  You can also use the metric to measure instance latency. By comparing the time per call at different points, you can identify changes in performance and investigate the causes of a latency discrepancy.  
`redis.googleapis.com/stats/connections/total` | This metric represents the total number of connections that the server accepts.  
`redis.googleapis.com/commands/total_time` | This metric measures the total amount of time, in microseconds, spent on each open source Redis command (such as [`SET`](https://redis.io/docs/latest/commands/set/), [ `GET`](https://redis.io/docs/latest/commands/get/), or [ `HSET`](https://redis.io/docs/latest/commands/hset/)) over the last second. For example, if the `SET` command uses 800,000 microseconds, then it takes 80% of a single CPU core to process all instances of that command combined.  
`redis.googleapis.com/stats/network_traffic` | This metric represents the total number of bytes that are sent to or from Redis. This count includes the bytes from the commands, the payload data, and any delimiters.  
`redis.googleapis.com/server/uptime` | This metric indicates the uptime of the running Redis server process.   
`redis.googleapis.com/stats/memory/usage` | This metric represents the total number of bytes that the Redis server process allocates.  
  
### Client-side metrics

This section lists and describes client-side metrics in Monitoring that are available for Memorystore for Redis.

Metric name | Description  
---|---  
`workload.googleapis.com/redis_client_rtt` | This metric measures the round-trip time (RTT), which is the time elapsed from the moment your application sends the command until your client fully receives the response. A high value for this metric indicates network congestion, cross-region or cross-zone routing delays, or an overloaded Memorystore for Redis server.   
`workload.googleapis.com/redis_client_blocking_latency` | This metric measures the time your application threads spend waiting to acquire an available TCP connection from the Redis client's connection pool. A high value for this metric indicates that your connection pool is too small for your concurrent application traffic, forcing threads to queue.  
`workload.googleapis.com/redis_application_blocking_latency` | This metric measures the time your application spends parsing, deserializing, or otherwise processing the response from Memorystore for Redis after it arrives over the network. A high value for this metric indicates that your application is CPU-starved or is retrieving excessively large payloads (for example, large JSON strings) that take a long time for the language interpreter to process.  
`workload.googleapis.com/redis_retry_count` | This metric measures the number of times a command fails to complete, triggering your client's internal exponential backoff retry loop. A high value for this metric indicates packet loss, transient network interruptions, or aggressive connection timeouts that close the TCP connection prematurely.  
`workload.googleapis.com/redis_connectivity_error_count` | This metric measures the number of times your client fails to establish a socket connection to the Memorystore for Redis server. A high value for this metric indicates a network misconfiguration, VPC peering issues, firewall blockages, or an unreachable instance.  
  
## Instance details metrics

This section lists and describes metrics that are available for an instance on the [**Instance details** page](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances#monitoring-instances-console) of the Google Cloud console.

Metric name | Description  
---|---  
Bytes pending replication | This metric shows the amount of data that's written to a primary node, but isn't copied to a replica node. This represents the difference between the replication byte offset of the primary instance and the offset of the replica. A value of zero for the metric indicates that the replica is fully synchronized with the primary instance. A high value typically occurs during periods of high write activity or during a failover process because data is being synchronized.  
Cache hit ratio | This metric shows the ratio of successful Redis database calls (hits) to the total number of calls (hits plus misses). The metric represents how effectively your application uses the cache.  A higher cache-to-hit ratio indicates that more requests are being fulfilled directly from the cache. This is beneficial for the performance of your application because it reduces latency. A low or dropping ratio often indicates that your application requests data that isn't present in the cache. This might require you to increase the size of the instance or adjust your data population logic.  
Calls | This metric shows the number of Redis commands that are run on a primary instance each minute. The metric counts all open source Redis commands, such as [`SET`](https://redis.io/docs/latest/commands/set/), [`GET`](https://redis.io/docs/latest/commands/get/), and [`HSET`](https://redis.io/docs/latest/commands/hset/). However, the metric doesn't include commands that are specific to Memorystore for Redis, such as [`create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/create) or [`update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/update). You can use the metric to measure and analyze the instance's latency. By comparing the volume of calls with the time spent on them, you can identify changes in performance and investigate what might cause latency spikes.  
Connected clients / Blocked clients | This metric shows the following information:

  * Connected clients: the total number of clients that are connected to an instance. You can use this information to identify the overall load on the instance. If the number of connected clients approaches the `maxclients` limit, then the server might begin rejecting new connection attempts. Tracking the number of connected clients helps you determine if you approach connection limits that require scaling or connection pooling. 
  * Blocked clients: the number of client connections that wait for data because they run blocking commands, such as [`BLPOP`](https://redis.io/docs/latest/commands/blpop/), [`BRPOP`](https://redis.io/docs/latest/commands/brpop/), and [`BRPOPLPUSH`](https://redis.io/docs/latest/commands/brpoplpush/). A high number of blocked clients can indicate that your application waits on specific events or for keys to be populated. This can manifest as increased latency in your application.

  
CPU seconds | This metric shows the total CPU usage time (in seconds) that an instance uses over a specific period. By monitoring this metric, you can determine whether the instance has a high CPU usage. This is a frequent cause of increased latency because high CPU utilization can delay the processing of commands. You can also use the metric to determine whether a high load from a large number of clients drives the CPU usage.  
Evicted keys / Expired keys | This metric shows the following information:

  * Evicted keys: the number of keys that Memorystore for Redis removes (evicts) from an instance because the instance reaches its maximum memory (`maxmemory`) limit
  * Expired keys: the number of keys that reach their expiration limit and are deleted

  
Instance uptime | This metric indicates the total amount of time that the Redis server process runs continuously. If an instance restarts because of a failover, maintenance, or an unexpected crash, the value for the metric drops to zero, and then increases again from the new start time. You can use the metric to identify and correlate unexpected service interruptions, failover events, or maintenance windows with other performance changes.  
Keys in database | This metric shows the total number of keys that are stored in each Redis database within an instance. The metric tracks all keys that reside in the databases, regardless of whether the keys have an expiration set. If no keys are stored in the databases, then "no data" is displayed in the chart for the metric, rather than a zero value. You can monitor the metric to verify that the instance receives traffic and stores data. A sudden drop in the metric might indicate data loss, mass eviction, or an instance restart.  
Memory usage / Max memory | This metric shows an instance's memory usage compared to its maximum memory (`maxmemory`) limit. This limit represents the maximum amount of memory that keys can use in the instance. After the limit is reached, Memorystore for Redis begins evicting keys in accordance with the eviction policy configured for the instance.  
Network bytes in/out | This metric shows the number of bytes that an instance sends and receives over a given period. This network traffic includes data from commands, payload data, and delimiters. You can use the metric to understand your application's network load, identify bandwidth bottlenecks, and correlate network spikes with either latency changes or your application's performance.  
Received connections/Rejected connections | This metric shows the successful (received) network connection attempts and rejected connection attempts over a given period. You can use the metric to understand your incoming connection rate, detect connection storms, and diagnose client connectivity or capacity issues.   
  
## RDB snapshot metrics

This section lists and describes metrics that help you manage [RDB snapshots](https://docs.cloud.google.com/memorystore/docs/redis/rdb-snapshots) for Memorystore for Redis.

#### Snapshot monitoring metrics

This section lists and describes snapshot monitoring metrics for Memorystore for Redis.

Metric name | Description  
---|---  
`redis.googleapis.com/rdb/enabled` | This metric indicates if the RDB snapshot mode is enabled for an instance.  
`redis.googleapis.com/rdb/snapshot/time_until_next_run` | This metric indicates the number of seconds until the next scheduled snapshot starts running.  
  
#### Snapshot status metrics

This section lists and describes snapshot status metrics for Memorystore for Redis.

Metric name | Description  
---|---  
`redis.googleapis.com/rdb/snapshot/in_progress` | This metric indicates whether an RDB snapshot is in progress. If the value of the metric is `true`, then the snapshot is occurring.   
`redis.googleapis.com/rdb/snapshot/elapsed_time` | This metric measures the amount of time that passes while the current snapshot is created.  
`redis.googleapis.com/rdb/snapshot/attempt_count` | This metric indicates the number of snapshot attempts that are made every minute.  
`redis.googleapis.com/rdb/snapshot/last_status` | This metric indicates the status of the most recent snapshot attempt.   
`redis.googleapis.com/rdb/snapshot/last_success_duration` | This metric indicates the total time required to write the last successful snapshot. This time doesn't include failed attempts.  
`redis.googleapis.com/rdb/snapshot/last_success_age` | This metric indicates the time that elapses since the start of the last successful snapshot.  
  
#### Snapshot recovery metrics

This section lists and describes snapshot recovery metrics for Memorystore for Redis.

Metric name | Description  
---|---  
`redis.googleapis.com/rdb/recovery/in_progress` | This metric indicates whether a recovery from an RDB snapshot takes place. If the value of this metric is `true`, then a recovery is in progress.  
`redis.googleapis.com/rdb/recovery/elapsed_time` | This metric indicates the increasing time that elapses during an in-progress recovery from an RDB snapshot.  
`redis.googleapis.com/rdb/recovery/estimated_recovery_time` | This metric indicates the expected time that it takes to recover when using the last successful RDB snapshot.  
`redis.googleapis.com/rdb/recovery/estimated_remaining_time` | This metric indicates the remaining time that it takes to finish a recovery from an RDB snapshot.  
`redis.googleapis.com/rdb/recovery/attempts_since_last_success ` | This metric indicates the number of recovery attempts since the last successful recovery attempt from an RDB snapshot.  
`redis.googleapis.com/rdb/recovery/last_status` | This metric indicates the status of the most recent recovery from an RDB snapshot.  
`redis.googleapis.com/rdb/recovery/last_duration` | This metric indicates the time that it takes to restore the last RDB snapshot.  
`redis.googleapis.com/rdb/recovery/total_bytes_count` | This metric indicates the size of an RDB snapshot.  
`redis.googleapis.com/rdb/recovery/loaded_bytes_count` | This metric indicates the number of bytes that load during the recovery from an RDB snapshot. If the recovery isn't active, then the number of bytes is `0`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
