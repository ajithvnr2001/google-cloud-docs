---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size/
title: Configure broker disk size \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:29.009825+00:00
---

# Configure broker disk size  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Configure broker disk size Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how Managed Service for Apache Kafka manages storage for a Kafka cluster, and how to configure disk capacity in a cluster. The service automatically provisions disks when you create a cluster, but depending on your Kafka workloads, you might want to allocate more disk capacity than the default.

## Overview

Managed Service for Apache Kafka uses [tiered storage](https://kafka.apache.org/37/operations/tiered-storage/). Tiered storage combines two tiers of storage: 

  * A limited amount of fast _local storage_ , in the form of pre-provisioned disks attached to the brokers.
  * Effectively unlimited _remote storage_. Remote storage is less expensive and doesn't need to be pre-provisioned.



The tiered storage system lets you store large volumes of data with less risk of running out of disk space. It can also cost less than using local storage alone.

When a broker receives a message, it writes the message to a local segment file. When the segment file reaches a maximum size or age, it is closed (or "rolled") and moved to remote storage. At any time, there is a single open segment file per partition, so the volume of local storage scales with the number of partitions and the maximum size of the segment files. Brokers that handle more partitions need more local storage space.

To set the size of the segment files, set the `log.roll.ms` and `log.segment.bytes` broker configurations.

If you enable [log compaction](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-topic#log-compaction), then only local storage is used for that topic.

## Default disk configuration

By default, Managed Service for Apache Kafka provisions at least 100 GiB of disk capacity per vCPU for every broker. When you scale up a cluster, the service ensures that brokers have at least 100 GiB per CPU. Disk capacity per broker is never reduced, even if the number of vCPUs per broker decreases.

To see how much disk capacity has been allocated, view the cluster's effective disk capacity.

## Custom disk configuration

The default disk configuration provides a balance of local storage that is safe and cost effective for most users. However, you can also specify the local disk size by setting a _custom disk configuration_ when you create or update a cluster.

**Important:** After you set a custom disk configuration, you can't re-enable the default disk configuration for that cluster.

You might choose to increase the disk size for the following reasons:

  * **Log compaction with large key spaces**. If [log compaction](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/edit-topic#log-compaction) is enabled on a topic, Kafka stores the latest message for each key on disk. A large key space can result in a large number of messages being kept on disk indefinitely.

  * **Large number of partitions.** Each partition requires enough space to store a rolled segment, plus space for a new segment file while the broker copies the rolled segment file to remote storage. If you have more than 200 partitions per vCPU, consider setting a custom storage configuration.

  * **High load**. An overloaded broker might not have enough disk capacity to move rolled files to remote storage quickly enough, and therefore might require more local storage.

  * **Out-of-disk errors.** If your cluster runs out of disk space on a broker, you can increase the disk capacity to make the cluster operational.




For more information, see [Estimate the required disk size](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/plan-cluster-size#required-disk-size).

### Disk configuration requirements

A custom disk configuration must meet the following requirements:

  * The disk size per broker must be at least equal to the number of vCPUs on each broker multiplied by 100 GiB.

For example, a cluster with 6 vCPUs and 3 brokers requires at least 200 GiB per broker.

  * The disk size per broker can't exceed 32768 GiB (32 TiB).

  * Disk size per broker cannot decrease. If you update a cluster, the new disk size must be equal to or greater than the current effective disk capacity.

  * If you scale up a cluster, the updated vCPU count and disk size must meet the previous requirements, taking into account that new brokers might be added. To calculate the number of brokers, see [Scaling the cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers#scaling).

For example, suppose you have a cluster with 3 vCPUs and 200 GiB of disks per broker. If you scale the cluster to 9 vCPUs, the minimum disk size is 300 GiB (9 vCPUs / 3 brokers × 100 GiB). To meet this requirement, you would need to set the disk size along with the vCPU count in the same update request.




### Set a custom disk configuration

You can set a custom disk configuration when you create a cluster, or by updating an existing cluster. The configuration applies to all brokers in the cluster.

###  Console 

In the **Create Kafka cluster** or **Edit Kafka cluster** page, perform the following steps:

  1. Under **Capacity configuration** , click the **Enable custom local storage size** toggle to the on position.

**Important:** After you click **Save** , this setting cannot be disabled again for this cluster.
  2. In the **Custom local storage** field, enter the disk size per broker, in GiB. The value must meet the Disk configuration requirements, or an error occurs.

  3. Click **Save**.




###  gcloud 

Specify the `--broker-disk-size-gib` flag in the `gcloud managed-kafka clusters create` or `gcloud managed-kafka clusters update` command.

Create a cluster:
    
    
    gcloud managed-kafka clusters create CLUSTER_ID \
      --location=LOCATION \
      --broker-disk-size-gib=DISK_SIZE
    
      # Other configruration flags
      ...
    

Update a cluster:
    
    
    gcloud managed-kafka clusters update CLUSTER_ID \
      --location=LOCATION \
      --broker-disk-size-gib=DISK_SIZE
    

Replace the following:

  * CLUSTER_ID: The name of the cluster.
  * LOCATION: The location of the cluster.
  * DISK_SIZE: The disk size per broker, in GiB. The value must meet the Disk configuration requirements, or an error occurs.



For more information about creating and updating Kafka clusters, see the following documents:

  * [Create a Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster)
  * [Update a Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster)



### View a custom disk configuration

To view a custom disk configuration on a Managed Service for Apache Kafka cluster, perform the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. From the list of clusters, click the cluster that you want to view.

  3. Select the **Configurations** tab.

  4. Under **Capacity** , if the cluster has a custom disk configuration, the **Custom local storage** row shows the disk size per broker. Otherwise, the row shows `Disabled`.




###  gcloud 

Run the [`gcloud managed-kafka clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/describe) command:
    
    
    gcloud managed-kafka clusters describe CLUSTER_ID \
      --location=LOCATION
    

Replace the following:

  * CLUSTER_ID: The name of the cluster.
  * LOCATION: The location of the cluster.



In the returned cluster description, the `brokerCapacityConfig` field shows the configuration:
    
    
    brokerCapacityConfig:
      diskSizeGib: '3000'
    

If you didn't set a custom disk configuration, this field is empty:
    
    
    brokerCapacityConfig: {}
    

## View the effective disk capacity

A cluster's _effective_ disk capacity is how much disk space has been provisioned per broker. To view the effective disk capacity for a cluster, run the [`gcloud managed-kafka clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/describe) command with the `--full` flag.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. From the list of clusters, click the cluster that you want to view.

  3. Select the **Configurations** tab.

  4. Under **Capacity** , the **Effective local storage** row shows the disk size per broker.




###  gcloud 
    
    
    gcloud managed-kafka clusters describe CLUSTER_ID --full \
      --location=LOCATION
    

Replace the following:

  * CLUSTER_ID: The name of the cluster.
  * LOCATION: The location of the cluster.



In the returned cluster description, the `effectiveCapacityConfig` field contains the disk size per broker and the number of brokers:
    
    
    effectiveCapacityConfig:
      brokerCount: '3'
      brokerDiskSizeGib: '1024'
    

Total disk capacity equals `brokerCount` × `brokerDiskSizeGib`.

## Pricing

If your cluster uses default disk configuration, you are billed for 100 GiB per cluster vCPU, although the actual disk size per broker might exceed this value.

After you set a custom disk configuration on a cluster, you are billed for the actual size of the disks across all of the brokers.

## What's next

  * [Plan the size of your Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/plan-cluster-size)
  * [View a cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster)
  * [Create a cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster)
  * [Update a cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
