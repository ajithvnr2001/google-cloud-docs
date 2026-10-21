---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/plan-cluster-size/
title: Plan the size of your Managed Service for Apache Kafka cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:10.478205+00:00
---

# Plan the size of your Managed Service for Apache Kafka cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/plan-cluster-size/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Plan the size of your Managed Service for Apache Kafka cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to estimate the capacity that you need for a Managed Service for Apache Kafka cluster, and how to adjust the size of an existing cluster.

When you create a Managed Service for Apache Kafka cluster, you choose the following parameters for the size of the cluster:

  * **vCPUs** : The number of vCPUs in the cluster. The minimum vCPU count is 3.

  * **Memory** : The amount of memory per vCPU. You must provision between 1 GiB and 8 GiB per vCPU.




You can update these values after the cluster is created.

## Choose the initial cluster size

To choose the initial cluster size, start by estimating the following values, based on your particular workload.

  * **Write throughput** : The total rate at which producers send data to the cluster, in MBps.
  * **Read throughput** : The total rate at which consumers read data from the cluster, in MBps.



To estimate the size of a cluster necessary to handle this throughput, perform the following steps:

  1. Calculate the total write bandwidth, including [replication](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-topic#replication-factor).

`Total write bandwidth = produce rate * replicas`

This value includes bandwidth from the client to the leader broker, and from the leader to replica brokers. The default number of replicas is 3.

  2. Calculate the total read bandwidth, including replication.

`Total read bandwidth = consume rate + produce rate * ( replicas - 1)`

This value includes bandwidth for the client's read operations (consume rate), plus bandwidth needed for the replicas to stay synchronized. Replicas synchronize by reading data from the partition leader. The `(replicas - 1)` term is used because the partition leader doesn't read from any replicas.

  3. Calculate the write-equivalent data rate.

As a general rule, read bandwidth is 4 times more efficient to process than write bandwidth. To account for this difference, calculate the _write-equivalent_ data rate as follows:

`Write-equivalent rate = (total write bandwidth) + (total read bandwidth / 4)`

  4. Determine your target vCPU utilization. This value represents average vCPU utilization as a percentage of vCPU capacity. The actual utilization might spike or dip over time.

     * As a baseline, start with a utilization target of 50%.
     * If you know the expected traffic patterns, set the utilization target equal to the ratio of the average write-equivalent bandwidth to the peak bandwidth you must accommodate.

Generally, increasing utilization lowers the cost of your cluster by reducing its size, but is also riskier if the traffic exceeds estimates. Excessive vCPU utilization can cause high latencies and errors.

  5. Calculate the number of vCPUs.

`vCPU count = ceiling (write-equivalent rate / 20 MBps / utilization)`

The estimated capacity for a single vCPU in a single zone is 20 MBps. Therefore, if the vCPUs ran at 100% utilization, you would need `(write-equivalent rate / 20)` vCPUs. To get the actual number, divide that value by the target utilization and round up.

Also, sending messages in batches smaller than 10 KB reduces throughput per CPU, relative to the benchmark here. In that case, either account for the reduced throughput capacity or consider sending larger batches.

  6. Estimate the required memory. We recommend 4 GiB of RAM for each vCPU.

`Memory = vCPU count * 4 GiB`




Test with your real workload for the most accurate sizing. Monitor the cluster's resource usage and scale up if needed.

### Example size calculation

Assume that a workload has a write rate of 50 MBps and a read rate of 100 MBps, with 3 replicas and a target vCPU utilization of 50%.

  1. `Total write bandwidth = 50 MBps * 3 replicas = 150 MBps`
  2. `Total read traffic = 100 MBps + 50 MBps * (3 - 1) = 200 MBps`
  3. `Write-equivalent rate = 150 MBps + (200 MBps / 4) = 200 MBps`
  4. `Target utilization = 0.5`
  5. `Number of vCPUs = ceiling (200 MBps / 20 MBps / 0.5) = 20 vCPUs`
  6. `Memory = 20 vCPUs * 4 GiB = 80 GiB`



### Partition replica limits

There are limits on the partition replica counts per cluster and per broker that are important to consider when sizing your cluster.

The per cluster limit is 100,000 partition replicas. This is a hard limit and is independent of the number of brokers in a cluster. If your workload requires more than 100,000 partition replicas, consider splitting it between two or more clusters.

The per broker limit is 4,000 partition replicas. This is not a hard limit. If you need to handle more than this number of replicas, consider increasing the size of the cluster to provision more brokers. For information about how the service determines the number of brokers, see [Broker provisioning](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers#broker-provisioning).

Once you have a sufficient number of brokers to handle your partitions, you can scale the broker sizes to accommodate the throughput.

## Update the cluster size

After you create a Managed Service for Apache Kafka cluster, you can adjust the vCPU count and memory to accommodate your needs. For more information, see [Update a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster).

When you update an existing cluster, the following rules apply:

  * The cluster's overall vCPU-to-memory ratio must always remain between 1:1 and 1:8.

  * There must be at least 1 vCPU and 1 GiB of memory for each existing broker. The number of brokers never decreases.

  * If the cluster has a [custom disk configuration](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size#custom-disk-configuration), the update must meet the [disk configuration requirements](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size#disk-configuration-requirements) for local storage.

  * If you upscale, the average vCPU and memory per broker can't decrease by more than 10% compared to the averages before the update. For example, if you try to upscale a cluster from 45 vCPUs (3 brokers) to 48 vCPUs (4 brokers), the average vCPU per broker decreases from 15 to 12, which is a 20% reduction, exceeding the 10% limit.

If you need to decrease the vCPU count by more than 10%, we recommend reducing it in several stages. After each update, monitor resource utilization, and rebalance partitions if needed.

However, if you are confident that your brokers will have enough capacity after the update, you can disable this check by running the [`gcloud managed-kafka clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update) command with the `allow_broker_downscale_on_cluster_upscale=true` flag. This flag signals that you accept the potential performance risk.




### Example update operations

The following examples start with a cluster that has **75 vCPUs** , **130 GiB RAM** , and **5 brokers**.

#### Example of a failed upscale operation

Upscale the cluster to **80 vCPUs** and **140 GiB RAM**.

  * The service determines whether a new broker is needed.

    * ceiling (80 vCPUs / 15) = 6 brokers

The cluster would grow from 5 to 6 brokers, so the 10% safety check is triggered.

  * The current averages per broker are:

    * 75 vCPUs / 5 brokers = 15 vCPUs per broker

    * 130 GiB / 5 brokers = 26 GiB per broker

  * With 6 brokers, the new averages are:

    * 80 vCPUs / 6 brokers = 13.33 vCPUs per broker, an 11.1% reduction

    * 140 GiB / 6 brokers = 23.33 GiB per broker, a 10.2% reduction

The operation fails, because these averages exceed 10%.




#### Example of a successful upscale operation

Upscale the cluster to **85 vCPUs** and **150 GiB RAM**.

  * The service determines if a new broker is needed.

    * ceiling (85 vCPUs / 15) = 6 brokers

The cluster would grow from 5 to 6 brokers, so the 10% safety check is triggered.

  * The current averages per broker are:

    * 75 vCPUs / 5 brokers = 15 vCPUs per broker

    * 130 GiB / 5 brokers = 26 GiB per broker

  * With 6 brokers, the new averages are:

    * 85 vCPUs / 6 brokers = 14.17 vCPUs per broker, a 5.5% reduction

    * 150 GiB / 6 brokers = 25 GiB per broker, a 3.8% reduction




This operation succeeds because the reduction in average vCPU and memory per broker is within the 10% limit.

## Estimate the required disk size

By default, Managed Service for Apache Kafka allocates 100 GiB per vCPU to each broker. The default allocation provides enough local storage for most workloads, but you can [configure the broker disk size](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size) for your specific requirements. This section describes how to estimate the amount of disk capacity that you need.

When a broker receives a message, it writes the message to a local segment file. When the segment file reaches a maximum size or age, it is closed (or "rolled") and moved to remote storage. The maximum size of a segment file is specified by the `log.roll.bytes` setting, and the maximum age is specified by the `log.segment.ms` setting.

When a segment file is rolled, the broker opens a new segment file. The rolled segment remains in local storage while the broker copies it to remote storage. Therefore, each partition needs enough space to store a rolled segment file, plus space for a new segment file while the rolled segment is being moved to remote storage.

By default, the maximum size of a segment file is 230 MiB. For clusters with moderate utilization, you can assume that 250 MiB is needed per partition, to give additional buffer space while a rolled segment is being moved. Using this assumption, the minimum disk size per broker is:

`250 MiB * partition count * replication factor / broker count`

However, the required size depends on factors such as the maximum segment file size, the load on the cluster, the rate at which new data is written, and the latency of writes to long-term storage.

It is critical to maintain some unused disk capacity on each broker. The behavior of a broker with no disk capacity is not predictable, and can result in data loss as well as cluster instability. Monitor disk usage ([`disk/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/disk/used_bytes)) against total available disk size ([`disk/limit`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#managedkafka/disk/limit)). If disk usage is over 80% of the total available disk size, configure a larger disk size. For more information, see [Monitor cluster capacity](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-reliability#monitor-capacity).

## What's next

  * [Create a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster)
  * [Monitor a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/monitor-cluster)
  * [Update a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster)
  * [Configure broker disk size](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
