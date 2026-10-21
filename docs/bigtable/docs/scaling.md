---
url: https://docs.cloud.google.com/bigtable/docs/scaling/
title: Scaling \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:09.763715+00:00
---

# Scaling  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/scaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Scaling

**Note:** This page includes features that are available only in the Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

_Scaling_ a cluster is the process of adding or removing nodes from the cluster in response to changes in the cluster's workload or data storage needs. When you create a cluster, you also can configure the _node scaling factor_ for the cluster. Before you configure scaling, understand the limitations.

You can scale your Bigtable cluster based on metrics such as the cluster's CPU usage. For example, if your cluster is under heavy load and its CPU utilization is high, you can add nodes to the cluster until its CPU usage drops. You can also save money by removing nodes from the cluster when it is not being used heavily.

You can scale a Bigtable cluster in the following ways:

## Horizontal scaling

  * [Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling)
  * Manual node allocation



**In most cases, choose autoscaling.** When you enable autoscaling for a cluster, Bigtable continuously monitors the cluster and automatically adjusts the number of nodes based on your settings.

## In-memory tier vertical scaling

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Bigtable in-memory tier uses fully managed vertical scaling for throughput, which lets clusters respond almost instantly to spikes in point-read traffic.

Vertical scaling automatically adjusts each node to accommodate workload demands and works seamlessly with Bigtable autoscaling. Each Bigtable node with in-memory tier enabled has a vertical scaling limit. If that limit is reached, Bigtable autoscaling adds nodes within the maximum node configuration to support the workload and rebalance the traffic.

For more information about vertical scaling limits, see [Quotas and limits](https://docs.cloud.google.com/bigtable/quotas). For more information about in-memory throughput capacity per node, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance).

## Node scaling factor

When you create a Bigtable cluster, you have the option to configure the cluster with a **2x node scaling factor**. When you choose this configuration, Bigtable treats two standard nodes as a larger, single compute node, and the cluster is always scaled in increments of two nodes. As a result, there are fewer compute boundaries between nodes in the cluster. Depending on the workload, the benefits of 2x node scaling include the following:

  * Improved throughput and tail latency stability
  * Greater ability to absorb hotspots



You can create a cluster with 2x node scaling factor enabled when you use the Google Cloud console or the gcloud CLI.

You can configure 2x node scaling with autoscaling or manual node allocation. In the Enterprise Plus edition, you must enable 2x node scaling to access the expanded tiered storage limit of 64 TB per node ([Preview](https://cloud.google.com/products#product-launch-stages)).

For limitations, see Node scaling factor limitations.

### Small clusters

2x node scaling is optimal for larger workloads. If you are considering changing from standard node scaling (by a factor of one) to 2x node scaling, consider the cost implications. For a smaller workload, such as one that runs on a cluster with one node, using 2x node scaling costs twice as much. Similarly, using 2x node scaling for a workload that previously was run on a cluster with 3 nodes increases costs by 33%.

On the other hand, for a workload that previously ran on a large cluster, such as a cluster with 50 nodes, the effect of a 2x node scaling factor is small relative to the number of nodes.

Bigtable returns an error if you try to create a cluster with 2x node scaling factor in an unsupported zone.

## Limitations

Cluster scaling is subject to node availability, takes time to complete, can't compensate for an inappropriate schema design, and must be done gradually. The following sections describe these limitations, as well as limitations that apply to 2x node scaling.

### Node availability

Node quotas apply whether a cluster has manual node allocation or autoscaling enabled. See [Quotas and node availability](https://docs.cloud.google.com/bigtable/quotas#availability) for details.

### Delay while nodes rebalance

After you add nodes to a cluster, it can take up to 20 minutes under load before you see a significant improvement in the cluster's performance. As a result, if your workload involves short bursts of high activity, adding nodes to your cluster based on CPU load doesn't improve performance — by the time Bigtable rebalances your data, the short burst of activity will be over.

To plan for this delay, you can add nodes to your cluster, either programmatically or through the Google Cloud console, _before_ you increase the load on the cluster. This approach gives Bigtable time to rebalance your data across the additional nodes before the workload increases. On clusters that use manual node allocation, change the number of nodes. On clusters that use autoscaling, change the [minimum number of nodes](https://docs.cloud.google.com/bigtable/docs/autoscaling#parameters). After your traffic returns to normal, change your node settings back.

The in-memory tier handles traffic spikes with almost instant vertical scaling. When Bigtable adds nodes through autoscaling and the in-memory tier throughput capacity increases, it automatically manages data sharding in the in-memory tier.

### Latency increases caused by scaling down too quickly

When you decrease the number of nodes in a cluster to scale down, try not to reduce the cluster size by more than 10% in a 10-minute period. Scaling down too quickly can cause performance problems, such as increased latency, if the remaining nodes in the cluster become temporarily overwhelmed.

### Schema design issues

If there are problems with the schema design for your table, adding nodes to your Bigtable cluster may not improve performance. For example, if you have a large number of reads or writes to a single row in your table, all of the reads or writes will go to the same node in your cluster; as a result, adding nodes doesn't improve performance. In contrast, if reads and writes are evenly distributed across rows in your table, adding nodes will generally improve performance.

See [Designing Your Schema](https://docs.cloud.google.com/bigtable/docs/schema-design) for details about how to design a schema that lets Bigtable scale effectively.

### Editions limitations

The in-memory tier and vertical scaling are available only for SSD clusters in the Enterprise Plus edition.

### Node scaling factor limitations

You can't convert a cluster with standard node scaling to use 2x node scaling; you must create a new cluster and enable 2x node scaling at creation time. For more information on adding a cluster to an instance, see [Modify an instance](https://docs.cloud.google.com/bigtable/docs/modifying-instance).

You can't configure 2x node scaling for an HDD cluster.

You can create clusters configured with 2x node scaling in every Bigtable region, but not in every zone. The following zones can't contain a cluster with 2x node scaling:

  * me-central2-b 



## What's next

  * Learn about [Bigtable autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling).
  * Find out how you can [monitor your instance](https://docs.cloud.google.com/bigtable/docs/monitoring-instance), both programmatically and through the Google Cloud console.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
