---
url: https://docs.cloud.google.com/bigtable/docs/monitoring-instance/
title: Monitoring \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:05.181751+00:00
---

# Monitoring  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/monitoring-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitoring

**Note:** This page includes features that are available only in the Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

You can monitor Bigtable visually, using charts that are available in the [Google Cloud console](https://console.cloud.google.com/), or you can programmatically call the Cloud Monitoring API.

**Note:** If you use a Java client library to access Bigtable, you can enable [client-side metrics](https://docs.cloud.google.com/bigtable/docs/client-side-metrics).

In the Google Cloud console, monitoring data is available in the following places:

  * Bigtable system insights
  * Bigtable instance overview
  * Bigtable cluster overview
  * Bigtable table overview
  * Cloud Monitoring
  * Key Visualizer



The system insights and overview pages provide a high-level view of your Bigtable usage. You can use [Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started) to drill down into your access patterns by row key and troubleshoot specific performance issues.

## Understand resource usage

No matter what tools you use to monitor your instance, it's essential to monitor the CPU, disk, and in-memory tier ([Preview](https://cloud.google.com/products#product-launch-stages)) usage for each cluster in the instance. If a cluster's CPU or disk usage exceeds certain thresholds, the cluster won't perform well, and it might return errors when you try to read or write data.

### CPU usage

The nodes in your clusters use CPU resources to handle reads, writes, and administrative tasks. We recommend that you [enable autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling), which lets Bigtable automatically add and remove nodes to a cluster based on workload. To learn more about how the number of nodes affects a cluster's performance, see [Performance for typical workloads](https://docs.cloud.google.com/bigtable/docs/performance#typical-workloads).

Bigtable reports the following metrics for CPU usage:

Metric | Description  
---|---  
**Average CPU utilization** |  The average CPU utilization across all nodes in the cluster. Includes change stream activity if a change stream is enabled for a table in the instance. In app profile charts, <system> indicates system background activities such as replication and compaction. System background activities are not client-driven. The recommended maximum values provide headroom for brief spikes in usage.   
**CPU utilization of hottest node** |  CPU utilization for the busiest node in the cluster. This metric continues to be provided for continuity, but in most cases you should use the more accurate metric _High-granularity CPU utilization of hottest node_.   
**High-granularity CPU utilization of hottest node** |  A fine-grained measurement of CPU utilization for the busiest node in the cluster.  The hottest node is not necessarily the same node over time and can change rapidly, especially during large batch jobs or table scans.  If the hottest node is frequently above the recommended value, even when your average CPU utilization is reasonable, you might be accessing a small part of your data much more frequently than the rest of your data. 

  * Use the [Key Visualizer tool](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started) to identify hotspots in your table that might be causing spikes in CPU utilization. 
  * Check your [schema design](https://docs.cloud.google.com/bigtable/docs/schema-design) to make sure it supports an even distribution of reads and writes across each table. 

  
**Change stream CPU utilization** |  The average CPU utilization caused by change stream activity across all nodes in the cluster.   
**CPU utilization by app profile, method, and table** |  CPU utilization by app profile, method, and table.  If you observe higher than expected CPU usage for a cluster, use this metric to determine if the CPU usage of a particular app profile, API method, or table is driving the CPU load.   
**Note:** If an instance has one or two clusters and at least one of the instance's app profiles uses multi-cluster routing, the CPU utilization chart shows a recommendation line that is calculated based on multi-cluster routing.

### Disk usage

For each cluster in your instance, Bigtable stores a separate copy of all of the tables in that instance.

Bigtable tracks disk usage in binary units, such as binary gigabytes (GB), where 1 GB is 230 bytes. This unit of measurement is also known as a [gibibyte (GiB)](https://en.wikipedia.org/wiki/Gibibyte).

**Note:** Storage usage metrics can take up to 2 hours to reflect changes in your storage usage.

Bigtable reports the following metrics for disk usage:

Metric | Description  
---|---  
**Storage utilization (bytes)** |  The amount of data stored in the cluster. Change stream usage is not included for this metric.  This value affects your [costs](https://docs.cloud.google.com/bigtable/pricing#storage). Also, as described below, you might need to add nodes to each cluster as the amount of data increases.   
**Storage utilization (% max)** |  The percentage of the cluster's storage capacity that is being used. The capacity is based on the number of nodes in your cluster. Change stream usage is not included for this metric.  In general, do not use more than 70% of the hard limit on total storage, so you have room to add more data. If you do not plan to add significant amounts of data to your instance, you can use up to 100% of the hard limit.  **Important** : If any cluster in an instance exceeds the hard limit on the amount of storage per node, writes to all clusters in that instance will fail until you [add nodes to each cluster that is over the limit](https://docs.cloud.google.com/bigtable/docs/modifying-instance#nodes). Also, if you try to remove nodes from a cluster, and the change would cause the cluster to exceed the hard limit on storage, Bigtable will deny the request. If you are using more than the recommended percentage of the storage limit, add nodes to the cluster. You can also delete existing data, but [deleted data takes up _more_ space, not less, until a compaction occurs](https://docs.cloud.google.com/bigtable/docs/overview#mutations-deletions).  For details about how this value is calculated, see [Storage utilization per node](https://docs.cloud.google.com/bigtable/quotas#storage-per-node).   
**Change stream storage utilization (bytes)** |  The amount of storage consumed by change stream records for tables in the instance. This storage does not count toward the total storage utilization. You are charged for change stream storage, but it is not included in the calculation of storage utilization (% max).   
**Disk load** |  For HDD clusters, the percentage your cluster is using of the maximum possible bandwidth for HDD reads. For SSD clusters with [tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) enabled, the percentage your cluster is using of the maximum possible throughput for the [infrequent access tier](https://docs.cloud.google.com/bigtable/docs/tiered-storage#infrequent-access-storage).  If this value is frequently at 100%, you might experience increased latency. Add nodes to the cluster to reduce the disk load percentage.   
  
### In-memory tier usage

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Bigtable tracks in-memory tier throughput in reads per second. One read per second is an equivalent of a 1 KiB point read. If your workload requires higher throughput than the base capacity, Bigtable automatically scales vertically. For more information about throughput limits and vertical scaling, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance#typical-workloads). For more information about the in-memory tier, see [In-memory tier overview](https://docs.cloud.google.com/bigtable/docs/in-memory-overview).

Bigtable reports the following metrics for in-memory usage:

Metric | Description  
---|---  
**In-memory storage capacity** |  Memory layer storage capacity in bytes.  
**In-memory max request units** |  Maximum number of reads per second used in a 5 minute window.  
**In-memory request unit count** |  The reads per second usage for read requests that attempt to use the memory layer.  
**In-memory read request count** |  Number of read requests for a table that went to the memory layer, broken down by whether the memory read was successful.  
**In-memory read latencies** |  Distribution of server read request latencies for a table that attempted to reach the memory layer.  
**In-memory hit ratio** |  Ratio of number of read requests that successfully read from the memory layer compared to all memory eligible read requests.  
**In-memory ineligible reason count** |  Number of requests that were ineligible for the memory layer, broken down by the reason.  
  
### Compaction and replicated instances

Storage metrics reflect the data size on disk as of the last compaction. Because compaction happens on a rolling basis over the course of a week, storage usage metrics for a cluster might sometimes temporarily be different from metrics for other clusters in the instance. Observable impacts of this include the following:

  * A new cluster that has recently been added to an instance might temporarily show 0 bytes of storage even though all data has successfully been replicated to the new cluster.

  * A table might be a different size in each cluster, even when replication is working properly.

  * Storage usage metrics might be different in each cluster, even after replication has finished and no writes have been sent for a few days. The internal storage implementation, including how data is divided and stored in a distributed manner, can be different for each cluster, causing the actual usage of storage to differ.




## Instance overview

The instance overview page provides a summary of the health and performance of your instance.

### Instance metrics

The following table describes the values for the key metrics of each cluster in your instance:

Metric | Description  
---|---  
**CPU utilization average** |  The average CPU utilization across all nodes in the cluster. Includes change stream activity if a change stream is enabled for a table in the instance. In app profile charts, <system> indicates system background activities such as replication and compaction. System background activities are not client-driven.  
**CPU utilization of hottest node** |  CPU utilization for the busiest node in the cluster. This metric continues to be provided for continuity, but in most cases you should use the more accurate metric _High-granularity CPU utilization of hottest node_.   
**High-granularity CPU utilization of hottest node** |  A fine-grained measurement of CPU utilization for the busiest node in the cluster.  The hottest node is not necessarily the same node over time and can change rapidly, especially during large batch jobs or table scans.  Exceeding the recommended maximum for the busiest node can cause latency and other issues for the cluster.   
**Rows read** |  The number of rows read per second.   
**Rows written** |  The number of rows written per second.   
**Read throughput** |  The number of bytes per second of response data sent. This metric refers to the full amount of data that is returned after filters are applied.   
**Write throughput** |  The number of bytes per second that were received when data was written.   
**System error rate** |  The percentage of all requests that failed on the Bigtable server side.   
**Replication latency for input** |  The highest amount of time at the 99th percentile, in seconds, for a write to another cluster to be replicated to this cluster.   
**Replication latency for output** |  The highest amount of time at the 99th percentile, in seconds, for a write to this cluster to be replicated to another cluster.   
  
To see an overview of these key metrics:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose metrics you want to view. The Google Cloud console displays the current metrics for your instance's clusters.




### Alerts and warnings

In addition to the metrics listed in the earlier table, if you enabled [tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) ([Preview](https://cloud.google.com/products#product-launch-stages)) for any tables in the instance, you might see a warning banner stating that infrequent access storage impacts SSD capacity on one or more clusters.

## Cluster overview

Use the cluster overview page to understand the current and past status of an individual cluster.

The cluster overview page displays charts showing the following metrics for each cluster:

Metric | Description  
---|---  
**Number of nodes** | The number of nodes in use for the cluster at a given time.  
**Maximum node count target** | The maximum number of nodes that Bigtable will scale the cluster up to when autoscaling is enabled. This metric is visible only when autoscaling is enabled for the cluster. You are able to change this value on the **Edit cluster** page.  
**Minimum node count target** | The minimum number of nodes that Bigtable will scale the cluster down to when autoscaling is enabled. This metric is visible only when autoscaling is enabled for the cluster. You are able to change this value on the **Edit cluster** page.  
**Recommended number of nodes for CPU target** | The number of nodes that Bigtable recommends for the cluster based on the CPU utilization target that you set. This metric is visible only when autoscaling is enabled for the cluster. If this number is higher than the maximum node count target, consider raising your CPU utilization target or increasing the maximum number of nodes for the cluster. If this number is lower than the minimum number of nodes, the cluster might be overprovisioned for your usage, and you should consider lowering the minimum.   
**Recommended number of nodes for storage target** | The number of nodes that Bigtable recommends for the cluster based on the built-in storage utilization target. This metric is visible only when autoscaling is enabled for the cluster. If this number is higher than the maximum node count target, consider increasing the maximum number of nodes for the cluster.  
**CPU utilization** |  The average CPU utilization across all nodes in the cluster. Includes change stream activity if a change stream is enabled for a table in the instance. In app profile charts, <system> indicates system background activities such as replication and compaction. System background activities are not client-driven.  
**Storage utilization** |  The amount of data stored in the cluster. Change stream usage is not included for this metric.  This metric reflects the fact that Bigtable compresses your data when it is stored.   
**In-memory tier metrics** | Enterprise Plus only. Includes charts for hit ratio, read latency, and request unit (RU) usage for the cluster.  
  
To view a cluster's overview page, do the following:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose metrics you want to view. 

  3. Go to the section that follows the section that shows the current status of some of the cluster's metrics.

  4. Click the cluster ID to open the cluster's **Cluster overview** page.




### Logs

The **Logs** chart displays system event log entries for the cluster. System event logs are generated only for clusters that use autoscaling. To learn additional ways to view Bigtable audit logs, see [Audit logging](https://docs.cloud.google.com/bigtable/docs/audit-logging).

## Table overview

Use the table overview page to understand the current and past status of an individual table.

The table overview page displays charts showing the following metrics for the table. Each chart shows a separate line for each cluster that the table is in.

Metric | Description  
---|---  
**Storage utilization (bytes)** | The percentage of the cluster's storage capacity that is being used by the table. The capacity is based on the number of nodes in the cluster. Tables with [tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) ([Preview](https://cloud.google.com/products#product-launch-stages)) enabled additionally show the breakdown of SSD and infrequent access storage utilization over time.  For details about how this value is calculated, see [Storage utilization per node](https://docs.cloud.google.com/bigtable/quotas#storage-per-node).   
**CPU utilization** |  The average CPU utilization across all nodes in the cluster. Includes change stream activity if a change stream is enabled for a table in the instance. In app profile charts, <system> indicates system background activities such as replication and compaction. System background activities are not client-driven.  
**Read latency** | The time for a read request to return a response. Measurement of read latency begins when Bigtable receives the request and ends when the last byte of data is sent to the client. For requests for large amounts of data, read latency can be affected by the client's ability to consume the response.   
**Write latency** | The time for a write request to return a response.  
**Rows read** |  The number of rows read per second.  This metric provides a more useful view of Bigtable's overall throughput than the number of read requests, because a single request can read a large number of rows.   
**Rows written** |  The number of rows written per second.  This metric provides a more useful view of Bigtable's overall throughput than the number of write requests, because a single request can write a large number of rows.   
**Read requests** | The number of random reads and scan requests per second.  
**Write requests** | The number of write requests per second.  
**Read throughput** |  The number of bytes per second of response data sent. This metric refers to the full amount of data that is returned after filters are applied.   
**Write throughput** |  The number of bytes per second that were received when data was written.   
**Automatic failovers** |  The number of requests that were automatically rerouted from one cluster to another due to a failover scenario, such as a brief outage or delay. Automatic rerouting can occur if an app profile uses multi-cluster routing. This chart does not include manually rerouted requests.  
  
The table overview page also shows the table's replication state in each cluster in the instance. For each cluster, the page displays the following:

  * Status
  * Cluster ID
  * Zone
  * The amount of cluster storage used by the table
  * Encryption key and key status
  * Date of the latest backup of the selected table
  * A link to the **Edit cluster** page.



To view a table's overview page, do the following:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose metrics you want to view. 

  3. In the left pane, click **Tables**. The Google Cloud console displays a list of all the tables in the instance.

  4. Click a table ID to open the table's **Table overview** page.




## Monitor performance over time

Use your Bigtable instance's system insights page to understand the past performance of your instance. You can analyze the performance of each cluster, and you can break down the metrics for different types of Bigtable resources. Charts can display a period ranging from the past 1 hour to the past 6 weeks.

### System insights charts for Bigtable resources

The Bigtable system insights page provides charts for the following types of Bigtable resources:

  * Instances
  * Tables
  * Application profiles
  * Replication



Charts on the system insights page show the following metrics:

Metric | Available for | Description  
---|---|---  
**CPU utilization** | Instances  
Tables  
App profiles |  The average CPU utilization across all nodes in the cluster. Includes change stream activity if a change stream is enabled for a table in the instance. In app profile charts, <system> indicates system background activities such as replication and compaction. System background activities are not client-driven.  
**High-granularity CPU utilization (hottest node)** | Instances |  A fine-grained measurement of CPU utilization for the busiest node in the cluster.  The hottest node is not necessarily the same node over time and can change rapidly, especially during large batch jobs or table scans.  Exceeding the recommended maximum for the busiest node can cause latency and other issues for the cluster.   
**Data Boost serverless processing units (SPUs)** | Instances | Billable Data Boost compute usage measured in SPU-seconds.  
**Read latency** |  Instances  
Tables  
App profiles  |  The time for a read request to return a response. Measurement of read latency begins when Bigtable receives the request and ends when the last byte of data is sent to the client. For requests for large amounts of data, read latency can be affected by the client's ability to consume the response.   
**SQL read latency** |  Instances  
App profiles  |  The time for a SQL read request to return a response. Measurement of SQL read latency begins when Bigtable receives the request and ends when the last byte of data is sent to the client. For requests for large amounts of data, SQL read latency can be affected by the client's ability to consume the response.   
**Write latency** |  Instances  
Tables  
App profiles  |  The time for a write request to return a response.  
**Client-side read latency** |  Instances  
Tables  
App profiles  |  The total end-to-end latency across all RPC attempts associated with a Bigtable operation. Measures the operation's round trip from the client to Bigtable and back to the client and includes all retries.  
**Client-side SQL read latency** |  Instances  
Tables  
App profiles  |  The total end-to-end latency across all RPC attempts associated with a Bigtable operation. Measures the operation's round trip from the client to Bigtable and back to the client and includes all retries. For `ExecuteQuery` requests, the operation latencies include the application processing time for each returned message.  
**Client-side write latency** |  Instances  
Tables  
App profiles  |  The total end-to-end latency across all RPC attempts associated with a Bigtable operation. Measures the operation's round trip from the client to Bigtable and back to the client and includes all retries.  
**Client-side read attempt latency** |  Instances  
Tables  
App profiles  |  The latencies of a client read RPC attempt. Under normal circumstances, this value is identical to `operation_latencies`. If the client receives transient errors, however, then `operation_latencies` is the sum of all `attempt_latencies` and the exponential delays.  
**Client-side SQL read attempt latency** |  Instances  
Tables  
App profiles  |  The latencies of a client SQL read RPC attempt. Under normal circumstances, this value is identical to `operation_latencies`. If the client receives transient errors, however, then `operation_latencies` is the sum of all `attempt_latencies` and the exponential delays.  
**Client-side write attempt latency** |  Instances  
Tables  
App profiles  |  The latencies of a client write RPC attempt. Under normal circumstances, this value is identical to `operation_latencies`. If the client receives transient errors, however, then `operation_latencies` is the sum of all `attempt_latencies` and the exponential delays.  
**User error rate** | Instances |  The rate of errors caused by the content of a request, as opposed to errors on the Bigtable server side. The user error rate includes the following [status codes](https://docs.cloud.google.com/bigtable/docs/status-codes): 

  * INVALID_ARGUMENT
  * NOT_FOUND
  * PERMISSION_DENIED
  * RESOURCE_EXHAUSTED
  * OUT_OF_RANGE

User errors are typically caused by a configuration issue, such as a request that specifies the wrong cluster, table, or app profile.  **Note:** To view this chart, you must group the system insights data by instance. In the **View metrics for** drop-down list, select **Instance**. Then, under **Group by** , click **Instance**.   
**System error rate** |  Instances  |  The percentage of all requests that failed on the Bigtable server side. The system error rate includes the following [status codes](https://docs.cloud.google.com/bigtable/docs/status-codes): 

  * UNKNOWN
  * ABORTED
  * UNIMPLEMENTED
  * INTERNAL
  * UNAVAILABLE

  
**Automatic failovers** |  Instances  
Tables  
App profiles  |  The number of requests that were automatically rerouted from one cluster to another due to a failover scenario, such as a brief outage or delay. Automatic rerouting can occur if an app profile uses multi-cluster routing. This chart does not include manually rerouted requests.  
**SQL automatic failovers** |  Instances  
Tables  
App profiles  |  The number of SQL requests that were automatically rerouted from one cluster to another due to a failover scenario, such as a brief outage or delay. Automatic rerouting can occur if an app profile uses multi-cluster routing. This chart does not include manually rerouted requests.  
**Storage utilization (bytes)** |  Instances  
Tables  |  The amount of data stored in the cluster. Change stream usage is not included for this metric.  This metric reflects the fact that Bigtable compresses your data when it is stored.   
**Storage utilization (% max)** | Instances |  The percentage of the cluster's storage capacity that is being used. The capacity is based on the number of nodes in your cluster. Change stream usage is not included for this metric.  For details about how this value is calculated, see [Storage utilization per node](https://docs.cloud.google.com/bigtable/quotas#storage-per-node).   
**Disk load** | Instances |  For HDD clusters, the percentage your cluster is using of the maximum possible bandwidth for HDD reads. For SSD clusters with [tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) enabled, the percentage your cluster is using of the maximum possible throughput for the [infrequent access tier](https://docs.cloud.google.com/bigtable/docs/tiered-storage#infrequent-access-storage).   
**In-memory tier storage capacity** | Instances  
Clusters | Enterprise Plus only. Memory layer storage capacity in bytes.  
**In-memory tier max request units** | Instances  
Clusters | Enterprise Plus only. Maximum number of Request-Units per second used in a 5 minute window.  
**In-memory tier request unit count** | Instances  
Clusters  
Tables  
App profiles | Enterprise Plus only. The Request-Unit usage for read requests that attempt to use the memory layer.  
**In-memory tier read request count** | Instances  
Clusters  
Tables  
App profiles | Enterprise Plus only. Number of read requests for a table that went to the memory layer, broken down by whether the memory read was successful.  
**In-memory tier read latency** | Instances  
Clusters  
Tables  
App profiles | Enterprise Plus only. Distribution of server read request latencies for a table that attempted to reach the memory layer.  
**In-memory tier hit ratio** | Instances  
Clusters  
Tables  
App profiles | Enterprise Plus only. Ratio of number of read requests that successfully read from the memory layer compared to all memory eligible read requests.  
**In-memory tier ineligible reason count** | Instances  
Clusters  
Tables  
App profiles | Enterprise Plus only. Number of requests that were ineligible for the memory layer, broken down by the reason.  
**Rows read** |  Instances  
Tables  
App profiles  |  The number of rows read per second.  This metric provides a more useful view of Bigtable's overall throughput than the number of read requests, because a single request can read a large number of rows.   
**Rows written** |  Instances  
Tables  
App profiles  |  The number of rows written per second.  This metric provides a more useful view of Bigtable's overall throughput than the number of write requests, because a single request can write a large number of rows.   
**Read requests** |  Instances  
Tables  
App profiles  | The number of random reads and scan requests per second.  
**Write requests** |  Instances  
Tables  
App profiles  | The number of write requests per second.  
**Read throughput** |  Instances  
Tables  
App profiles  |  The number of bytes per second of response data sent. This metric refers to the full amount of data that is returned after filters are applied.   
**Write throughput** |  Instances  
Tables  
App profiles  |  The number of bytes per second that were received when data was written.   
**Write throughput** |  Instances  
Tables  
App profiles  |  The number of bytes per second that were received when data was written.   
**Node count** | Instances | The number of nodes in the cluster.  
**Data Boost traffic eligibility** | App profiles | Current Bigtable requests that are eligible and ineligible for Data Boost.  
**Data Boost traffic ineligible reasons** | App profiles | Reasons that current traffic is ineligible for Data Boost.  
  
To view metrics for these resources:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose metrics you want to view. 

  3. In the left pane, click **System insights**. The Google Cloud console displays a series of charts for the instance, as well as a tabular view of the instance's metrics. By default, the Google Cloud console shows metrics for the past hour, and it shows separate metrics for each cluster in the instance.

To view all of the charts, scroll through the pane where the charts are displayed.

To view metrics at the table level, click **Tables**.

To view metrics for individual app profiles, click **Application Profiles**.

To view combined metrics for the instance as a whole, find the **Group by** section above the charts, then click **Instance**.

To view metrics for a longer period of time, click the arrow next to **1 Hour**. Choose a pre-set time range or enter a custom time range, then click **Apply**.


**Important:** When you group by **Cluster** , you might sometimes see requests tagged with an **< unspecified>** cluster ID. This tag is used for requests that were unable to reach a cluster, and generally represents only a very small percentage of requests.

### Charts for replication

The system insights page provides a chart that shows replication latency over time. You can view the average latency for replicating writes at the 50th, 99th, and 100th percentiles.

To view the replication latency over time:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose metrics you want to view. 

  3. In the left pane, click **System insights**. The page opens on the **Instance** tab.

  4. Click the **Replication** tab. The Google Cloud console displays replication latency over time. By default, the Google Cloud console shows replication latency for the past hour.

To toggle between latency charts grouped by table or by cluster, use the **Group by** menu.

To change which percentile to view, use the **Percentile** menu.

To view metrics for a longer period of time, click the arrow next to **1 Hour**. Choose a pre-set time range or enter a custom time range, then click **Apply**.




## Required roles

To get the permissions that you need to view or modify insights dashboards, including custom dashboards, ask your administrator to grant you the following IAM roles on the project: 

  * To create and edit custom dashboards: [Monitoring Dashboard Configuration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.dashboardEditor) (`roles/monitoring.dashboardEditor`) 
  * To open and view Metrics Explorer charts: [Monitoring Dashboard Configuration Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.dashboardViewer) (`roles/monitoring.dashboardViewer`) 
  * To create and edit Metrics Explorer alerts: [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view or modify insights dashboards, including custom dashboards. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view or modify insights dashboards, including custom dashboards:

  * To create custom dashboards: `monitoring.dashboards.create`
  * To edit custom dashboards: `monitoring.dashboards.update`
  * To view custom dashboards: `monitoring.dashboards.get, monitoring.dashboards.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Customize the system insights dashboard

The system insights dashboard is a predefined dashboard that you can customize to display the information that is most important to you. You can add new charts, change the layout, and filter the data to focus on specific resources.

Changes to the system insights dashboard are non-destructive, and can be reset by setting the _dashboard selector_ to **Predefined**.

### Modify the dashboard

To modify the dashboard, click edit **Customize dashboards**. The following options are available to you:

  * **Add a widget:** In the dashboard toolbar, click add **Add widget** , select the widget you want to add, and then configure it.
  * **Edit a widget:** Hover over a widget to show its toolbar, then click edit **Edit**. You can change the widget's type and customize the data it displays.
  * **Clone a widget:** Hover over a widget to show its toolbar, click more_vert **More chart options** , then **Clone widget**.
  * **Delete a widget:** Hover over a widget to show its toolbar, click more_vert **More chart options** , then **Delete widget**.
  * **Change the layout:** You can drag widgets to reposition them and drag their corners to resize them.
  * **Name the custom view:** You can set the custom view name in the **Custom view name** box.
  * **Save the dashboard:** You can save the custom view by clicking save **Save**. You can also quit without saving by clicking **Exit edit mode**.



## Monitor with Cloud Monitoring

Bigtable exports [usage metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-bigtable) to [Cloud Monitoring](https://docs.cloud.google.com/monitoring). You can use these metrics in a variety of ways:

  * Monitor programmatically using the Cloud Monitoring API.
  * Monitor visually in the Metrics Explorer.
  * Set up [alerting policies](https://docs.cloud.google.com/monitoring/alerts).
  * Add Bigtable usage metrics [to a custom dashboard](https://docs.cloud.google.com/monitoring/charts#create_a_new_chart).
  * Use a graphing library, such as [Matplotlib](https://matplotlib.org/) for Python, to plot and analyze the usage metrics for Bigtable.



To view usage metrics in the Metrics Explorer:

  1. Open the Monitoring page in the Google Cloud console.

[Open the Monitoring page](https://console.cloud.google.com/monitoring)

If you are prompted to choose an account, choose the account that you use to access Google Cloud.

  2. Click **Resources** , then click **Metrics Explorer**.

  3. Under **Find resource type and metric** , type `bigtable`. A list of Bigtable resources and metrics appears.

  4. Click a metric to view a chart for that metric.




For additional information about using Cloud Monitoring, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

For a complete list of Bigtable metrics, see [Metrics](https://docs.cloud.google.com/bigtable/docs/metrics).

## Create a storage utilization alert

You can set up an alert to notify you when your Bigtable cluster exceeds a specified threshold. For more information about determining your target storage utilization, see Disk usage.

To create an alerting policy that triggers when the storage utilization for your [Bigtable](https://docs.cloud.google.com/bigtable/docs) cluster is above a recommended threshold, such as 70%, use the following settings.

#### Steps to create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).

To create an alerting policy, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the resource, metric, and filters, expand the **Select a metric** menu and then use the values in the **New condition** table: 
     1. Optional: To limit the menu to relevant entries, enter the resource or metric name in the filter bar. 
     2. Select a **Resource type**. For example, select **VM instance**.
     3. Select a **Metric category**. For example, select **instance**.
     4. Select a **Metric**. For example, select **CPU Utilization**.
     5. Select **Apply**.
  5. Click **Next** and then configure the alerting policy trigger. To complete these fields, use the values in the **Configure alert trigger** table. 
  6. Click **Next**.
  7. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.

To be notified when alerts are opened and closed, check **Notify on alert closure**. By default, notifications are sent only when alerts are opened.

  8. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  9. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  10. Click **Alert name** and enter a name for the alerting policy.
  11. Click **Create Policy**.

**New condition**  
Field |   
Value  
---|---  
**Resource and Metric** | In the **Resources** menu, select **Cloud Bigtable Cluster**.  
In the **Metric categories** menu, select **Cluster**.  
In the **Metrics** menu, select **Storage utilization**.  
  
(The metric.type is `bigtable.googleapis.com/cluster/storage_utilization`).   
**Filter** | `cluster = YOUR_CLUSTER_ID`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Condition triggers if** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** |  70   
**Retest window** | `10 minutes`  
  
## What's next

  * Find out how to [troubleshoot issues with Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started).
  * Read about [client-side metrics](https://docs.cloud.google.com/bigtable/docs/client-side-metrics).
  * Try the [Cloud Monitoring quickstart](https://docs.cloud.google.com/monitoring/monitor-compute-engine-virtual-machine).
  * Learn about [creating alerts based on Bigtable metrics](https://docs.cloud.google.com/monitoring/alerts).
  * Read about [investigating performance with AI assistance](https://docs.cloud.google.com/bigtable/docs/investigate-performance-with-ai).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
