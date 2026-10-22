---
url: https://docs.cloud.google.com/bigtable/docs/in-memory-overview/
title: In-memory tier overview \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:22.111669+00:00
---

# In-memory tier overview  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/in-memory-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# In-memory tier overview

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The in-memory tier is a cluster-level setting that uses specialized nodes. Before you read this page, understand [instances, clusters, and nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes). We also recommend that you familiarize yourself with the limitations.

**Important:** The in-memory tier is available only in the Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

The Bigtable _in-memory tier_ is an integrated memory tier as part of the Bigtable node that enables seamless, cost-optimized data tiering based on access patterns and performance needs, all through a single API. Using remote direct memory access (RDMA), the Bigtable in-memory tier significantly reduces response times, mitigates hotspots and ensures high throughput for latency-sensitive data. For more information, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance).

## When to use the in-memory tier

We recommend that you enable the in-memory tier for the following use cases:

  * **Sub-millisecond latency requirements** : workloads that require read latencies of less than 1ms, typically addressed by fronting a database with a self-managed cache solution.
  * **High-throughput point reads** : applications with high read traffic throughput requirements on specific subsets of data.
  * **Hotspot mitigation** : high throughput workloads that may include traffic spikes or hotspots on particular row keys.
  * **Cost optimization** : scenarios where you want to reduce the number of Bigtable nodes by offloading high read volumes to a more cost-effective in-memory tier.



## How the in-memory tier works

In-memory tier support is provided by _hybrid storage nodes_. These specialized nodes extend Bigtable's compute and storage disaggregation to include a memory tier with vertically scalable throughput. Bigtable can take up to 30 minutes to provision the specialized in-memory tier nodes. During this period, Bigtable continues to serve traffic from persistent storage.

You can [enable the in-memory tier](https://docs.cloud.google.com/bigtable/docs/modifying-instance#enable-in-memory) at the cluster level.

In-memory tier operates as follows:

  * **Getting data in the memory tier** : the in-memory tier offers read-through caching behavior. A row goes into the memory tier with read operations through an app profile that you configure for the in-memory tier. A write operation from any app profile updates the memory tier if the row data is already in the in-memory tier.
  * **Eviction and invalidation policies** : the in-memory tier uses Least Recently Used (LRU) eviction at the row level and applies a time to live (TTL) invalidation policy to maximize the in-memory tier hit ratio.
  * **Negative caching** : the in-memory tier remembers if a resource is missing for a period of time to prevent backend overload.
  * **Security** : the in-memory tier supports encryption at rest and in transit (TLS).
  * **Replication** : in a multi-cluster instance, memory tiers of different clusters aren't in sync. Because each memory tier independently determines which data to load into memory based on the read traffic it receives, different clusters might hold different row keys in their memory tiers. Bigtable loads data into memory from the local cluster's SSD tier. A write to a row eventually updates it in all memory tiers where it is present, following the standard Bigtable replication model of eventual consistency.
  * **Vertical autoscaling** : the in-memory tier supports [vertical autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling#in-memory-autoscaling) at the node level that works alongside Bigtable autoscaling.



The in-memory tier is optimized for high-performance access to current data. To maintain this performance, only the latest timestamped versions of a row reside in the memory tier. Requests for earlier versions of data, also known as _historical cells_ , automatically bypass the memory tier and are served from persistent storage.

### Data coherence

Bigtable ensures that in-memory tier data is consistent with the persistent data on SSD or infrequent access storage tier. This hybrid architecture lets Bigtable provide a consistent storage model across all storage tiers, enabling you to access your data through the same semantic interface regardless of whether it physically resides in RAM or persistent storage. With Bigtable in-memory tier enabled, you retain read-your-write consistency at the cluster level.

### Vertical scaling

Enabling the in-memory tier lets each node use vertical [scaling](https://docs.cloud.google.com/bigtable/docs/scaling) to modify its in-memory tier throughput capacity. Each node includes 8 GB of RAM for the in-memory tier and starts with a base capacity of 40,000 reads per second. To manage surges in point-read traffic, nodes can automatically scale in increments of 40,000 reads per second, reaching up to a maximum of 120,000 reads per second per node.

This vertical scaling feature integrates with Bigtable autoscaling. If the maximum in-memory tier capacity is reached on all nodes in the cluster and autoscaling is active, Bigtable automatically provisions additional nodes to further boost in-memory tier throughput.

Vertical scaling on a node only applies to in-memory tier reads per second, and it works whether or not cluster-level autoscaling is enabled. Vertical scaling beyond the base 40,000 reads per second is billed by applying a multiplier to the node's hourly cost. For more information, see [pricing](https://docs.cloud.google.com/bigtable/pricing) and [limits](https://docs.cloud.google.com/bigtable/quotas#limits).

## Limitations

The following limitations apply to the in-memory tier:

  * The in-memory tier requires SSD storage.
  * The in-memory tier supports only single row-level point read operations.
  * The in-memory tier doesn't serve data scans or support SQL queries.
  * In-memory tier app profiles support only single-cluster routing.
  * The in-memory tier limits row size to 1 MiB per row key. Bigtable reads rows that exceed this limit from persistent storage.
  * The in-memory tier requires the following versions of Bigtable [client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries):

    * Java version 2.77.0 or later
    * [BOM](https://docs.cloud.google.com/java/docs/bom) version 26.80.0 or later
    * Go version 1.52.0 or later

Other client libraries aren't supported.

  * Clusters that have customer-managed encryption keys (CMEK) enabled don't support the in-memory tier.

  * The in-memory tier is limited to a maximum of 10 nodes per cluster.




## What's next

  * Learn how to [enable the in-memory tier](https://docs.cloud.google.com/bigtable/docs/modifying-instance#enable-in-memory)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
