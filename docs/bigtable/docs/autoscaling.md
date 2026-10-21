---
url: https://docs.cloud.google.com/bigtable/docs/autoscaling/
title: Autoscaling \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:09.873534+00:00
---

# Autoscaling  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Autoscaling

**Note:** This page includes features that are available only in the Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

This page explains how autoscaling works. Before you read this page, you should be familiar with the [Overview of Bigtable](https://docs.cloud.google.com/bigtable/docs/overview) and [Instances, clusters, and nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes).

In Bigtable, instances are containers for clusters, which are location-specific resources that handle requests. Each cluster has one or more nodes, which are compute resources used to manage your data. When you create a cluster in an instance, you choose either _manual node allocation_ or _autoscaling_.

With manual node allocation, the number of nodes in the cluster remains constant until you change it. When autoscaling is enabled, Bigtable continuously monitors the cluster and automatically adjusts the number of nodes in the cluster when necessary. Autoscaling works on both HDD and SSD clusters, in all Bigtable regions.

You can configure autoscaling in the Google Cloud console, using `gcloud`, or using the Cloud Bigtable client library for Java.

## When to use autoscaling

We recommend that you enable autoscaling in most cases. The benefits of autoscaling include the following:

  * **Costs** \- Autoscaling can help you optimize costs because Bigtable reduces the number of nodes in your cluster whenever possible. This can help you avoid over-provisioning.
  * **Performance** \- Autoscaling lets Bigtable automatically add nodes to a cluster when a workload changes or there is an increase in data storage requirements. This helps maintain workload performance objectives by ensuring that the cluster has enough nodes to meet the target CPU utilization and storage requirements.
  * **Automation** \- Autoscaling reduces management complexity. You don't need to monitor and scale the cluster size manually or write an application to do these tasks, because the Bigtable service handles them for you.



Autoscaling alone might not work well for the following workload types, because even though Bigtable quickly adds nodes when traffic increases, it can take time to balance the additional nodes.

  * Bursty traffic
  * Sudden batch workloads



If your spikes in usage are predictable or regularly scheduled, you can use autoscaling and adjust the settings before the planned bursts. See [Delay while nodes rebalance](https://docs.cloud.google.com/bigtable/docs/scaling#delay) for details.

## In-memory tier and autoscaling

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Clusters within Enterprise Plus edition instances can use the in-memory tier. Bigtable in-memory tier uses fully managed [vertical scaling](https://docs.cloud.google.com/bigtable/docs/scaling#vertical-scaling) for throughput, which lets clusters respond almost instantly to spikes in point-read traffic. Vertical scaling adjusts each node automatically to accommodate workload demands and integrates with Bigtable autoscaling. For more information about vertical scaling limits and in-memory tier throughput capacity, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance).

When in-memory tier capacity reaches its limit, Bigtable automatically scales the cluster horizontally according to the autoscaling configuration.

## How autoscaling works

Autoscaling is the process of automatically _scaling_ , or changing the size of, a cluster by adding or removing nodes. When you enable autoscaling, Bigtable automatically adjusts the size of your cluster for you. When your cluster's workload or storage needs fluctuate, Bigtable either _scales up_ , adding nodes to the cluster, or it _scales down_ , removing nodes from the cluster.

Bigtable autoscaling determines the number of nodes required, based on the following dimensions:

  * CPU utilization target
  * Storage utilization target
  * Minimum number of nodes
  * Maximum number of nodes



Each scaling dimension generates a recommended node count, and Bigtable automatically uses the highest one. This means, for example, that if your cluster needs 10 nodes to meet your storage utilization target but 12 to meet your CPU utilization target, Bigtable scales the cluster to 12 nodes.

As the number of nodes changes, Bigtable continuously optimizes the storage, rebalancing data across the nodes, to ensure that traffic is spread evenly and no node is overloaded.

After a cluster is scaled up, Bigtable automatically rebalances the nodes in your cluster for optimal performance. All requests continue to reach the cluster while scaling and rebalancing are in progress. See [Scaling limitations](https://docs.cloud.google.com/bigtable/docs/scaling#limitations) for more information.

If a cluster has scaled up to its maximum number of nodes and the CPU utilization target is exceeded, requests might have high latency or fail. If a cluster has scaled up to its maximum number of nodes and the storage utilization _limit_ is exceeded, write requests will fail. See [Storage per node](https://docs.cloud.google.com/bigtable/quotas#storage-per-node) for more details on storage limits.

When a node is added to a small cluster, such as a one-node cluster, you might observe a temporary increase in latency as the cluster rebalances. This is because the additional node proportionally doubles the size of the cluster. Similarly, if a cluster decreases in size from two nodes to one node, some latency might occur.

When a cluster is scaled down, nodes are removed at a slower rate than when scaling up, to prevent any impact on latency. See [scaling limitations](https://docs.cloud.google.com/bigtable/docs/scaling#limitations) for more details.

## Autoscaling parameters

When you create or edit a cluster and choose autoscaling, you define the values for CPU utilization target, min nodes, and max nodes. You can either configure the storage utilization target or leave it at the default, which is 50% (2.5 TB for SSD and 8 TB for HDD).

Parameter | Description| **CPU utilization target** |  A percentage of the cluster's CPU capacity. Can be from 10% to 80%. When a cluster's CPU utilization exceeds the target that you have set, Bigtable immediately adds nodes to the cluster. When CPU utilization is substantially lower than the target, Bigtable removes nodes. For more information, see Determine the CPU utilization target.   
---|---  
**Minimum number of nodes** |  The lowest number of nodes that Bigtable will scale the cluster down to. If [2x node scaling](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling) is enabled (the default for Enterprise Plus), this must be an even number. This value must be greater than zero and can't be lower than 10% of the value you set for the maximum number of nodes. For example, if the maximum number of nodes is 40, the minimum number of nodes must be at least 4. The 10% requirement is a hard limit. For more information, see Determine minimum number of nodes.  
**Maximum number of nodes** |  The highest number of nodes that you want to let the cluster scale up to. If [2x node scaling](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling) is enabled (the default for Enterprise Plus), this must be an even number. This value must be greater than zero and equal to or greater than the minimum number of nodes. The value can't be more than 10 times the number that you choose for the minimum number of nodes. The 10x requirement is a hard limit. For more information, see Determine the maximum number of nodes.  
**Storage utilization target** |  The maximum number of terabytes per node that you can store in SSD or HDD clusters before Bigtable scales up. This target ensures that you always have enough nodes to handle fluctuations in the amount of data that you store. For more information, see Determine the storage utilization target. This target doesn't include the infrequent access tier.  
**Combined usage of SSD and infrequent access** |  The maximum number of terabytes per node that you can store in SSD and infrequent access clusters before Bigtable scales up. This target ensures that you always have enough nodes to handle fluctuations in the amount of data that you store. For more information, see the Tiered storage and autoscaling section of this document.  
  
## Configure autoscaling

This section describes how to choose your autoscaling parameters. After you set your initial values, [monitor your cluster](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cluster-overview) and adjust the numbers if necessary.

### Determine the CPU utilization target

Base the CPU utilization target on your unique workload. The optimal target for your cluster depends on the latency and throughput requirements of your workload. For more information, see [Plan your Bigtable capacity](https://docs.cloud.google.com/bigtable/docs/performance#planning-your-capacity).

In general, if you observe unacceptably high latency, you should lower the CPU utilization target.

### Determine the storage utilization target

If your application is latency-sensitive, keep storage utilization lower than 60%. If your application is not latency-sensitive, you can choose a storage utilization target of 70% or more. For more information, see [Plan your Bigtable capacity](https://docs.cloud.google.com/bigtable/docs/performance#planning-your-capacity).

For autoscaling, storage utilization is expressed as the number of bytes of storage per node rather than as a percentage. The storage utilization target is specified per node but is applied to the entire cluster. The capacity limits for nodes are 5 TB per node for SSD storage and 16 TB per node for HDD storage.

The following table shows target amounts for typical storage utilization target percentages. The Google Cloud console accepts the value in TB per node, and the gcloud CLI, API, and Cloud Bigtable client libraries accept an integer value in GiB per node.

Percentage | SSD | HDD  
---|---|---  
80% | 4 TB or 4,096 GiB | 12.8 TB or 13,107 GiB  
70% | 3.5 TB or 3,584 GiB | 11.2 TB or 11,468 GiB  
60% | 3 TB or 3,072 GiB | 9.6 TB or 9,830 GiB  
50% | 2.5 TB or 2,560 GiB | 8 TB or 8,192 GiB  
  
#### Tiered storage and autoscaling

Tiered storage ([Preview](https://cloud.google.com/products#product-launch-stages)) doesn't impact SSD autoscaling described in the Determine the storage utilization target section of this document. When you enable infrequent access as part of tiered storage, autoscaling additionally makes sure that the combined SSD and the infrequent access storage doesn't exceed the storage limit per node, depending on the edition. When the limit is reached, Bigtable scales up automatically.

  * **Enterprise edition** : The limit is 32 TB per node.
  * **Enterprise Plus edition** : The limit is 32 TB per node or 64 TB per node.



For example, on an SSD cluster, if you set a storage utilization target of 2.5 TB (50%) per node, and your infrequent access usage is high enough to push the storage usage with tiered storage over the limit, Bigtable adds nodes. This happens even if your SSD usage remains within the 50% target.

The following table helps you understand how autoscaling recommends a node count based on both the SSD usage and the infrequent access usage:

Scenario | Storage utilization target | Utilization percentage | SSD usage | Infrequent access usage | Combined SSD and infrequent access storage | Recommended node count  
---|---|---|---|---|---|---  
SSD usage is within the target range and there is no infrequent access usage. | 5 TB | 100% | Less than 5 TB | 0 TB | Less than 5 TB | 1  
SSD usage exceeds the storage per node limit. | 5 TB | 100% | 6 TB | 0 TB | 6 TB | 2  
SSD usage and infrequent access usage are within the tiered storage limit. | 5 TB | 100% | 5 TB | 27 TB | 32 TB | 1  
Tiered storage usage exceeds the tiered storage limit. | 5 TB | 100% | 5 TB | 28 TB | 33 TB | 2  
SSD usage almost exceeds the SSD usage target, and there is no infrequent access usage. | 3 TB | 60% | 3 TB | 0 TB | 3 TB | 1  
SSD usage almost exceeds the SSD usage target, and tiered usage almost exceeds the tiered storage limit. | 3 TB | 60% | 3 TB | 29 TB | 32 TB | 1  
SSD usage exceeds SSD storage target, and there is no infrequent access usage. | 2.5 TB | 50% | 4 TB | 0 TB | 4 TB | 2  
Tiered usage exceeds the tiered storage limit. | 2.5 TB | 50% | 2 TB | 31 TB | 33 TB | 2  
  
For more information about tiered storage, see [Tiered storage overview](https://docs.cloud.google.com/bigtable/docs/tiered-storage).

### Determine the maximum number of nodes

The value that you choose as the maximum number of nodes should be the number of nodes that the cluster needs to handle your workload's heaviest traffic, even if you don't expect to reach that volume most of the time. Bigtable never scales up to more nodes than it needs. You can also think of this number as the highest number of nodes that you are willing to pay for. For details on accepted values, see Autoscaling parameters.

**Note:** If [2x node scaling](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling) is enabled, the maximum number of nodes must be an even number.

The maximum number needs to allow for both the CPU utilization target set by you _and_ the storage utilization target set by Bigtable.

**If you're changing a cluster from manual allocation to autoscaling** , find the highest number of nodes that the cluster has had over the last month or so. Your autoscaling maximum should be at least that number.

**If you are enabling autoscaling for a new cluster in an existing instance** , use metrics from other clusters in the instance as your guidepost.

**If you have a new workload and you're not sure how it's going to grow** , you can estimate the number of nodes that you need to meet the built-in storage utilization target and then adjust the number later.

**If you enabled tiered storage** , you must account for the storage limit of 32 TB per node (Enterprise) or 64 TB (Enterprise Plus). Even if your SSD usage is low, a large volume of data in the infrequent access tier can trigger node scaling.

To arrive at this number, estimate the amount of data that you plan to store on the cluster, and then divide that number by the storage utilization target for the storage type that you use.

For example, if you store 10 TB on an SSD cluster, you can divide 10 TB by 2.5 TB, which is the storage utilization target set by default for SSD clusters that use autoscaling. The result is 4, which means that 4 is the number of nodes that can handle that amount of data, and **the maximum should be some number higher than that**.

Using the same formula, the following examples show the number of nodes you might need for some sample storage amounts:

SSD storage per cluster | Smallest maximum number of nodes  
---|---  
25 TB | 10  
35 TB | 14  
50 TB | 20  
  
After your cluster is up and running with autoscaling enabled, monitor the cluster and make sure that the value you choose for maximum number of nodes is at least as high as the `recommended number of nodes for CPU target` and the `recommended number of nodes for storage target`.

### Determine the minimum number of nodes

You can set the minimum as low as 1 to ensure that your Bigtable can scale down to the smallest, most cost-efficient size if possible. The cluster never becomes too small because Bigtable automatically prevents the node count from dropping below the minimum needed to maintain the CPU and storage utilization targets. See Autoscaling parameters for details on accepted values.

However, in many cases you will want to set this value to more than one. Choose a higher number or raise the minimum number of nodes for the following situations:

  * You have an upcoming peak scale event, when you expect your traffic to temporarily increase, and you want to make sure you have enough capacity.
  * Your application sends spiky traffic. When new nodes are added, Bigtable automatically rebalances onto the new nodes. Because this process can take several minutes, you are often better off taking a conservative approach and choosing a higher minimum so that your cluster can seamlessly accommodate the spikes.
  * You increase the maximum number of nodes. The minimum must always be ten percent or less of the maximum number of nodes. For example, if you set the maximum to 30, you must set the minimum to at least 3.

**Note:** If [2x node scaling](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling) is enabled, the minimum number of nodes must be an even number.

If you increase the value for a cluster's minimum number of nodes, Bigtable immediately attempts to scale the cluster to the new minimum. The [standard constraints](https://docs.cloud.google.com/bigtable/quotas#availability) apply, however; if a zone is out of nodes, additional nodes are not provisioned to meet the configured minimum. Bigtable continues to attempt to add nodes and creates an audit log entry for each failed attempt until it successfully scales the cluster to the new minimum number of nodes. Bigtable does not change the configured value in this situation. As a result, you might observe that the cluster's node count is less than the minimum until scaling is complete.

### Fine-tune your settings

After you enable autoscaling, it's important to monitor its behavior and adjust your settings as needed. Use the monitoring metrics to observe the following:

  * **Recommended node counts:** Pay close attention to the `recommended_node_count_for_cpu` and `recommended_node_count_for_storage` metrics. These metrics indicate the ideal number of nodes based on your CPU and storage utilization targets, respectively.
  * **Provisioned node count:** Compare the recommended node counts with the actual number of nodes that are provisioned. If your cluster is consistently using more nodes than recommended, you can consider reducing the minimum number of nodes to lower your costs.
  * **Maximum node count:** Ensure that your maximum number of nodes is high enough to allow your cluster to scale up to meet demand. If you observe that your cluster is frequently hitting the maximum node count, increase it to provide more capacity.



You can also **adjust CPU utilization target for performance**. If you observe latency issues, you might need to lower the CPU utilization target to ensure that your cluster scales up more aggressively when demand increases. Conversely, if your cluster is consistently over-provisioned and your latency is acceptable, you can consider increasing the CPU target.

### Account for replication

In an instance that uses replication, each cluster's autoscaling settings and activity are completely independent of those for the other clusters in the instance. You must configure the scaling mode for each cluster in an instance.

In general, for replicated instances, you should enable autoscaling for every cluster in the instance. Your autoscaling configuration will often be the same for every cluster in the instance, but might be different depending on the use case, workload, and performance requirements for each cluster.

Because clusters in a replicated instance do some additional work to manage replication, you should choose a higher maximum number of nodes for them than you would for a single-cluster instance. To learn more, see [Replication and performance](https://docs.cloud.google.com/bigtable/docs/performance#performance-replication).

## Access control

To configure autoscaling, you need to be a principal in a role that has [`create` and `update` permissions](https://docs.cloud.google.com/bigtable/docs/access-control#permissions) for the cluster and instance that you are configuring.

## Monitoring

Bigtable provides several metrics to help you understand how Bigtable autoscaling is working as it scales up and down to meet workload requirements. The metrics also can help you gauge whether your settings are optimal to meet your business's workload and cost requirements. For example, if you observe that the node count for a cluster is often close to the maximum number of nodes, you might consider raising the maximum. To learn more about monitoring your Bigtable resources, see [Monitoring an instance](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).

The following metrics are [displayed in graphs](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cluster-overview) on the cluster overview page in the Google Cloud console. You can also view these metrics using [Cloud Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#stackdriver).

  * `bigtable.googleapis.com/cluster/autoscaling/min_node_count`
  * `bigtable.googleapis.com/cluster/autoscaling/max_node_count`
  * `bigtable.googleapis.com/cluster/autoscaling/recommended_node_count_for_cpu`
  * `bigtable.googleapis.com/cluster/autoscaling/recommended_node_count_for_storage`
  * Enterprise Plus only: `bigtable.googleapis.com/memory_layer/request_unit_usage`



## Logging

Bigtable emits a system event audit log each time it scales a cluster. The log entry is similar to the following:
    
    
    Grew from 9 to 10 nodes to maintain CPU utilization at 60%.
    

You can view autoscaling system event logs on the Bigtable cluster overview page in the Google Cloud console. You can also view them using Logs Explorer:

  1. Navigate to the Logs Explorer:

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

Select the appropriate Google Cloud project.

  2. In the **Query** field, enter the following:
         
         resource.type="audited_resource" resource.labels.service="bigtableadmin.googleapis.com"
         resource.labels.method="AutoscaleCluster"
         

  3. Click **Run query**.

The **Query results** pane displays the logs for the last hour.




To learn more about viewing logs, see [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview).

## What's next

  * [Enable autoscaling on an existing cluster.](https://docs.cloud.google.com/bigtable/docs/modifying-instance)
  * [Understand Bigtable performance.](https://docs.cloud.google.com/bigtable/docs/performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
