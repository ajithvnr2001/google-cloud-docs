---
url: https://docs.cloud.google.com/bigtable/docs/performance/
title: Understand performance \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:05.064948+00:00
---

# Understand performance  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand performance

This page describes the approximate performance that Bigtable can provide under optimal conditions, factors that can affect performance, and tips for testing and troubleshooting Bigtable performance issues.

## Performance for typical workloads

Bigtable delivers highly predictable performance that is linearly scalable. When you avoid the [causes of slower performance](https://docs.cloud.google.com/bigtable/docs/performance#slower-perf) described on this page, each Bigtable node can provide the following approximate throughput, depending on which type of storage the cluster uses:

Storage tier | Reads |  | Writes |  | Scans  
---|---|---|---|---|---  
**In-memory tier ([Preview](https://cloud.google.com/products#product-launch-stages))** | up to 120,000 rows per second1 | **or** | up to 10,000 rows per second2 |  | N/A  
**SSD** | up to 17,000 rows per second | **or** | up to 14,000 rows per second | **or** | up to 220 MBps  
**HDD** | up to 500 rows per second | **or** | up to 10,000 rows per second | **or** | up to 180 MBps  
**Infrequent access storage** | up to 100 rows per second | **or** | up to 10,000 rows per second | **or** | up to 36 MBps  
  
These estimates assume each row contains 1 KB. 

1 An Enterprise Plus node includes 40,000 rows per second and can scale vertically to 120,000 rows per second per node in increments of 40,000. For more information, see In-memory tier.

2 High write of rows per second to data in the in-memory tier can impact write throughput.

In general, a cluster's performance scales linearly as you add nodes to the cluster. For example, if you create an SSD cluster with 10 nodes, the cluster can support up to 140,000 rows per second for a typical read-only or write-only workload without the in-memory tier enabled. With the in-memory tier enabled, the cluster can support read throughput of up to 1.2 million rows per second.

**Note:** These performance numbers are **estimates only** , and they reflect a read-only or write-only workload. Bigtable performance is highly dependent on workload, schema design, and dataset characteristics. These performance numbers can help as a starting point when you're estimating your compute needs, but they shouldn't be used for exact cluster sizing or for cost estimates.

## Plan your Bigtable capacity

When planning your Bigtable clusters, decide whether you want to optimize for latency or throughput. For example, for a batch data processing job, you might care more about throughput and less about latency. In contrast, for an online service that serves user requests, you might prioritize lower latency over throughput. You can achieve the numbers in the [Performance for typical workloads](https://docs.cloud.google.com/bigtable/docs/performance#typical-workloads) section when you optimize for throughput.

### In-memory tier

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

With the in-memory tier enabled, each node includes 40,000 rows per second. Adding nodes horizontally increases the total cluster capacity. In addition, each node can scale vertically up to a maximum of 120,000 rows per second per node to support in-memory read throughput. When the vertical scaling limit is reached, Bigtable autoscaling adds additional nodes to scale horizontally. A cluster with manual scaling supports in-memory vertical scaling until throughput capacity is reached. Vertical scaling beyond the base 40,000 rows per second is billed by applying a multiplier to the node's hourly cost. For more information, see [Pricing](https://cloud.google.com/bigtable/pricing).

Each in-memory node includes 8 GB of storage capacity. While throughput can scale vertically, storage capacity remains fixed per node. However, horizontal scaling adds an additional 8 GB of memory for each new node. Because storage doesn't increase during vertical scaling, the miss rate of a workload may rise when a node scales its in-memory throughput vertically.

### CPU utilization

In almost all cases, we recommend that you use autoscaling, which lets Bigtable add or remove nodes based on usage. For more information, see [Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling).

Use the following guidelines when configuring your autoscaling targets or if you choose manual node allocation. These guidelines apply regardless of the number of clusters your instance has. For a cluster with manual node allocation, you must monitor the cluster's CPU utilization with the goal of keeping CPU utilization below these values for optimal performance.

**Optimization goal** | **Maximum CPU utilization**  
---|---  
Throughput | 90%  
Latency | 60%  
  
For more information on monitoring, see [Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).

### Storage utilization

Storage is another consideration in capacity planning. The storage capacity of a cluster is determined by the storage type and the number of nodes in the cluster. When the amount of data stored in a cluster increases, Bigtable optimizes storage by distributing data across all nodes in the cluster.

You can determine the storage usage per node by dividing the cluster's [storage utilization (bytes)](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#disk) by the number of nodes in the cluster. For example, consider a cluster that has three HDD nodes and 9 TB of data. Each node stores about 3 TB, which is 18.75% of the HDD storage per node limit of 16 TB.

When storage utilization increases, workloads can experience an increase in query processing latency even if the cluster has enough nodes to meet overall CPU needs. This is because the higher the storage per node, the more background work such as indexing is required. The increase in background work to handle more storage can result in higher latency and lower throughput.

Start with the following when configuring your autoscaling settings. If you choose manual node allocation, monitor the cluster's storage utilization and add or remove nodes to maintain the following.

**Optimization goal** | **Maximum storage utilization**  
---|---  
Throughput | 70%  
Latency | 60%  
  
For more information, see [Storage per node](https://docs.cloud.google.com/bigtable/quotas#storage-per-node).

### Run your workloads against Bigtable

Always run your workloads against a Bigtable cluster when doing capacity planning to determine the best resource allocation for your applications.

Google's _PerfKit Benchmarker_ uses [YCSB](https://ycsb.site) to benchmark cloud services. You can follow the [PerfKitBenchmarker tutorial for Bigtable](https://github.com/GoogleCloudPlatform/PerfKitBenchmarker/tree/master/tutorials/bigtable_walkthrough) to create tests for your workloads. When doing so, tune the parameters in the benchmarking config YAML files to ensure the generated benchmark reflects the following production characteristics:

  * Total size of your table (proportional, but at least 100 GB).
  * Row data shape ([row key size, number of columns, row data sizes](https://docs.cloud.google.com/bigtable/docs/schema-design#general-concepts), etc.)
  * Data access pattern (row key distribution)
  * Mixture of reads against writes



Refer to Testing performance with Bigtable for more best practices.

## Causes of slower performance

The following factors can cause Bigtable to perform more slowly than estimated:

  * **You read a large number of non-contiguous row keys or row ranges in a single read request.** Bigtable scans the table and reads the requested rows sequentially. This lack of parallelism affects _overall_ latency, and reads hitting a [hot node](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cpu) can increase _tail_ latency. See [Reads and performance](https://docs.cloud.google.com/bigtable/docs/reads#performance) for details.
  * **Your table's schema is not designed correctly.** To get good performance from Bigtable, it's essential to design a schema that makes it possible to distribute reads and writes evenly across each table. Additionally, hotspots in one table can affect the performance of other tables in the same instance. See [Schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design) for more information.
  * **The rows in your Bigtable table contain large amounts of data.** The performance estimates assume that each row contains 1 KB of data. You can read and write larger amounts of data per row, but increasing the amount of data per row will also reduce the number of rows per second.
  * **The rows in your Bigtable table contain a very large number of cells.** It takes time for Bigtable to process each cell in a row. Also, each cell adds some overhead to the amount of data that's stored in your table and sent over the network. For example, if you're storing 1 KB (1,024 bytes) of data, it's much more space-efficient to store that data in a single cell, rather than spreading the data across 1,024 cells that each contain 1 byte. If you split your data across more cells than necessary, you might not get the best possible performance. If rows contain a large number of cells because columns contain multiple timestamped versions of data, consider [keeping only the most recent value](https://docs.cloud.google.com/bigtable/docs/gc-latest-value). Another option for an existing table is to send a deletion for all previous versions with each rewrite.
  * **The cluster doesn't have enough nodes.** A cluster's nodes provide compute for the cluster to handle incoming reads and writes, keep track of storage, and perform maintenance tasks such as compaction. You need to make sure that your cluster has enough nodes to satisfy the recommended limits for both compute and storage. Use the [monitoring tools](https://docs.cloud.google.com/bigtable/docs/monitoring-instance) to check whether the cluster is overloaded.

    * **Compute** \- If your Bigtable cluster's CPU is overloaded, adding more nodes improves performance by spreading the workload across more nodes.
    * **Storage** \- If your [storage usage per node](https://docs.cloud.google.com/bigtable/quotas#storage-per-node) is higher than recommended, then add more nodes to maintain optimal latency and throughput, even if the cluster has enough CPU to process requests. This is because increasing the amount of storage per node increases the amount of background maintenance work per node. For more information, see Trade-offs between storage usage and performance.
  * **The Bigtable cluster was scaled up or scaled down recently.** After autoscaling increases the number of nodes in a cluster, it can take up to 20 minutes under load before performance significantly improves. Bigtable scales cluster nodes based on the load they experience.

When you decrease the number of nodes in a cluster to scale down, try not to reduce the cluster size by more than 10% in a 10-minute period to minimize latency spikes.

  * **The Bigtable cluster uses HDD disks.** In most cases, your cluster should use SSD disks, which have significantly better performance than HDD disks. See [Choosing between SSD and HDD storage](https://docs.cloud.google.com/bigtable/docs/choosing-ssd-hdd) for details.

  * **There are issues with the network connection.** Network issues can reduce throughput and cause reads and writes to take longer than usual. In particular, you might see issues if your clients are not running in the same [zone](https://docs.cloud.google.com/bigtable/docs/locations) as your Bigtable cluster, or if your clients run outside of Google Cloud.

  * **You are using replication but your application is using an out-of-date client library.** If you observe increased latency after enabling replication, make sure the Cloud Bigtable client library that your application is using is up to date. Earlier versions of the client libraries might not be optimized to support replication. See [Cloud Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries) to find your client library's GitHub repository, where you can check the version and upgrade if you need to.

  * **You enabled replication but didn't add more nodes to your clusters.** In an instance that uses replication, each cluster must handle the work of replication in addition to the load it receives from applications. Underprovisioned clusters can cause increased latency. You can verify this by checking the instance's [CPU usage](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cpu) charts in the Google Cloud console.




Because different workloads can cause performance to vary, perform tests with your workloads to obtain the most accurate benchmarks.

### Cold starts and low QPS

Cold starts and low QPS can increase latency. Bigtable performs best with large tables that are frequently accessed. For this reason, if you start sending requests after a period of no usage (a cold start), you might observe high latency while Bigtable reestablishes connections. Latency is also higher when QPS is low.

If your QPS is low, or if you know you will sometimes send requests to a Bigtable table after a period of inactivity, try the following strategies to keep your connection warm and prevent high latency.

  * Send a low rate of artificial traffic to the table at all times.
  * [Configure the connection pool to help ensure that steady QPS keeps the pool active.](https://docs.cloud.google.com/bigtable/docs/configure-connection-pools)



During periods of low QPS, the number of errors that Bigtable returns is more relevant than the percentage of operations that return an error.

**Cold start at client initialization time.** If you are using a version of the Cloud Bigtable client for Java that is earlier than version 2.17.1, you can [enable channel refreshing](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.Builder#com_google_cloud_bigtable_data_v2_BigtableDataSettings_Builder_setRefreshingChannel_boolean_). In later versions, channel refreshing is enabled by default. Channel refreshing does two things:

  * When the client initializes, it prepares the channel before sending the first requests.
  * The server disconnects long-lived connections every hour. Channel priming preemptively replaces expiring channels.



However, this doesn't keep the channel alive when there are periods of inactivity.

## How Bigtable optimizes your data over time

To store the underlying data for each of your tables, Bigtable shards the data into multiple tablets, which can be moved between nodes in your Bigtable cluster. This storage method enables Bigtable to use two strategies for optimizing data over time:

  1. Bigtable stores roughly the same amount of data on each Bigtable node.
  2. Bigtable distributes reads and writes equally across all Bigtable nodes.



Sometimes these strategies conflict. For example, if one tablet's rows are read extremely frequently, Bigtable might store that tablet on its own node, even if this causes some nodes to store more data than others.

As part of this process, Bigtable might split a tablet into two or more smaller tablets to reduce its size or to isolate hot rows within an existing tablet.

The following sections explain each of these strategies in more detail.

### Distributing the amount of data across nodes

As you write data to a Bigtable table, Bigtable shards the table's data into tablets. Each tablet contains a contiguous range of rows within the table.

If you have written less than several GB of data to the table, Bigtable stores all tablets on a single node within your cluster:

![A cluster with four tablets on a single node.](https://docs.cloud.google.com/bigtable/img/redistributing-volume-initial.png)

As more tablets accumulate, Bigtable moves some to other nodes in the cluster to balance the amount of data more evenly across the cluster:

![Additional tablets are distributed across multiple nodes.](https://docs.cloud.google.com/bigtable/img/redistributing-volume-writes.png)

### Distributing reads and writes evenly across nodes

If you've [designed your schema](https://docs.cloud.google.com/bigtable/docs/schema-design) correctly, then reads and writes should be distributed fairly evenly across your entire table. However, there are some cases where you can't avoid accessing certain rows more frequently than others. Bigtable helps you deal with these cases by taking reads and writes into account when it balances tablets across nodes.

For example, suppose that 25% of reads go to a small number of tablets within a cluster, and reads are spread evenly across all other tablets:

![Out of 48 tablets, 25% of reads are going to 3 tablets.](https://docs.cloud.google.com/bigtable/img/redistributing-load-initial.png)

Bigtable will redistribute the existing tablets so that reads are spread as evenly as possible across the entire cluster:

![The three hot tablets are isolated on their own node.](https://docs.cloud.google.com/bigtable/img/redistributing-load-balanced.png)

## Test performance with Bigtable

If you're running a performance test for an application that depends on Bigtable, follow these guidelines as you plan and execute your test:

  * **Test with enough data.**
    * If the tables in your production instance contain a total of 100 GB of data or less per node, test with a table of the same amount of data.
    * If the tables contain more than 100 GB of data per node, test with a table containing at least 100 GB of data per node. For example, if your production instance has one four-node cluster, and the tables in the instance contain a total of 1 TB of data, run your test using a table of at least 400 GB.
  * **Test with a single table**.
  * **Stay below the recommended storage utilization per node.** For details, see [Storage utilization per node](https://docs.cloud.google.com/bigtable/quotas#storage-per-node).
  * **Before you test, run a heavy pre-test for several minutes.** This step allows Bigtable to balance data across your nodes based on the access patterns it observes.
  * **Run your test for at least 10 minutes.** This step lets Bigtable further optimize your data, and it helps ensure that you will test reads from disk as well as cached reads from memory.
  * **For in-memory tier ([Preview](https://cloud.google.com/products#product-launch-stages)) testing**, ensure that the test duration is sufficient to populate the in-memory tier with reads.



## Troubleshoot performance issues

If you think that Bigtable might be creating a performance bottleneck in your application, be sure to check all of the following:

  * **Examine the Key Visualizer scans for your table.** The [Key Visualizer tool for Bigtable](https://docs.cloud.google.com/bigtable/docs/keyvis-overview) generates new scan data every 15 minutes showing the usage patterns for each table in a cluster. Key Visualizer lets you check whether your usage patterns are causing undesirable results, such as hotspots on specific rows or excessive CPU utilization. For more information, see [Use Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started).
  * **Comment out the code that performs Bigtable reads and writes.** If the performance issue disappears, then you're probably using Bigtable in a way that results in suboptimal performance. If the performance issue persists, the issue is probably not related to Bigtable.
  * **Ensure that you're creating as few clients as possible.** Creating a client for Bigtable is a relatively expensive operation. Therefore, you should create the smallest possible number of clients:

    * If you use [replication](https://docs.cloud.google.com/bigtable/docs/replication-overview), or if you use [app profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles) to identify different types of traffic to your instance, create one client per app profile and share the clients throughout your application.
    * If you don't use replication or app profiles, create a single client and share it throughout your application.

If you're using the HBase client for Java, you create a `Connection` object rather than a client, so create as few connections as possible.

  * **Make sure you're reading and writing many different rows in your table.** Bigtable performs best when reads and writes are evenly distributed throughout your table, which helps Bigtable distribute the workload across all of the nodes in your cluster. If reads and writes cannot be spread across all of your Bigtable nodes, performance will suffer.

If you find that you're reading and writing only a small number of rows, you might need to [redesign your schema](https://docs.cloud.google.com/bigtable/docs/schema-design) so that reads and writes are more evenly distributed.

  * **Verify that you see approximately the same performance for reads and writes.** If you find that reads are much faster than writes, you might be trying to read row keys that don't exist, or a large range of row keys that contains only a small number of rows.

To make a valid comparison between reads and writes, aim for at least 90% of your reads to return valid results. Also, if you're reading a large range of row keys, measure performance based on the actual number of rows in that range, rather than the maximum number of rows that _could_ exist.

  * **Use the right type of write requests for your data.** Choosing the optimal way to [write your data](https://docs.cloud.google.com/bigtable/docs/writes) helps maintain high performance.

  * **Check the latency for a single row.** If you observe unexpected latency when sending `ReadRows` requests, you can check the latency of the first row of the request to narrow down the cause. By default, the overall latency for a `ReadRows` request includes the latency for every row in the request as well as the processing time between rows. If the overall latency is high but the first row latency is low, this suggests that the latency is caused by the number of requests or processing time, rather than by a problem with Bigtable.

If you're using the [Bigtable client library for Java](https://github.com/googleapis/google-cloud-java/tree/main/java-bigtable), you can view the `read_rows_first_row_latency` metric in the [Google Cloud console Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) after [enabling client side metrics](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-setup).

  * **Use a separate app profile for each workload.** If you experience performance issues after adding a new workload, [create a new app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile) for the new workload. Then you can monitor metrics for your app profiles separately to troubleshoot further. See [How app profiles work](https://docs.cloud.google.com/bigtable/docs/app-profiles#how-they-work) for details on why it's a best practice to use multiple app profiles.

  * **Enable client-side metrics.** You can [set up client-side metrics](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-setup) to help optimize and troubleshoot performance issues. For example, since Bigtable works best with evenly distributed, high QPS, increased P100 (max) latency for a small percentage of requests does not necessarily indicate a larger performance issue with Bigtable. Client-side metrics can give you insight into which portion of the request lifecycle might be causing latency.

  * **Make sure your application consumes read requests before they time out.** If your application processes data during a read stream, you run the risk of the request timing out before you've received all responses from the call. This results in an `ABORTED` message. If you see this error, reduce the amount of processing during the read stream.




## Direct connectivity

Bigtable supports direct connectivity for application traffic that meets certain criteria, bypassing the Google frontend and optimizing performance. Upgrading to the latest version of your client library to take advantage of direct connectivity can improve throughput and latency. Direct connectivity is provided for applications with the following characteristics:

  * Running on a Compute Engine or Google Kubernetes Engine (GKE) virtual machine in a [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc)
  * Using a supported Bigtable client library
  * Using a standard app profile (not Data Boost)
  * In a network configured with routes and firewall rules that allow egress traffic to reach `34.126.0.0/18` and `2001:4860:8040::/42`



Direct connectivity is supported and enabled by default when you use one of the following Bigtable client libraries:

  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview) version 2.76.0 or later
  * [HBase adapter](https://github.com/googleapis/java-bigtable-hbase) version 2.17.0 or later
  * [Go](https://pkg.go.dev/cloud.google.com/go/bigtable) version 1.50.1 or later



Both IPv4 and IPv6 are supported. For more information, see [Direct connectivity to APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#direct-connectivity) in the VPC documentation.

## What's next

  * Learn how to [design a Bigtable schema](https://docs.cloud.google.com/bigtable/docs/schema-design).
  * Find out how to [monitor Bigtable performance](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).
  * Learn how to [troubleshoot issues with Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started).
  * Learn how to [troubleshoot latency](https://docs.cloud.google.com/bigtable/docs/latency).
  * View sample code for [programmatically adding nodes to a Bigtable cluster](https://docs.cloud.google.com/bigtable/docs/scaling).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
