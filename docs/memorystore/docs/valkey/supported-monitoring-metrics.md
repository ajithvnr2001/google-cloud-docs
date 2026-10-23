---
url: https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics/
title: Supported monitoring metrics \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:01.427826+00:00
---

# Supported monitoring metrics  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Supported monitoring metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page lists metrics that are available for Memorystore for Valkey and describes what each metric measures.

To learn how to view these metrics, see [Monitor instances](https://docs.cloud.google.com/memorystore/docs/valkey/monitor-instances).

## Backup metrics

This section lists and describes [backup](https://docs.cloud.google.com/memorystore/docs/valkey/backups) and [import](https://docs.cloud.google.com/memorystore/docs/valkey/manage-backups#import) metrics.

### Instance-level metrics

This section lists and describes instance-level backup and import metrics.

Metric name | Description  
---|---  
`memorystore.googleapis.com/instance/backup/last_backup_start_time` | This metric shows the start time of the last backup operation.  
`memorystore.googleapis.com/instance/backup/last_backup_status` | This metric shows whether the most recent backup attempt completed successfully or failed. The statuses are `1` for `Success` and `0` for `Failed`.  
`memorystore.googleapis.com/instance/backup/last_backup_duration` | This metric shows the duration of the last backup operation (in milliseconds).  
`memorystore.googleapis.com/instance/backup/last_backup_size` | This metric shows the size of the last backup (in bytes). This metric is a key indicator for monitoring backup efficiency and storage capacity planning.  
`memorystore.googleapis.com/instance/import/last_import_start_time` | This metric shows the start time of the last import operation.  
`memorystore.googleapis.com/instance/import/last_import_duration` | This metric shows the duration of the last import operation (in milliseconds).  
  
## Bloom filter and JSON metrics

This section lists node-level metrics for [Bloom filters](https://docs.cloud.google.com/memorystore/docs/valkey/about-bloom-filters) and [JSON documents](https://docs.cloud.google.com/memorystore/docs/valkey/about-json).

### Node-level metrics

These metrics offer detailed insights about the total number of Bloom filter objects and JSON documents, and the amount of memory that these filters and documents consume.

Metric name | Description  
---|---  
`memorystore.googleapis.com/instance/node/bloomfilter/objects_count ` | This metric measures the total number of Bloom filter objects that are inserted into an instance.  
`memorystore.googleapis.com/instance/node/bloomfilter/used_memory ` | This metric measures the amount of memory that the Bloom filters consume. To prevent exceeding the capacity limits of the instance, you can use the metric to track the memory growth of scaling filters. These filters add subfilters when the instance's memory capacity is exceeded.   
`memorystore.googleapis.com/instance/node/json/documents_count ` | This metric measures the total number of JSON documents that are located on an instance node. You can use the metric to track data distribution and capacity because the metric shows how many documents are indexed, deleted, or merged at the node level.  
`memorystore.googleapis.com/instance/node/json/used_memory ` | This metric measures the amount of memory (in bytes or as a percentage of available memory) that JSON documents consume. You can use the metric to monitor capacity, identify memory-bound nodes, and trigger scaling actions.  
  
## Certificate Authority (CA) metrics

This section lists metrics that are associated with [customer-managed Certificate Authorities (CA)](https://docs.cloud.google.com/memorystore/docs/valkey/use-customer-managed-ca).

### Instance-level metrics

These metrics provide a high-level overview of the certificates that are associated with machines in an instance.

Metric name | Description  
---|---  
`memorystore.googleapis.com/instance/security/rotate_tls_cert_count` | This metric shows the status of rotating certificates that are associated with machines in an instance. The metric can have the following statuses:

  * `SUCCESS`: Memorystore for Valkey rotated the certificate.
  * `FAILED`: Memorystore for Valkey didn't rotate the certificate because the certificate isn't available, Memorystore for Valkey doesn't have permissions to rotate the certificate, or there's an internal error.
  * `SKIPPED`: Memorystore for Valkey skipped rotating the certificate because it doesn't have to be rotated.

  
  
## Cloud Monitoring metrics

This section lists and describes Cloud Monitoring metrics that are available for Memorystore for Valkey.

### Instance-level metrics

These metrics provide a high-level overview of the overall health and performance of an instance. You can use the metrics to understand the overall capacity and utilization of an instance as well as to identify potential bottlenecks or areas for improvement.

Metric name | Description  
---|---  
`memorystore.googleapis.com/instance/clients/average_connected_clients` | This metric measures the average number of active client connections to an instance over a specified time. You can use the metric to monitor connection scaling, identify application bottlenecks, and ensure that the instance is stable  
`memorystore.googleapis.com/instance/clients/maximum_connected_clients` | This metric shows the maximum number of active client connections across all nodes of an instance. You can use the metric to monitor the highest connection load on the instance at any time. This is critical to ensure a high performance for the instance because high connection counts can increase response times.  
`memorystore.googleapis.com/instance/clients/maximum_connection_duration` | This metric measures the maximum duration of a client connection for a single node in an instance. You can use this metric to manage resource exhaustion, ensure load balancing, and enforce security policies.  
`memorystore.googleapis.com/instance/clients/total_connected_clients` | This metric tracks the current number of active client connections to an instance. You can use the metric to monitor the load of your database and prevent connection limits.  
`memorystore.googleapis.com/instance/stats/total_connections_received_count` | This metric shows the cumulative number of client connections that are created in an instance in the last minute. You can use the metric to analyze traffic load, ensure that connection limits aren't exceeded, and determine whether you need to scale the instance.  
`memorystore.googleapis.com/instance/stats/total_rejected_connections_count` | This metric tracks the total number of connections to an instance that are rejected because the `maxclients` limit is reached.  
`memorystore.googleapis.com/instance/commandstats/total_usec_count` | This metric measures the total CPU time that each command consumes. The metric indicates the total microseconds used, which provides insights into an instance's performance and latency.  
`memorystore.googleapis.com/instance/commandstats/total_calls_count` | This metric measures the total number of calls that are associated with a specific command on an instance node in one minute. To identify bottlenecks or high traffic on specific commands, you can use the metric to monitor command throughput (commands per minute) across primary and replica nodes.  
`memorystore.googleapis.com/instance/cpu/average_utilization` | This metric shows the mean CPU utilization for an instance (from 0.0 to 1.0). You can use the metric to identify overprovisioned or underutilized resources, manage auto scaling thresholds, and detect performance bottlenecks, with an ideal utilization of 40%-70%.   
`memorystore.googleapis.com/instance/cpu/maximum_utilization` | This metric shows the peak CPU usage across all nodes in an instance (from 0.0 to 1.0). The metric summarizes only the `sys_main_thread` and `user_main_thread` states. It doesn't include other CPU states (such as `sys_children` or `user_children`) that are available in the `/instance/node/cpu/utilization ` metric. Make sure that CPU utilization doesn't exceed 0.8 seconds for the primary node and 0.5 seconds for each replica that's designated as a read replica. For more information, see [CPU usage best practices](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#cpu_usage_best_practices).  
`memorystore.googleapis.com/instance/stats/average_expired_keys` | This metric measures the mean number of key expiration events for all _primary_ nodes of an instance. You can use the metric to monitor the number of keys that are expiring.  
`memorystore.googleapis.com/instance/stats/maximum_expired_keys` | This metric measures the maximum number of key expiration events that are occurring across all _primary_ nodes of an instance.  
`memorystore.googleapis.com/instance/stats/total_expired_keys_count` | This metric tracks the total number of key expiration events that are occurring across all _primary_ nodes of an instance. You can use the metric to monitor the number of keys that are expiring.  
`memorystore.googleapis.com/instance/stats/average_evicted_keys` | This metric tracks the mean number of keys that are evicted because of memory capacity constraints across the _primary_ shards of an instance.   
`memorystore.googleapis.com/instance/stats/maximum_evicted_keys` | This metric shows the highest number of keys that are evicted from a node or shard of a _primary_ instance because of memory capacity.  
`memorystore.googleapis.com/instance/stats/total_evicted_keys_count` | This metric shows the total number of keys that are evicted by a node of of a _primary_ instance because of memory capacity.  
`memorystore.googleapis.com/instance/keyspace/total_keys` | This metric shows the number of keys that are stored in an instance.   
`memorystore.googleapis.com/instance/stats/average_keyspace_hits` | This metric shows the mean number of successful lookups of keys across all nodes in an instance.  
`memorystore.googleapis.com/instance/stats/maximum_keyspace_hits` | This metric shows the maximum number of successful lookups of keys in an instance node. You can use the metric to monitor the instance's performance and to identify potential hotspots across the instance.  
`memorystore.googleapis.com/instance/stats/total_keyspace_hits_count` | This metric tracks the cumulative number of successful lookups of keys across all nodes in an instance.  
`memorystore.googleapis.com/instance/stats/average_keyspace_misses` | This metric shows the mean number of failed lookups of keys across an instance. You can use the metric to track how often keys are requested but aren't found in the cache.  
`memorystore.googleapis.com/instance/stats/maximum_keyspace_misses` | This metric shows the maximum number of failed lookups of keys across an instance node.  
`memorystore.googleapis.com/instance/stats/total_keyspace_misses_count` | This metric shows the total number of failed lookups of keys across all instance nodes.  
`memorystore.googleapis.com/instance/memory/average_utilization` | This metric shows the mean memory utilization across an instance (from 0.0 to 1.0). You can use the metric to monitoring the instance's capacity and to set alert thresholds. For example, you can set an alert threshold to notify users when the average memory exceeds a specific percentage (for example, 80%).  
`memorystore.googleapis.com/instance/memory/maximum_utilization` | This metric shows the maximum memory utilization across all instance nodes (from 0.0 to 1.0). You can use the metric to identify when to scale an instance. We recommend that you monitor usage to ensure that it stays under 100%. Under high write loads, performance might degrade if this metric reaches 65% to 85%.  
`memorystore.googleapis.com/instance/memory/total_used_memory` | This metric shows the total memory usage of an instance (in bytes). You can use the metric to monitor the instance's capacity.  
`memorystore.googleapis.com/instance/memory/size` | This metric measures the total, used, and available RAM across all nodes in an instance. You can use the metric to monitor the instance's capacity and to prevent node failures.  
`memorystore.googleapis.com/instance/replication/average_ack_lag` | This metric shows the mean acknowledgement lag (in seconds) of replicas across an instance.   
  
_Acknowledgment lag_ is a bottleneck on the primary node in an instance. This bottleneck is caused by its replicas that can't keep up with the information that the primary node sends to them. When this happens, the primary node must wait for the acknowledgment that the replicas received the information. This might slow down transaction commits and cause a performance hit on the primary node.  
`memorystore.googleapis.com/instance/replication/maximum_ack_lag` | This metric shows the maximum acknowledgement lag (in seconds) of replicas across an instance.  
`memorystore.googleapis.com/instance/replication/average_offset_diff` | This metric shows the mean replication acknowledge offset diff (in bytes) across an instance.   
  
Replication acknowledge offset diff means the number of bytes that aren't replicated between replicas and their primary instances.  
`memorystore.googleapis.com/instance/replication/maximum_offset_diff` | This metric shows the maximum replication offset diff (in bytes) across an instance.  
  
Replication offset diff means the number of bytes that aren't replicated between replicas and their primary instances.  
`memorystore.googleapis.com/instance/stats/total_net_input_bytes_count` | This metric shows the count of incoming network bytes that an instance's endpoints receives.  
`memorystore.googleapis.com/instance/stats/total_net_output_bytes_count` | This metric shows the count of outgoing network bytes that an instance's endpoints sends.  
`memorystore.googleapis.com/instance/migration_status` | This metric provides the overall migration status for a Memorystore for Valkey instance. You can use the metric to monitor the health of migrations from self-managed Redis or Valkey workloads into Memorystore for Valkey.  
  
### Node-level metrics

These metrics offer detailed insights into the health and performance of individual nodes within an instance. You can use the metrics to troubleshoot issues with the nodes to optimize their performance.

Metric name | Description  
---|---  
`memorystore.googleapis.com/instance/node/clients/connected_clients` | This metric indicates the number of active client connections to an instance node, excluding replica connections. You can use the metric to monitor connection limits and to identify hotspots where a shard receives disproportionate traffic.  
`memorystore.googleapis.com/instance/node/clients/blocked_clients` | This metric shows the number of client connections that an instance node blocks. A high or rapidly increasing number of blocked client connections might indicate that many clients are waiting on operations. This can lead to an increased latency.  
`memorystore.googleapis.com/instance/node/server/uptime` | This metric measures the uptime of an instance node. You can use the metric to track how long a server runs continuously without a reboot or failure.  
`memorystore.googleapis.com/instance/node/stats/connections_received_count` | This metric tracks the total number of client connections that are created on an instance node within a specified period. You can use the metric to monitor connection traffic to individual nodes within an instance. As a result, you can analyze load distribution and identify spikes in connection activity.  
`memorystore.googleapis.com/instance/node/stats/rejected_connections_count` | This metric shows the number of connections that are rejected because an instance node reaches the `maxclients` limit. You can use the metric to identify if a node is under high-connection pressure and is refusing new connections because it can't handle more connections.  
`memorystore.googleapis.com/instance/node/commandstats/usec_count` | This metric shows the total time that each command consumes in an instance node. You can use the metric to analyze the performance of commands, identify slow commands, and troubleshoot latency issues at the node level.   
`memorystore.googleapis.com/instance/node/commandstats/calls_count` | This metric tracks the total number of calls for a command on an instance node per minute. You can use the metric to monitor traffic distribution, identify heavily used commands, and troubleshoot bottlenecks on individual nodes.  
`memorystore.googleapis.com/instance/node/cpu/utilization` | This metric shows the CPU utilization for an instance node (from 0.0 to 1.0).  
`memorystore.googleapis.com/instance/node/stats/expired_keys_count` | This metric shows the total number of expiration events in an instance node. You can use the metric to monitor the rate at which keys are being removed from the instance because their time to live (TTL) reaches zero.  
`memorystore.googleapis.com/instance/node/stats/evicted_keys_count` | This metric counts the total number of keys that an instance node evicts because the instance reaches its maximum memory limit. The metric can identify if an instance is under memory pressure. High or rising counts of evicted keys indicate that an instance is running out of space. As a result, the instance removes keys to make room for new data.  
`memorystore.googleapis.com/instance/node/keyspace/total_keys` | This metric measures the total number of keys that an instance node stores. The metric provides visibility into data distribution and sharding across nodes.  
`memorystore.googleapis.com/instance/node/stats/keyspace_hits_count` | This metric tracks the number of successful key lookups on an instance node. You can use the metric to monitor the efficiency that the node has to retrieve in-memory data.  
`memorystore.googleapis.com/instance/node/stats/keyspace_misses_count` | This metric tracks the number of failed key lookups on an instance node.   
`memorystore.googleapis.com/instance/node/memory/utilization` | This metric tracks the memory utilization in an instance node (from 0.0 to 1.0). You can use the metric to prevent node failures and to ensure an instance's stability.  
`memorystore.googleapis.com/instance/node/memory/usage` | This metric measures the total memory usage of an instance node.  
`memorystore.googleapis.com/instance/node/stats/net_input_bytes_count` | This metric measures the total number of incoming network bytes that an instance node receives. You can use the metric to monitor the network throughput, identify potential bottlenecks, and analyze traffic spikes on the node.  
`memorystore.googleapis.com/instance/node/stats/net_output_bytes_count` | This metric measures the total number of outgoing network bytes that an instance node sends. You can use the metric to monitor the network egress volume for the node for performance tuning and capacity planning purposes.   
`memorystore.googleapis.com/instance/node/replication/offset` | This metric measures the replication offset bytes of an instance node. Before you promote the replicas of an instance to primary instances, you can use the metric to check whether the replicas processed all data. This prevents data loss.  
`memorystore.googleapis.com/instance/node/server/healthy` | This metric determines whether an instance node is available and functioning correctly.   
`memorystore.googleapis.com/instance/node/migration_status` | This metric is associated with migrating the workloads of self-managed Redis and Valkey instances into Memorystore for Valkey. You can use the metric to determine whether the replication links between the shards of the source and target instances are healthy and active during the migration process.  
`memorystore.googleapis.com/instance/node/migration_received_bytes_size ` | This metric shows the number of bytes that a node of the target instance receives. The metric measures the inflow of data to the node during migration. You can use the metric to monitor the progress of data synchronization during the migration process.  
`memorystore.googleapis.com/instance/node/migration_link_reconnect_count ` | This metric measures the number of migration reconnect attempts. You can use the metric to determine how often the target instance tries to reconnect to the source instance so that the migration can occur.  
`memorystore.googleapis.com/instance/node/stats/evicted_clients_count ` | This metric tracks the total number of clients that Memorystore for Valkey disconnects because the aggregate memory consumed by all client buffers exceeds a predefined memory threshold. You can use the metric as a protective mechanism to prevent runaway memory usage by clients from exhausting server memory and triggering crashes.  
`memorystore.googleapis.com/instance/node/clients/tracking_clients ` | This metric tracks the number of active Valkey clients that are registered to receive server-side tracking and invalidation messages. You can use the metric to monitor and debug client-side caching implementations to ensure that server tracking is operating as expected.   
`memorystore.googleapis.com/instance/node/clients/maxclients` | This metric shows the maximum number of concurrent client connections that Memorystore for Valkey allows on an instance node.  
`memorystore.googleapis.com/instance/node/clients/recent_max_input_buffer ` | This metric reports the largest memory buffer (in bytes) that's used to process a single incoming client command among all active connections. You can use the metric to track connection stability and prevent memory bloat. If a specific client's input buffer size maxes out your limits consistently, then this can lead to network stalls or dropped connections across the instance.  
`memorystore.googleapis.com/instance/node/clients/recent_max_output_buffer ` | This metric measures the longest output list (in bytes) among the most recently connected client connections to a server. The metric is a vital indicator of the server's health because it identifies clients that request large amounts of data faster than the server can send it to them.  
`memorystore.googleapis.com/instance/node/commandstats/rejected_calls_count ` | The metric shows the number of Valkey commands (calls) that a server rejects before they're run. These calls are triggered by preconditions, such as having syntax errors in the command or running memory-constrained commands when the instance is out of memory (OOM).  
`memorystore.googleapis.com/instance/node/commandstats/failed_calls_count ` | This metric tracks the number of failed operations on an instance node. You can use the metric to assess whether your client application passes improper parameters or is out-of-sync with your dataset schema. In addition, you can diagnose whether an increase in failures correlates with command degradation.  
`memorystore.googleapis.com/instance/node/keyspace/keys_with_expiration ` | This metric tracks the number of active keys in an instance that have either a time-to-live (TTL) or an expiration timestamp set. You can use the metric to monitor caching limits, memory usage, and session management.  
`memorystore.googleapis.com/instance/node/memory/dataset_usage ` | This metric measures the amount of memory that datasets or primary data objects in an instance node consume.  
`memorystore.googleapis.com/instance/node/memory/mem_not_counted_for_evict ` | This metric shows the amount of memory that a server excludes when it evaluates the memory that it needs for key eviction. When Memorystore for Valkey calculates whether it needs to evict keys, it compares its total allocated memory (`used_memory`) against the configured `maxmemory` limit. However, the value for `mem_not_counted_for_evict` is subtracted from this equation.  
`memorystore.googleapis.com/instance/node/memory/number_of_cached_scripts ` | This metric tracks the total number of `EVAL` scripts that a server caches on an instance node. You can use the metric to monitor the overhead associated with Lua scripts in the instance.  
`memorystore.googleapis.com/instance/node/memory/number_of_functions ` | This metric tracks the total number of functions that are defined on an instance node. You can use the metric to gain insights into the use of the [Valkey Functions](https://valkey.io/topics/functions-intro/) feature in an instance.  
`memorystore.googleapis.com/instance/node/memory/lua_usage` | This metric tracks the number of bytes that Lua uses for `EVAL` scripts on an instance node.  
`memorystore.googleapis.com/instance/node/memory/replica_clients_usage ` | This metric tracks the amount of memory (in bytes) that replica clients consume on an instance node. The metric measures the memory that replica clients use. Because replica buffers share memory with the replication backlog, the metric can report a value of `0` when replicas don't trigger an increase in memory usage beyond what's allocated for the backlog.  
`memorystore.googleapis.com/instance/node/memory/normal_clients_usage ` | This metric tracks the amount of memory (in bytes) that non-replica clients use on an instance node. The metric measures the memory consumption from non-replica client connections.  
`memorystore.googleapis.com/instance/node/memory/peak_usage` | This metric tracks the peak memory that Memorystore for Valkey consumes on an instance node. The metric measures the maximum amount of memory (in bytes) that Memorystore for Valkey uses since it last started.  
`memorystore.googleapis.com/instance/node/memory/rss_usage` | This metric tracks the resident set size (RSS) usage of Memorystore for Valkey on an instance node. The metric represents the number of bytes that Memorystore for Valkey allocates. Monitoring RSS usage is vital because it reflects the actual physical RAM usage so it can detect high memory fragmentation. For example, if the RSS approaches the container limit of the instance, then this can lead to OOM issues.  
`memorystore.googleapis.com/instance/node/memory/scripts_usage ` | This metric tracks the memory overhead associated with scripts on an instance node. The metric measures the number of bytes of memory overhead that `EVAL` and Valkey Function scripts use. This memory is considered part of the overall   
`used_memory` of the instance.   
`memorystore.googleapis.com/instance/node/memory/maxmemory_policy ` | This metric tracks the eviction policy configuration for an instance node. The metric reports the current `maxmemory-policy` setting for the node, which determines how Memorystore for Valkey selects keys for eviction when it reaches the `maxmemory` limit.  
`memorystore.googleapis.com/instance/node/persistence/aof_enabled ` | This metric indicates whether Append-Only File (AOF) persistence is enabled on an instance node.  
`memorystore.googleapis.com/instance/node/persistence/async_loading ` | This metric indicates whether Memorystore for Valkey loads a replication dataset asynchronously while it serves existing data. The metric tracks the state where Memorystore for Valkey loads the dataset. This occurs when the `repl-diskless-load` configuration is enabled and set to `swapdb`.  
`memorystore.googleapis.com/instance/node/persistence/loading ` | This metric indicates whether Memorystore for Valkey loads a dump file on an instance node. You can use the metric to assess whether Memorystore for Valkey loads data from a persistent store, such as a Redis Database (RDB) snapshot or an AOF file.   
`memorystore.googleapis.com/instance/node/persistence/current_cow_peak ` | This metric tracks the peak memory usage associated with copy-on-write (COW) operations during a child fork process on an instance node. The metric measures the maximum size (in bytes) of COW memory while a child fork runs. This occurs during operations that involve forking the process, such as creating an RDB snapshot or performing an AOF rewrite. Monitoring the peak COW size is important for capacity planning and preventing OOM issues because the total memory usage of the node increases during the fork process by the amount of data that's modified while the fork is active.  
`memorystore.googleapis.com/instance/node/persistence/current_cow_size ` | This metric tracks the current size of COW memory while a child fork process is active on an instance node. The metric measures the size (in bytes) of memory that's copied during a fork process, such as creating an RDB snapshot or performing an AOF rewrite. You can use the metric to monitor the real-time memory overhead of an ongoing fork.  
`memorystore.googleapis.com/instance/node/persistence/rdb_last_bgsave_time_sec ` | This metric tracks the duration of the most recent background save (`BGSAVE`) operation for an RDB on an instance node. The metric measures how long (in seconds) the last RDB save operation took to complete.  You can use the metric to monitor the performance impact of persistence operations, especially during maintenance or scale-out events.  
`memorystore.googleapis.com/instance/node/persistence/rdb_last_cow_size ` | This metric tracks the size of the COW memory during the most recent RDB save operation on an instance node. The metric measures the amount of memory (in bytes) that's copied while the last RDB snapshot is created in the background. You can use the metric to debug potential issues with full synchronizations during maintenance or configuration updates because the metric provides insights into the memory overhead of the persistence process.   
`memorystore.googleapis.com/instance/node/persistence/current_fork_percentage ` | This metric tracks the progress of the current fork process on an instance node. The metric indicates the completion percentage for active fork operations, such as those used for RDB snapshots or AOF rewrites.  
`memorystore.googleapis.com/instance/node/persistence/aof_rewrite_in_progress ` | This metric provides a real-time status (`1` for true and `0` for false) of whether Memorystore for Valkey performs an AOF rewrite on an instance node. You can use the metric to determine if background AOF operations contribute to noticeable increases in latency or memory usage. Rewrite operations can trigger transient load spikes.  
`memorystore.googleapis.com/instance/node/persistence/aof_last_cow_size ` | This metric tracks the size of COW memory that's used during the most recent AOF rewrite operation on an instance node. The metric measures the amount of memory (in bytes) that Memorystore for Valkey copies while it performs the last background AOF rewrite. You can use the metric to monitor the COW memory size during persistence operations. This is critical for capacity planning because the total memory usage of the node increases during the fork process by the amount of data that's modified while the fork is active. If you don't manage the COW memory, then you might experience OOM issues for the instance.  
`memorystore.googleapis.com/instance/node/persistence/aof_last_rewrite_time_sec ` | This metric measures how long (in seconds) the most recent background AOF rewrite operation takes to complete on an instance node. You can use the metric to assess the performance impact of background AOF persistence and to understand the duration of transient load spikes that rewrite operations cause.   
`memorystore.googleapis.com/instance/node/errorstats/errors_count ` | This metric provides a granular view of errors that are derived from the `ERRORSTATS` section of Memorystore for Valkey's internal statistics. The metric measures the change in error counts over an interval.   
`memorystore.googleapis.com/instance/node/stats/expire_cycle_cpu_millisecond_count ` | This metric measures the cumulative amount of CPU time spent on active expiry cycles over an interval.  
`memorystore.googleapis.com/instance/node/stats/expired_keys_percentage ` | This metric shows the estimated expired key percentage at a point in time. The metric provides insights into the expiration process. If the percentage is consistently high, then Memorystore for Valkey might not allocate enough background CPU cycles to keep up with the rate of key expiration.  
`memorystore.googleapis.com/instance/node/stats/expired_time_cap_reached_count ` | This metric measures the cumulative count of cycles that hit the time limit over an interval. A high or increasing value for the metric often correlates with high memory usage from expired keys. To maintain the health of the dataset, more background CPU cycles might be needed.   
`memorystore.googleapis.com/instance/node/stats/pubsub_channels ` | This metric shows the global number of Pub/Sub channels that have client subscriptions.  
`memorystore.googleapis.com/instance/node/stats/pubsub_patterns ` | This metric shows the global number of Pub/Sub patterns that have client subscriptions.  
`memorystore.googleapis.com/instance/node/stats/pubsubshard_channels ` | This metric shows the global number of Pub/Sub shard channels that have client subscriptions.  
`memorystore.googleapis.com/instance/node/stats/total_fork_count ` | This metric measures the change in the total number of forks over an interval. The metric is a key indicator of Memorystore for Valkey's background activity. You can use the metric to monitor the fork frequency for capacity planning because each fork process involves COW memory. COW memory increases the overall memory footprint of an instance node.  
`memorystore.googleapis.com/instance/node/stats/tracking_total_keys ` | This metric shows the number of keys that Memorystore for Valkey tracks. The metric is a component of the server-side tracking feature, which lets clients maintain a local cache that's invalidated when keys change on Memorystore for Valkey.  
`memorystore.googleapis.com/instance/node/stats/tracking_total_items ` | This metric shows the total number of items that Memorystore for Valkey tracks. The metric represents the sum of all clients watching each key.  
`memorystore.googleapis.com/instance/node/stats/tracking_total_prefixes ` | This metric shows the number of prefixes that are tracked in Memorystore for Valkey's `prefix` table.  
`redis.googleapis.com/cluster/node/stats/latest_fork_usec ` | This metric shows the duration of the latest fork operation (in microseconds).  
`memorystore.googleapis.com/instance/node/replication/primary_sync_in_progress ` | This metric shows whether a primary instance is synchronizing with a replica. A value of `1` indicates that the synchronization is in progress; a value of `0` signifies that the instance isn't synchronizing with the replica. You can use the metric to troubleshoot data consistency issues and understand the progress of scale-out or maintenance events.  
`memorystore.googleapis.com/instance/node/replication/sync_partial_ok_count ` | This metric measures the number of successful partial resynchronization attempts.  
`memorystore.googleapis.com/instance/node/replication/sync_partial_err_count ` | This metric measures the number of failed partial resynchronization attempts. You can use the metric as an indicator of replication health. When a partial resynchronization fails, the replica must perform a full resynchronization. This involves creating an RDB snapshot on the primary instance and transferring the entire dataset over the network.  
`memorystore.googleapis.com/instance/node/replication/sync_full_count ` | This metric measures the change in the number of full resynchronizations that a primary instance has with a replica. A full resynchronization occurs when a partial resynchronization fails. This happens when the replication backlog on the primary instance isn't large enough to hold the data that the replica missed during a disconnection. You can use the metric to diagnose replication health and capacity issues for the instance.  
`memorystore.googleapis.com/instance/node/memory/maxmemory` | This metric reflects the `maxmemory` configuration setting for an instance node, which is the maximum amount of memory that Memorystore for Valkey can consume. This setting determines when Memorystore for Valkey begins to evict keys, based on the configured setting for the `maxmemory-policy`. You can use the metric for capacity planning and troubleshooting OOM issues because the metric defines the upper bound of memory usage for data storage and server overhead. For more information about the `maxmemory` and `maxmemory-policy` settings, see [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters).  
`memorystore.googleapis.com/instance/node/clients/pubsub_clients ` | This metric shows the number of Pub/Sub clients. You can use the metric to assess the overall client load and the resource usage that's dedicated to real-time messaging. **Important** : The metric is available only for instances that run versions 8.0 and later.  
`memorystore.googleapis.com/instance/node/clients/watching_clients ` | This metric shows the number of clients in watching mode. Watching clients are an indicator of active multi-key transactions that rely on optimistic concurrency control to ensure data integrity. **Important** : The metric is available only for instances that run versions 8.0 and later.  
`memorystore.googleapis.com/instance/node/stats/evicted_scripts_count ` | This metric shows the number of `EVAL` scripts that Memorystore for Valkey evicts because of the least recently used (LRU) eviction policy. Eviction occurs when Memorystore for Valkey must free up memory for other scripts or data based on the configured cache limits and the eviction policy. **Important** : The metric is available only for instances that run versions 8.0 and later.  
`memorystore.googleapis.com/instance/node/stats/client_query_buffer_limit_disconnections_count ` | This metric shows the total number of disconnections that occur because a client reaches the query buffer limit. You can use the metric as a protective mechanism to prevent runaway memory usage by clients. Runaway memory usage might result in exhausting the server's memory and triggering crashes. **Important** : The metric is available only for instances that run versions 8.0 and later.  
`memorystore.googleapis.com/instance/node/stats/client_output_buffer_limit_disconnections_count` | This metric shows the total number of disconnections that occur because a client reaches the output buffer limit. You can use the metric to monitor output buffer disconnections. Monitoring these disconnections is critical to maintain the server's stability because large output buffers are a common cause of unexpected memory pressure and OOM issues. **Important** : The metric is available only for instances that run versions 8.0 and later.  
`memorystore.googleapis.com/instance/node/stats/acl_access_denied_auths_count ` | This metric tracks the number of authentication and authorization failures for a user. This includes when the user provides an invalid token, their account is deactivated, or they're denied access because of an access control list (ACL). Every minute, Memorystore for Valkey aggregates this number and sends it to your Google Cloud project. You can find detailed information about these failures in the Data Access audit logs. To learn how to access these logs, see [ Monitor access using audit logs](https://docs.cloud.google.com/memorystore/docs/valkey/audit-logging).  
`memorystore.googleapis.com/instance/node/stats/acl_access_denied_commands_count ` | This metric tracks the number of times that a client issues a command but isn't authorized to do so because of the client's ACL permissions. Every minute, Memorystore for Valkey aggregates this number for each node and sends it to your Google Cloud project. You can find detailed information about these failures in the Data Access audit logs.   
`memorystore.googleapis.com/instance/node/stats/acl_key_denied_commands_count ` | This metric tracks the number of times that a client is denied access to a key because of the client's ACL permissions. Every minute, Memorystore for Valkey aggregates this number for each node and sends it to your Google Cloud project. You can find detailed information about these failures in the Data Access audit logs.  
`memorystore.googleapis.com/instance/node/stats/acl_channel_denied_commands_count ` | This metric tracks the number of times that a client is denied access to a Pub/Sub channel because of the client's ACL permissions. Every minute, Memorystore for Valkey aggregates this number for each node and sends it to your Google Cloud project. You can find detailed information about these failures in the Data Access audit logs.  
  
## Cross-region replication metrics

This section lists and describes [cross-region replication](https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication) metrics.

Metric name | Description  
---|---  
`memorystore.googleapis.com/instance/cross_instance_replication/secondary_replication_links` | This metric shows the number of shard links between the primary and secondary instances. Within a cross-region replication group, a primary instance reports the number of cross-region replication links that it has with the secondary instances in the group. For each secondary instance, this number is expected to be equal to the number of shards. If the number drops below the number of shards, then this metric identifies the number of shards when replication stopped between the replicator and the follower. In an ideal state, this metric has the same number as the shard count for the primary instance.  
`memorystore.googleapis.com/instance/cross_instance_replication/secondary_maximum_replication_offset_diff` | This metric shows the maximum replication offset difference between the primary and secondary shards.  
`memorystore.googleapis.com/instance/cross_instance_replication/secondary_average_replication_offset_diff` | This metric shows the average replication offset difference between the primary and secondary shards.  
  
## Persistence metrics

This section lists and describes [persistence](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview) metrics.

### RDB persistence metrics

This section lists and describes RDB persistence metrics.

#### Instance-level metrics

This section lists and describes instance-level RDB persistence metrics.

Metric name | Description  
---|---  
`memorystore.googleapis.com/instance/persistence/rdb_saves_count` | This metric tracks the cumulative number of times that an RDB persistence snapshot (also known as an _RDB save_) is taken on an instance node. You can use the metric to monitor the frequency and success of RDB snapshots on a per-node basis. The metric has a `status_code` field. To check if an RDB snapshot fails, filter the `status_code` field for the `3 - INTERNAL_ERROR` status.  
`memorystore.googleapis.com/instance/persistence/rdb_last_success_ages` | This metric shows a distribution snapshot age for all nodes across an instance. In the case of a recovery incident, you can use the metric to view the timeframe for data staleness. Ideally, the distribution has values that have less lag time (or the same lag time) than your snapshot frequency.  
  
#### Node-level metrics

Metric name | Description  
---|---  
`memorystore.googleapis.com/instance/node/persistence/rdb_bgsave_in_progress` | This metric indicates whether an RDB (`BGSAVE`) is active on an instance node. A status of `TRUE` means that the `BGSAVE` is active.  
`memorystore.googleapis.com/instance/node/persistence/rdb_last_bgsave_status` | This metric indicates whether the `BGSAVE` operation on an instance node completed or encountered an error. A status of `TRUE` means that the operation completed.  
`memorystore.googleapis.com/instance/node/persistence/rdb_saves_count` | This metric tracks the cumulative number of RDB snapshots that are created on an instance node. You can use the metric to monitor the frequency and success of snapshots on the node.  
`memorystore.googleapis.com/instance/node/persistence/rdb_last_save_age` | This metric measures the time, in seconds, that elapsed since the last successful RDB snapshot. You can use the metric to monitor the staleness of RDB persistence data on an instance node.  
`memorystore.googleapis.com/instance/node/persistence/rdb_next_save_time_until` | This metric measures the time remaining, in seconds, until the next RDB snapshot is scheduled to occur on an instance node. You can use the metric to monitor the schedule of RDB persistence and track when the next automatic snapshot is taken.  
`memorystore.googleapis.com/instance/node/persistence/current_save_keys_total` | This metric tracks the total number of keys that are processed in the current RDB save operation on an instance node.  
  
### AOF persistence metrics

This section lists and describes AOF persistence metrics.

#### Instance-level metrics

This section lists and describes instance-level AOF persistence metrics.

Metric name | Description  
---|---  
`memorystore.googleapis.com/instance/persistence/aof_fsync_lags` | This metric measures the time difference (or lag) for all nodes in an instance that passes between writing data to the AOF and when that data is synchronized successfully to durable storage. When the `appendfsync` parameter is set to `everysec`, you can use the metric to assess the health of persistence for the instance. Ideally, you want the distribution of the lag to have values that have less lag time (or the same time) than the synchronization frequency of the AOF.  
`memorystore.googleapis.com/instance/persistence/aof_rewrite_count` | This metric tracks the cumulative number of times that an instance node triggers an AOF rewrite operation. You can use the metric to diagnose performance issues because a high frequency of AOF rewrites might cause latency spikes or memory pressure on the instance. The metric has a `status_code` field. To check if AOF rewrites fail, filter this field for the `3 - INTERNAL_ERROR` status.  
  
#### Node-level metrics

This section lists and describes node-level AOF persistence metrics.

Metric name | Description  
---|---  
`memorystore.googleapis.com/instance/node/persistence/aof_last_write_status` | This metric shows the status of the last write operation to the AOF file on an instance node. If the status is `TRUE`, then the write operation is successful. You can use the metric to verify that Memorystore for Valkey persists data successfully.   
`memorystore.googleapis.com/instance/node/persistence/aof_last_bgrewrite_status` | This metric shows the status of the last AOF `bgrewrite` operation on an instance node. If the status is `TRUE`, then the operation is successful.  
`memorystore.googleapis.com/instance/node/persistence/aof_fsync_lag` | This metric measures the time difference (or lag) for an instance node that passes between writing data to the AOF and when that data is synchronized successfully to durable storage. When the `appendfsync` parameter is set to `everysec`, you can use the metric to assess the health of persistence for the node. If the process of synchronizing data takes longer than 1 second, then persistence lags behind the incoming data, which can lead to performance degradation or data loss in a crash scenario.  
`memorystore.googleapis.com/instance/node/persistence/aof_rewrites_count` | This metric tracks the cumulative number of times that an instance node triggers an AOF rewrite operation. You can use the metric to diagnose performance issues. High frequencies of AOF rewrites can lead to increased latency or memory pressure on the instance. The metric has a `status_code` field. To check if AOF rewrites fail, filter this field for the `3 - INTERNAL_ERROR` status.  
`memorystore.googleapis.com/instance/node/persistence/aof_fsync_errors_count` | This metric tracks the cumulative number of times that the AOF `fsync()` system call fails on an instance node. The metric is applicable only for AOF-enabled instances where the `appendfsync` parameter is set to either `everysec` or `always`.  
  
### Common persistence metrics

This section lists and describes metrics that are applicable to both AOF and RDB persistence.

#### Node-level metrics

This section lists and describes node-level AOF and RDB persistence metrics.

Metric name | Description  
---|---  
`memorystore.googleapis.com/instance/node/persistence/auto_restore_count` |  This metric tracks the cumulative number of times that an instance node restores from a persistence dump file (AOF or RDB) automatically. The metric has a `status_code` field. To check if restores fail, filter this field for the `2 - INTERNAL_ERROR` status.   
  
#### Sample use cases for persistence metrics

This section describes sample use cases for AOF and RDB persistence metrics.

##### Check if AOF write operations cause latency and memory pressure

Suppose you detect an increase of latency or memory usage on either an instance or a node within the instance. If this occurs, then check whether the extra usage is related to AOF persistence.

AOF rewrite operations can trigger transient load spikes. We recommend that you inspect the `aof_rewrites_count` metric because this metric gives you the cumulative count of AOF rewrites over the lifetime of the instance or instance node.

Suppose this metric shows that increments in the rewrites count correspond to latency increases. To reduce the frequency of rewrites, either reduce the write rate or increase the shard count.

##### Check if RDB save operations cause latency and memory pressure

Suppose you detect an increase of latency or memory usage on either an instance or a node within the instance. If this occurs, then check whether the extra usage is related to RDB persistence.

RDB save operations can trigger transient load spikes. We recommend that you inspect the `rdb_saves_count` metric because this metric gives you the cumulative count of RDB saves over the lifetime of the instance or instance node.

Suppose this metric shows that increments in the RDB saves count correspond to latency increases. To lower the frequency of RDB saves, increase the RDB snapshot interval. Also, to reduce the baseline load levels, scale out the instance.

## Interpret metrics for Memorystore for Valkey

Many metrics belong to the following categories: average, maximum, and total.

We provide _average_ and _maximum_ variations of the same metric so that you can use both metrics to identify hotspots for that metric family.

The _total_ value of the metric is independent from the _average_ and _maximum_ variations of the metric. This value provides insights that are separate and unrelated to the purpose of the variations for hotspots.

### Understand average and maximum metrics

Suppose you compare the values of the `average_keyspace_hits` and `maximum_keyspace_hits` metrics for an instance. As the difference between the two metrics grows, a greater difference indicates more hotspots for hits in the instance. A close value between the metrics indicates that hits are distributed more evenly across the nodes in the instance.

This principle applies to all metrics that have the _average_ and _maximum_ variations of the same metric.

#### Hotspot example

If you compare the values of the `average_keyspace_hits` and `maximum_keyspace_hits` metrics for all shards in an instance, then you can determine in which shards hotspots occur. For example, suppose shards in a six-shard instance have the following number of hits:

  * Shard 1 – 2 hits
  * Shard 2 – 2 hits
  * Shard 3 – 2 hits
  * Shard 4 – 2 hits
  * Shard 5 – 2 hits
  * Shard 6 – 8 hits



In this example, the `average_keyspace_hits` metric returns a value of 3, but the `maximum_keyspace_hits` metric returns a value of 8. The hits aren't distributed evenly across the shards in the instance. Shard 6 is a hotspot because it handles a disproportionately high amount of traffic.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
