---
url: https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics/
title: Supported monitoring metrics \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:14.633842+00:00
---

# Supported monitoring metrics  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Supported monitoring metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page lists metrics that are available for Memorystore for Redis Cluster and describes what each metric measures.

To learn how to view these metrics, see [Monitor clusters](https://docs.cloud.google.com/memorystore/docs/cluster/monitor-instances).

## Backup metrics

This section lists and describes [backup](https://docs.cloud.google.com/memorystore/docs/cluster/backups) and [import](https://docs.cloud.google.com/memorystore/docs/cluster/manage-backups#import) metrics.

### Cluster-level metrics

This section lists and describes cluster-level backup and import metrics.

Metric name | Description  
---|---  
`redis.googleapis.com/cluster/backup/last_backup_start_time` | This metric shows the start time of the last backup operation.  
`redis.googleapis.com/cluster/backup/last_backup_status` | This metric shows whether the most recent backup attempt completed successfully or failed. The statuses are `1` for `Success` and `0` for `Failed`.  
`redis.googleapis.com/cluster/backup/last_backup_duration` | This metric shows the duration of the last backup operation (in milliseconds).  
`redis.googleapis.com/cluster/backup/last_backup_size` | This metric shows the size of the last backup (in bytes). This metric is a key indicator for monitoring backup efficiency and storage capacity planning.  
`redis.googleapis.com/cluster/import/last_import_start_time` | This metric shows the start time of the last import operation.  
`redis.googleapis.com/cluster/import/last_import_duration` | This metric shows the duration of the last import operation (in milliseconds).  
  
## Certificate Authority (CA) metrics

This section lists metrics that are associated with [customer-managed Certificate Authorities (CA)](https://docs.cloud.google.com/memorystore/docs/cluster/use-customer-managed-ca).

### Cluster-level metrics

These metrics provide a high-level overview of the certificates that are associated with machines in a cluster.

Metric name | Description  
---|---  
`redis.googleapis.com/cluster/security/rotate_tls_cert_count` | This metric shows the status of rotating certificates that are associated with machines in a cluster. The metric can have the following statuses:

  * `SUCCESS`: Memorystore for Redis Cluster rotated the certificate.
  * `FAILED`: Memorystore for Redis Cluster didn't rotate the certificate because the certificate isn't available, Memorystore for Redis Cluster doesn't have permissions to rotate the certificate, or there's an internal error.
  * `SKIPPED`: Memorystore for Redis Cluster skipped rotating the certificate because it doesn't have to be rotated.

  
  
## Cloud Monitoring metrics

This section lists and describes Cloud Monitoring metrics that are available for Memorystore for Redis Cluster.

### Cluster-level metrics

These metrics provide a high-level overview of the overall health and performance of a cluster. You can use the metrics to understand the overall capacity and utilization of a cluster as well as to identify potential bottlenecks or areas for improvement.

Metric name | Description  
---|---  
`redis.googleapis.com/cluster/clients/average_connected_clients ` | This metric measures the average number of active client connections to a cluster over a specified time. You can use the metric to monitor connection scaling, identify application bottlenecks, and ensure that the cluster is stable.  
`redis.googleapis.com/cluster/clients/maximum_connected_clients ` | This metric shows the maximum number of active client connections across all nodes of a cluster. You can use the metric to monitor the highest connection load on the cluster at any time. This is critical to ensure a high performance for the cluster because high connection counts can increase response times.  
`redis.googleapis.com/cluster/clients/total_connected_clients ` | This metric tracks the current number of active client connections to a cluster. You can use the metric to monitor the load of your database and prevent connection limits.  
`redis.googleapis.com/cluster/stats/total_connections_received_count ` | This metric shows the cumulative number of client connections that are created in a cluster in the last minute. You can use the metric to analyze traffic load, ensure that connection limits aren't exceeded, and determine whether you need to scale the cluster.   
`redis.googleapis.com/cluster/stats/total_rejected_connections_count ` | This metric tracks the total number of connections to a cluster that are rejected because the `maxclients` limit is reached.  
`redis.googleapis.com/cluster/commandstats/total_usec_count` | This metric measures the total CPU time that each command consumes. The metric indicates the total microseconds used, which provides insights into a cluster's performance and latency.  
`redis.googleapis.com/cluster/commandstats/total_calls_count` | This metric measures the total number of calls that are associated with a specific command on a cluster node in one minute. To identify bottlenecks or high traffic on specific commands, you can use the metric to monitor command throughput (commands per minute) across primary and replica nodes.   
`redis.googleapis.com/cluster/cpu/average_utilization` | This metric shows the mean CPU utilization for a cluster (from 0.0 to 1.0). You can use the metric to identify overprovisioned or underutilized resources, manage auto scaling thresholds, and detect performance bottlenecks, with an ideal utilization of 40%-70%.  
`redis.googleapis.com/cluster/cpu/maximum_utilization` | This metric shows the peak CPU usage across all nodes in a cluster (from 0.0 to 1.0). The metric summarizes only the `sys_main_thread` and `user_main_thread` states. It doesn't include other CPU states (such as `sys_children` or `user_children`) that are available in the `/cluster/node/cpu/utilization ` metric. Make sure that CPU utilization doesn't exceed 0.8 seconds for the primary node and 0.5 seconds for each replica that's designated as a read replica. For more information, see [CPU usage best practices](https://docs.cloud.google.com/memorystore/docs/cluster/general-best-practices#cpu_usage_best_practices).  
`redis.googleapis.com/cluster/stats/average_expired_keys` | This metric measures the mean number of key expiration events for all _primary_ nodes of a cluster. You can use the metric to monitor the number of keys that are expiring.  
`redis.googleapis.com/cluster/stats/maximum_expired_keys` | This metric measures the maximum number of key expiration events that are occurring across all _primary_ nodes of a cluster.  
`redis.googleapis.com/cluster/stats/total_expired_keys_count` | This metric tracks the total number of key expiration events that are occurring across all _primary_ nodes of a cluster. You can use the metric to monitor the number of keys that are expiring.  
`redis.googleapis.com/cluster/stats/average_evicted_keys` | This metric tracks the mean number of keys that are evicted because of memory capacity constraints across the _primary_ shards of a cluster.   
`redis.googleapis.com/cluster/stats/maximum_evicted_keys` | This metric shows the highest number of keys that are evicted from a node or shard of a _primary_ cluster because of memory capacity.  
`redis.googleapis.com/cluster/stats/total_evicted_keys_count` | This metric shows the total number of keys that are evicted by a node of of a _primary_ cluster because of memory capacity.  
`redis.googleapis.com/cluster/keyspace/total_keys` | This metric shows the number of keys that are stored in a cluster.  
`redis.googleapis.com/cluster/stats/average_keyspace_hits` | This metric shows the mean number of successful lookups of keys across all nodes in a cluster.  
`redis.googleapis.com/cluster/stats/maximum_keyspace_hits` | This metric shows the maximum number of successful lookups of keys in a cluster node. You can use the metric to monitor the cluster's performance and to identify potential hotspots across the cluster.  
`redis.googleapis.com/cluster/stats/total_keyspace_hits_count` | This metric tracks the cumulative number of successful lookups of keys across all nodes in a cluster.  
`redis.googleapis.com/cluster/stats/average_keyspace_misses` | This metric shows the mean number of failed lookups of keys across a cluster. You can use the metric to track how often keys are requested but aren't found in the cache.  
`redis.googleapis.com/cluster/stats/maximum_keyspace_misses` | This metric shows the maximum number of failed lookups of keys across a cluster node.  
`redis.googleapis.com/cluster/stats/total_keyspace_misses_count` | This metric shows the total number of failed lookups of keys across all cluster nodes.  
`redis.googleapis.com/cluster/memory/average_utilization` | This metric shows the mean memory utilization across a cluster (from 0.0 to 1.0). You can use the metric to monitoring the cluster's capacity and to set alert thresholds. For example, you can set an alert threshold to notify users when the average memory exceeds a specific percentage (for example, 80%).  
`redis.googleapis.com/cluster/memory/maximum_utilization` | This metric shows the maximum memory utilization across all cluster nodes (from 0.0 to 1.0). You can use the metric to identify when to scale a cluster. We recommend that you monitor usage to ensure that it stays under 100%. Under high write loads, performance might degrade if this metric reaches 65% to 85%.  
`redis.googleapis.com/cluster/memory/total_used_memory` | This metric shows the total memory usage of a cluster (in bytes). You can use the metric to monitor the cluster's capacity.  
`redis.googleapis.com/cluster/memory/size` | This metric measures the total, used, and available RAM across all nodes in a cluster. You can use the metric to monitor the cluster's capacity and to prevent node failures.  
`redis.googleapis.com/cluster/replication/average_ack_lag` | This metric shows the mean acknowledgement lag (in seconds) of replicas across a cluster.   
  
_Acknowledgment lag_ is a bottleneck on the primary node in a cluster. This bottleneck is caused by its replicas that can't keep up with the information that the primary node sends to them. When this happens, the primary node must wait for the acknowledgment that the replicas received the information. This might slow down transaction commits and cause a performance hit on the primary node.  
`redis.googleapis.com/cluster/replication/maximum_ack_lag` | This metric shows the maximum acknowledgement lag (in seconds) of replicas across a cluster.   
`redis.googleapis.com/cluster/replication/average_offset_diff` | This metric shows the mean replication acknowledge offset diff (in bytes) across a cluster.   
  
Replication acknowledge offset diff means the number of bytes that aren't replicated between replicas and their primary clusters.  
`redis.googleapis.com/cluster/replication/maximum_offset_diff` | This metric shows the maximum replication offset diff (in bytes) across a cluster.  
  
Replication offset diff means the number of bytes that aren't replicated between replicas and their primary clusters.  
`redis.googleapis.com/cluster/stats/total_net_input_bytes_count` | This metric shows the count of incoming network bytes that a cluster's endpoints receives.  
`redis.googleapis.com/cluster/stats/total_net_output_bytes_count` | This metric shows the count of outgoing network bytes that a cluster's endpoints sends.  
  
### Node-level metrics

These metrics offer detailed insights into the health and performance of individual nodes within a cluster. You can use the metrics to troubleshoot issues with the nodes to optimize their performance.

Metric name | Description  
---|---  
`redis.googleapis.com/cluster/node/clients/connected_clients` | This metric indicates the number of active client connections to a cluster node, excluding replica connections. You can use the metric to monitor connection limits and to identify hotspots where a shard receives disproportionate traffic.  
`redis.googleapis.com/cluster/node/clients/blocked_clients` | This metric shows the number of client connections that a cluster node blocks. A high or rapidly increasing number of blocked client connections might indicate that many clients are waiting on operations. This can lead to an increased latency.  
`redis.googleapis.com/cluster/node/server/uptime` | This metric measures the uptime of a cluster node. You can use the metric to track how long a server runs continuously without a reboot or failure.  
`redis.googleapis.com/cluster/node/stats/connections_received_count` | This metric tracks the total number of client connections that are created on a cluster node within a specified period. You can use the metric to monitor connection traffic to individual nodes within a cluster. As a result, you can analyze load distribution and identify spikes in connection activity.  
`redis.googleapis.com/cluster/node/stats/rejected_connections_count` | This metric shows the number of connections that are rejected because a cluster node reaches the `maxclients` limit. You can use the metric to identify if a node is under high-connection pressure and is refusing new connections because it can't handle more connections.  
`redis.googleapis.com/cluster/node/commandstats/usec_count` | This metric shows the total time that each command consumes in a cluster node. You can use the metric to analyze the performance of commands, identify slow commands, and troubleshoot latency issues at the node level.   
`redis.googleapis.com/cluster/node/commandstats/calls_count` | This metric tracks the total number of calls for a command on a cluster node per minute. You can use the metric to monitor traffic distribution, identify heavily used commands, and troubleshoot bottlenecks on individual nodes.  
`redis.googleapis.com/cluster/node/cpu/utilization` | This metric shows the CPU utilization for a cluster node (from 0.0 to 1.0).  
`redis.googleapis.com/cluster/node/stats/expired_keys_count` | This metric shows the total number of expiration events in a cluster node. You can use the metric to monitor the rate at which keys are being removed from the cluster because their time to live (TTL) reaches zero.  
`redis.googleapis.com/cluster/node/stats/evicted_keys_count` | This metric counts the total number of keys that a cluster node evicts because the cluster reaches its maximum memory limit. The metric can identify if a cluster is under memory pressure. High or rising counts of evicted keys indicate that a cluster is running out of space. As a result, the cluster removes keys to make room for new data.  
`redis.googleapis.com/cluster/node/keyspace/total_keys` | This metric measures the total number of keys that a cluster node stores. The metric provides visibility into data distribution and sharding across nodes.  
`redis.googleapis.com/cluster/node/stats/keyspace_hits_count` | This metric tracks the number of successful key lookups on a cluster node. You can use the metric to monitor the efficiency that the node has to retrieve in-memory data.  
`redis.googleapis.com/cluster/node/stats/keyspace_misses_count` | This metric tracks the number of failed key lookups on a cluster node.  
`redis.googleapis.com/cluster/node/memory/utilization` | This metric tracks the memory utilization in a cluster node (from 0.0 to 1.0). You can use the metric to prevent node failures and to ensure a cluster's stability.  
`redis.googleapis.com/cluster/node/memory/usage` | This metric measures the total memory usage of a cluster node.  
`redis.googleapis.com/cluster/node/stats/net_input_bytes_count` | This metric measures the total number of incoming network bytes that a cluster node receives. You can use the metric to monitor the network throughput, identify potential bottlenecks, and analyze traffic spikes on the node.  
`redis.googleapis.com/cluster/node/stats/net_output_bytes_count` | This metric measures the total number of outgoing network bytes that a cluster node sends. You can use the metric to monitor the network egress volume for the node for performance tuning and capacity planning purposes.   
`redis.googleapis.com/cluster/node/replication/offset` | This metric measures the replication offset bytes of a cluster node. Before you promote the replicas of a cluster to primary clusters, you can use the metric to check whether the replicas processed all data. This prevents data loss.  
`redis.googleapis.com/cluster/node/server/healthy` | This metric determines whether a cluster node is available and functioning correctly.   
`redis.googleapis.com/cluster/node/stats/evicted_clients_count ` | This metric tracks the total number of clients that Memorystore for Redis Cluster disconnects because the aggregate memory consumed by all client buffers exceeds a predefined memory threshold. You can use the metric as a protective mechanism to prevent runaway memory usage by clients from exhausting server memory and triggering crashes.  
`redis.googleapis.com/cluster/node/clients/tracking_clients` | This metric tracks the number of active Redis clients that are registered to receive server-side tracking and invalidation messages. You can use the metric to monitor and debug client-side caching implementations to ensure that server tracking is operating as expected.   
`redis.googleapis.com/cluster/node/clients/maxclients` | This metric shows the maximum number of concurrent client connections that Memorystore for Redis Cluster allows on a cluster node.  
`redis.googleapis.com/cluster/node/clients/recent_max_input_buffer ` | This metric reports the largest memory buffer (in bytes) that's used to process a single incoming client command among all active connections. You can use the metric to track connection stability and prevent memory bloat. If a specific client's input buffer size maxes out your limits consistently, then this can lead to network stalls or dropped connections across the cluster.  
`redis.googleapis.com/cluster/node/clients/recent_max_output_buffer ` | This metric measures the longest output list (in bytes) among the most recently connected client connections to a server. The metric is a vital indicator of the server's health because it identifies clients that request large amounts of data faster than the server can send it to them.  
`redis.googleapis.com/cluster/node/commandstats/rejected_calls_count ` | The metric shows the number of Redis commands (calls) that a server rejects before they're run. These calls are triggered by preconditions, such as having syntax errors in the command or running memory-constrained commands when the cluster is out of memory (OOM).  
`redis.googleapis.com/cluster/node/commandstats/failed_calls_count ` | This metric tracks the number of failed operations on a cluster node. You can use the metric to assess whether your client application passes improper parameters or is out-of-sync with your dataset schema. In addition, you can diagnose whether an increase in failures correlates with command degradation.  
`redis.googleapis.com/cluster/node/keyspace/keys_with_expiration ` | This metric tracks the number of active keys in a cluster that have either a time-to-live (TTL) or an expiration timestamp set. You can use the metric to monitor caching limits, memory usage, and session management.  
`redis.googleapis.com/cluster/node/memory/dataset_usage` | This metric measures the amount of memory that datasets or primary data objects in a cluster node consume.  
`redis.googleapis.com/cluster/node/memory/mem_not_counted_for_evict ` | This metric shows the amount of memory that a server excludes when it evaluates the memory that it needs for key eviction. When Memorystore for Redis Cluster calculates whether it needs to evict keys, it compares its total allocated memory (`used_memory`) against the configured `maxmemory` limit. However, the value for `mem_not_counted_for_evict` is subtracted from this equation.  
`redis.googleapis.com/cluster/node/memory/number_of_cached_scripts ` | This metric tracks the total number of `EVAL` scripts that a server caches on a cluster node. You can use the metric to monitor the overhead associated with Lua scripts in the cluster.  
`redis.googleapis.com/cluster/node/memory/number_of_functions ` | This metric tracks the total number of functions that are defined on a cluster node.  
`redis.googleapis.com/cluster/node/memory/lua_usage` | This metric tracks the number of bytes that Lua uses for `EVAL` scripts on a cluster node.  
`redis.googleapis.com/cluster/node/memory/replica_clients_usage ` | This metric tracks the amount of memory (in bytes) that replica clients consume on a cluster node. The metric measures the memory that replica clients use. Because replica buffers share memory with the replication backlog, the metric can report a value of `0` when replicas don't trigger an increase in memory usage beyond what's allocated for the backlog.  
`redis.googleapis.com/cluster/node/memory/normal_clients_usage ` | This metric tracks the amount of memory (in bytes) that non-replica clients use on a cluster node. The metric measures the memory consumption from non-replica client connections.  
`redis.googleapis.com/cluster/node/memory/peak_usage` | This metric tracks the peak memory that Memorystore for Redis Cluster consumes on a cluster node. The metric measures the maximum amount of memory (in bytes) that Memorystore for Redis Cluster uses since it last started.  
`redis.googleapis.com/cluster/node/memory/rss_usage` | This metric tracks the resident set size (RSS) usage of Memorystore for Redis Cluster on a cluster node. The metric represents the number of bytes that Memorystore for Redis Cluster allocates. Monitoring RSS usage is vital because it reflects the actual physical RAM usage so it can detect high memory fragmentation. For example, if the RSS approaches the container limit of the cluster, then this can lead to OOM issues.  
`redis.googleapis.com/cluster/node/memory/scripts_usage` | This metric tracks the memory overhead associated with scripts on a cluster node. The metric measures the number of bytes of memory overhead that the `EVAL` function uses. This memory is considered part of the overall `used_memory` of the cluster.   
`redis.googleapis.com/cluster/node/memory/maxmemory_policy` | This metric tracks the eviction policy configuration for a cluster node. The metric reports the current `maxmemory-policy` setting for the node, which determines how Memorystore for Redis Cluster selects keys for eviction when it reaches the `maxmemory` limit.  
`redis.googleapis.com/cluster/node/persistence/aof_enabled ` | This metric indicates whether Append-Only File (AOF) persistence is enabled on a cluster node.  
`redis.googleapis.com/cluster/node/persistence/async_loading ` | This metric indicates whether Memorystore for Redis Cluster loads a replication dataset asynchronously while it serves existing data. The metric tracks the state where Memorystore for Redis Cluster loads the dataset. This occurs when the `repl-diskless-load` configuration is enabled and set to `swapdb`.  
`redis.googleapis.com/cluster/node/persistence/loading` | This metric indicates whether Memorystore for Redis Cluster loads a dump file on a cluster node. You can use the metric to assess whether Memorystore for Redis Cluster loads data from a persistent store, such as a Redis Database (RDB) snapshot or an AOF file.   
`redis.googleapis.com/cluster/node/persistence/current_cow_peak ` | This metric tracks the peak memory usage associated with copy-on-write (COW) operations during a child fork process on a cluster node. The metric measures the maximum size (in bytes) of COW memory while a child fork runs. This occurs during operations that involve forking the process, such as creating an RDB snapshot or performing an AOF rewrite. Monitoring the peak COW size is important for capacity planning and preventing OOM issues because the total memory usage of the node increases during the fork process by the amount of data that's modified while the fork is active.  
`redis.googleapis.com/cluster/node/persistence/current_cow_size ` | This metric tracks the current size of COW memory while a child fork process is active on a cluster node. The metric measures the size (in bytes) of memory that's copied during a fork process, such as creating an RDB snapshot or performing an AOF rewrite. You can use the metric to monitor the real-time memory overhead of an ongoing fork.  
`redis.googleapis.com/cluster/node/persistence/rdb_last_bgsave_time_sec ` | This metric tracks the duration of the most recent background save (`BGSAVE`) operation for an RDB on a cluster node. The metric measures how long (in seconds) the last RDB save operation took to complete.  You can use the metric to monitor the performance impact of persistence operations, especially during maintenance or scale-out events.  
`redis.googleapis.com/cluster/node/persistence/rdb_last_cow_size ` | This metric tracks the size of the COW memory during the most recent RDB save operation on a cluster node. The metric measures the amount of memory (in bytes) that's copied while the last RDB snapshot is created in the background. You can use the metric to debug potential issues with full synchronizations during maintenance or configuration updates because the metric provides insights into the memory overhead of the persistence process.   
`redis.googleapis.com/cluster/node/persistence/current_fork_percentage ` | This metric tracks the progress of the current fork process on a cluster node. The metric indicates the completion percentage for active fork operations, such as those used for RDB snapshots or AOF rewrites.  
`redis.googleapis.com/cluster/node/persistence/aof_rewrite_in_progress ` | This metric provides a real-time status (`1` for true and `0` for false) of whether Memorystore for Redis Cluster performs an AOF rewrite on a cluster node. You can use the metric to determine if background AOF operations contribute to noticeable increases in latency or memory usage. Rewrite operations can trigger transient load spikes.  
`redis.googleapis.com/cluster/node/persistence/aof_last_cow_size ` | This metric tracks the size of COW memory that's used during the most recent AOF rewrite operation on a cluster node. The metric measures the amount of memory (in bytes) that Memorystore for Redis Cluster copies while it performs the last background AOF rewrite. You can use the metric to monitor the COW memory size during persistence operations. This is critical for capacity planning because the total memory usage of the node increases during the fork process by the amount of data that's modified while the fork is active. If you don't manage the COW memory, then you might experience OOM issues for the cluster.  
`redis.googleapis.com/cluster/node/persistence/aof_last_rewrite_time_sec ` | This metric measures how long (in seconds) the most recent background AOF rewrite operation takes to complete on a cluster node. You can use the metric to assess the performance impact of background AOF persistence and to understand the duration of transient load spikes that rewrite operations cause.   
`redis.googleapis.com/cluster/node/errorstats/errors_count` | This metric provides a granular view of errors that are derived from the `ERRORSTATS` section of Memorystore for Redis Cluster's internal statistics. The metric measures the change in error counts over an interval.   
`redis.googleapis.com/cluster/node/stats/expire_cycle_cpu_millisecond_count ` | This metric measures the cumulative amount of CPU time spent on active expiry cycles over an interval.  
`redis.googleapis.com/cluster/node/stats/expired_keys_percentage ` | This metric shows the estimated expired key percentage at a point in time. The metric provides insights into the expiration process. If the percentage is consistently high, then Memorystore for Redis Cluster might not allocate enough background CPU cycles to keep up with the rate of key expiration.  
`redis.googleapis.com/cluster/node/stats/expired_time_cap_reached_count ` | This metric measures the cumulative count of cycles that hit the time limit over an interval. A high or increasing value for the metric often correlates with high memory usage from expired keys. To maintain the health of the dataset, more background CPU cycles might be needed.   
`redis.googleapis.com/cluster/node/stats/pubsub_channels` | This metric shows the global number of Pub/Sub channels that have client subscriptions.  
`redis.googleapis.com/cluster/node/stats/pubsub_patterns` | This metric shows the global number of Pub/Sub patterns that have client subscriptions.  
`redis.googleapis.com/cluster/node/stats/pubsubshard_channels ` | This metric shows the global number of Pub/Sub shard channels that have client subscriptions.  
`redis.googleapis.com/cluster/node/stats/total_fork_count` | This metric measures the change in the total number of forks over an interval. The metric is a key indicator of Memorystore for Redis Cluster's background activity. You can use the metric to monitor the fork frequency for capacity planning because each fork process involves COW memory. COW memory increases the overall memory footprint of a cluster node.  
`redis.googleapis.com/cluster/node/stats/tracking_total_keys` | This metric shows the number of keys that Memorystore for Redis Cluster tracks. The metric is a component of the server-side tracking feature, which lets clients maintain a local cache that's invalidated when keys change on Memorystore for Redis Cluster.  
`redis.googleapis.com/cluster/node/stats/tracking_total_items ` | This metric shows the total number of items that Memorystore for Redis Cluster tracks. The metric represents the sum of all clients watching each key.  
`redis.googleapis.com/cluster/node/stats/tracking_total_prefixes ` | This metric shows the number of prefixes that are tracked in Memorystore for Redis Cluster's `prefix` table.  
`redis.googleapis.com/cluster/node/stats/latest_fork_usec ` | This metric shows the duration of the latest fork operation (in microseconds).  
`redis.googleapis.com/cluster/node/replication/primary_sync_in_progress ` | This metric shows whether a primary cluster is synchronizing with a replica. A value of `1` indicates that the synchronization is in progress; a value of `0` signifies that the cluster isn't synchronizing with the replica. You can use the metric to troubleshoot data consistency issues and understand the progress of scale-out or maintenance events.  
`redis.googleapis.com/cluster/node/replication/sync_partial_ok_count ` | This metric measures the number of successful partial resynchronization attempts.  
`redis.googleapis.com/cluster/node/replication/sync_partial_err_count ` | This metric measures the number of failed partial resynchronization attempts. You can use the metric as an indicator of replication health. When a partial resynchronization fails, the replica must perform a full resynchronization. This involves creating an RDB snapshot on the primary cluster and transferring the entire dataset over the network.  
`redis.googleapis.com/cluster/node/replication/sync_full_count ` | This metric measures the change in the number of full resynchronizations that a primary cluster has with a replica. A full resynchronization occurs when a partial resynchronization fails. This happens when the replication backlog on the primary cluster isn't large enough to hold the data that the replica missed during a disconnection. You can use the metric to diagnose replication health and capacity issues for the cluster.  
`redis.googleapis.com/cluster/node/memory/maxmemory` | This metric reflects the `maxmemory` configuration setting for a cluster node, which is the maximum amount of memory that Memorystore for Redis Cluster can consume. This setting determines when Memorystore for Redis Cluster begins to evict keys, based on the configured setting for the `maxmemory-policy`. You can use the metric for capacity planning and troubleshooting OOM issues because the metric defines the upper bound of memory usage for data storage and server overhead. For more information about the `maxmemory` and `maxmemory-policy` settings, see [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters).  
`redis.googleapis.com/cluster/node/stats/acl_access_denied_auths_count` | This metric tracks the number of authentication and authorization failures for a user. This includes when the user provides an invalid token, their account is deactivated, or they're denied access because of an access control list (ACL). Every minute, Memorystore for Redis Cluster aggregates this number and sends it to your Google Cloud project. You can find detailed information about these failures in the Data Access audit logs. To learn how to access these logs, see [ Monitor access using audit logs](https://docs.cloud.google.com/memorystore/docs/cluster/audit-logs).  
`redis.googleapis.com/cluster/node/stats/acl_access_denied_commands_count ` | This metric tracks the number of times that a client issues a command but isn't authorized to do so because of the client's access control list (ACL) permissions. Every minute, Memorystore for Redis Cluster aggregates this number for each node and sends it to your Google Cloud project. You can find detailed information about these failures in the Data Access audit logs.  
`redis.googleapis.com/cluster/node/stats/acl_key_denied_commands_count ` | This metric tracks the number of times that a client is denied access to a key because of the client's ACL permissions. Every minute, Memorystore for Redis Cluster aggregates this number for each node and sends it to your Google Cloud project. You can find detailed information about these failures in the Data Access audit logs.  
`redis.googleapis.com/cluster/node/stats/acl_channel_denied_commands_count ` | This metric tracks the number of times that a client is denied access to a Pub/Sub channel because of the client's ACL permissions. Every minute, Memorystore for Redis Cluster aggregates this number for each node and sends it to your Google Cloud project. You can find detailed information about these failures in the Data Access audit logs.  
  
## Cross-region replication metrics

This section lists and describes [cross-region replication](https://docs.cloud.google.com/memorystore/docs/cluster/about-cross-region-replication) metrics.

Metric name | Description  
---|---  
`redis.googleapis.com/cluster/cross_cluster_replication/secondary_replication_links` | This metric shows the number of shard links between the primary and secondary clusters. Within a cross-region replication group, a primary cluster reports the number of CRR replication links that it has with the secondary clusters in the group. For each secondary cluster, this number is expected to be equal to the number of shards. If, unexpectedly, the number drops below the number of shards, this identifies the number of shards where replication between the replicator and follower has ceased. In an ideal state, this metric should have the same number as the primary cluster shard count.  
`redis.googleapis.com/cluster/cross_cluster_replication/secondary_maximum_replication_offset_diff` | This metric measures the maximum replication offset difference (in bytes) between the primary and secondary (replica) shards of a cluster across different regions.  
`redis.googleapis.com/cluster/cross_cluster_replication/secondary_average_replication_offset_diff` | This metric measures the average replication offset difference (in bytes) between the primary and replica shards of a cluster across different regions. High values for the metric indicate a replication lag, which you can resolve by pausing and then resuming the replication.  
  
## JSON metrics

This section lists node-level metrics for [JSON documents](https://docs.cloud.google.com/memorystore/docs/cluster/about-json).

### Node-level metrics

These metrics offer detailed insights about the total number of JSON documents and the amount of memory that these documents consume.

Metric name | Description  
---|---  
`redis.googleapis.com/cluster/node/json/documents_count ` | This metric measures the total number of JSON documents that are located on a cluster node. You can use the metric to track data distribution and capacity because the metric shows how many documents are indexed, deleted, or merged at the node level.  
`redis.googleapis.com/cluster/node/json/used_memory ` | This metric measures the amount of memory (in bytes or as a percentage of available memory) that JSON documents consume. You can use the metric to monitor capacity, identify memory-bound nodes, and trigger scaling actions.  
  
## Persistence metrics

This section lists and describes [persistence](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview) metrics.

### RDB persistence metrics

This section lists and describes RDB persistence metrics.

#### Cluster-level metrics

This section lists and describes cluster-level RDB persistence metrics.

Metric name | Description  
---|---  
`redis.googleapis.com/cluster/persistence/rdb_saves_count` | This metric tracks the cumulative number of times that an RDB persistence snapshot (also known as an _RDB save_) is taken on a cluster node. You can use the metric to monitor the frequency and success of RDB snapshots on a per-node basis. The metric has a `status_code` field. To check if an RDB snapshot fails, filter the `status_code` field for the `3 - INTERNAL_ERROR` status.  
`redis.googleapis.com/cluster/persistence/rdb_save_ages` | This metric shows a distribution snapshot age for all nodes across a cluster. In the case of a recovery incident, you can use the metric to view the timeframe for data staleness. Ideally, the distribution has values that have less lag time (or the same lag time) than your snapshot frequency.  
  
#### Node-level metrics

Metric name | Description  
---|---  
`redis.googleapis.com/cluster/node/persistence/rdb_bgsave_in_progress` | This metric indicates whether an RDB background save (`BGSAVE`) is active on a cluster node. A status of `TRUE` means that the `BGSAVE` is active.  
`redis.googleapis.com/cluster/node/persistence/rdb_last_bgsave_status` | This metric indicates whether the `BGSAVE` operation on a cluster node completed or encountered an error. A status of `TRUE` means that the operation completed.  
`redis.googleapis.com/cluster/node/persistence/rdb_saves_count` | This metric tracks the cumulative number of RDB snapshots that are created on a cluster node. You can use the metric to monitor the frequency and success of snapshots on the node.  
`redis.googleapis.com/cluster/node/persistence/rdb_last_save_age` | This metric measures the time, in seconds, that elapsed since the last successful RDB snapshot. You can use the metric to monitor the staleness of RDB persistence data on a cluster node.  
`redis.googleapis.com/cluster/node/persistence/rdb_next_save_time_until` | This metric measures the time remaining, in seconds, until the next RDB snapshot is scheduled to occur on a cluster node. You can use the metric to monitor the schedule of RDB persistence and track when the next automatic snapshot is taken.  
`redis.googleapis.com/cluster/node/persistence/current_save_keys_total` | This metric tracks the total number of keys that are processed in the current RDB save operation on a cluster node.  
  
### AOF persistence metrics

This section lists and describes AOF persistence metrics.

#### Cluster-level metrics

This section lists and describes cluster-level AOF persistence metrics.

Metric name | Description  
---|---  
`redis.googleapis.com/cluster/persistence/aof_fsync_lags` | This metric measures the time difference (or lag) for all nodes in a cluster that passes between writing data to the AOF and when that data is synchronized successfully to durable storage. When the `appendfsync` parameter is set to `everysec`, you can use the metric to assess the health of persistence for the cluster. Ideally, you want the distribution of the lag to have values that have less lag time (or the same time) than the synchronization frequency of the AOF.  
`redis.googleapis.com/cluster/persistence/aof_rewrite_count` | This metric tracks the cumulative number of times that a cluster node triggers an AOF rewrite operation. You can use the metric to diagnose performance issues because a high frequency of AOF rewrites might cause latency spikes or memory pressure on the cluster. The metric has a `status_code` field. To check if AOF rewrites fail, filter this field for the `3 - INTERNAL_ERROR` status.  
  
#### Node-level metrics

This section lists and describes node-level AOF persistence metrics.

Metric name | Description  
---|---  
`redis.googleapis.com/cluster/node/persistence/aof_last_write_status` | This metric shows the status of the last write operation to the AOF file on a cluster node. If the status is `TRUE`, then the write operation is successful. You can use the metric to verify that Memorystore for Redis Cluster persists data successfully.   
`redis.googleapis.com/cluster/node/persistence/aof_last_bgrewrite_status` | This metric shows the status of the last AOF `bgrewrite` operation on a cluster node. If the status is `TRUE`, then the operation is successful.  
`redis.googleapis.com/cluster/node/persistence/aof_fsync_lag` | This metric measures the time difference (or lag) for a cluster node that passes between writing data to the AOF and when that data is synchronized successfully to durable storage. When the `appendfsync` parameter is set to `everysec`, you can use the metric to assess the health of persistence for the node. If the process of synchronizing data takes longer than 1 second, then persistence lags behind the incoming data, which can lead to performance degradation or data loss in a crash scenario.  
`redis.googleapis.com/cluster/node/persistence/aof_rewrites_count` | This metric tracks the cumulative number of times that a cluster node triggers an AOF rewrite operation. You can use the metric to diagnose performance issues. High frequencies of AOF rewrites can lead to increased latency or memory pressure on the cluster. The metric has a `status_code` field. To check if AOF rewrites fail, filter this field for the `3 - INTERNAL_ERROR` status.  
`redis.googleapis.com/cluster/node/persistence/aof_fsync_errors_count` | This metric tracks the cumulative number of times that the AOF `fsync()` system call fails on a cluster node. The metric is applicable only for AOF-enabled clusters where the `appendfsync` parameter is set to either `everysec` or `always`.   
  
### Common persistence metrics

This section lists and describes metrics that are applicable to both AOF and RDB persistence.

#### Node-level metrics

This section lists and describes node-level AOF and RDB persistence metrics.

Metric name | Description  
---|---  
`redis.googleapis.com/cluster/node/persistence/auto_restore_count` |  This metric tracks the cumulative number of times that a cluster node restores from a persistence dump file (AOF or RDB) automatically. The metric has a `status_code` field. To check if restores fail, filter this field for the `3 - INTERNAL_ERROR` status.   
  
#### Sample use cases for persistence metrics

This section describes sample use cases for AOF and RDB persistence metrics.

##### Check if AOF write operations cause latency and memory pressure

Suppose you detect an increase of latency or memory usage on either a cluster or a node within the cluster. If this occurs, then check whether the extra usage is related to AOF persistence.

AOF rewrite operations can trigger transient load spikes. We recommend that you inspect the `aof_rewrites_count` metric because this metric gives you the cumulative count of AOF rewrites over the lifetime of the cluster or cluster node.

Suppose this metric shows that increments in the rewrites count correspond to latency increases. To reduce the frequency of rewrites, either reduce the write rate or increase the shard count.

##### Check if RDB save operations cause latency and memory pressure

Suppose you detect an increase of latency or memory usage on either a cluster or a node within the cluster. If this occurs, then check whether the extra usage is related to RDB persistence.

RDB save operations can trigger transient load spikes. We recommend that you inspect the `rdb_saves_count` metric because this metric gives you the cumulative count of RDB saves over the lifetime of the cluster or cluster node.

Suppose this metric shows that increments in the RDB saves count correspond to latency increases. To lower the frequency of RDB saves, increase the RDB snapshot interval. Also, to reduce the baseline load levels, scale out the cluster.

## Interpret metrics for Memorystore for Redis Cluster

Many metrics belong to the following categories: average, maximum, and total.

We provide _average_ and _maximum_ variations of the same metric so that you can use both metrics to identify hotspots for that metric family.

The _total_ value of the metric is independent from the _average_ and _maximum_ variations of the metric. This value provides insights that are separate and unrelated to the purpose of the variations for hotspots.

### Understand average and maximum metrics

Suppose you compare the values of the `average_keyspace_hits` and `maximum_keyspace_hits` metrics for a cluster. As the difference between the two metrics grows, a greater difference indicates more hotspots for hits in the cluster. A close value between the metrics indicates that hits are distributed more evenly across the nodes in the cluster.

This principle applies to all metrics that have the _average_ and _maximum_ variations of the same metric.

#### Hotspot example

If you compare the values of the `average_keyspace_hits` and `maximum_keyspace_hits` metrics for all shards in a cluster, then you can determine in which shards hotspots occur. For example, suppose shards in a six-shard cluster have the following number of hits:

  * Shard 1 – 2 hits
  * Shard 2 – 2 hits
  * Shard 3 – 2 hits
  * Shard 4 – 2 hits
  * Shard 5 – 2 hits
  * Shard 6 – 8 hits



In this example, the `average_keyspace_hits` metric returns a value of 3, but the `maximum_keyspace_hits` metric returns a value of 8. The hits aren't distributed evenly across the shards in the cluster. Shard 6 is a hotspot because it handles a disproportionately high amount of traffic.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
