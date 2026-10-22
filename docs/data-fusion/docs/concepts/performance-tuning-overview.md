---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/performance-tuning-overview/
title: Pipeline performance overview \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:00.029172+00:00
---

# Pipeline performance overview  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/performance-tuning-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Pipeline performance overview Stay organized with collections  Save and categorize content based on your preferences. 

Tuning pipeline processing in Cloud Data Fusion lets you optimize execution speed and prevent runtime bottlenecks. Understanding these concepts helps you size infrastructure effectively and reduce compute costs across your data workflows.

Pipeline performance depends on the following aspects:

  * The size and characteristics of your data
  * The structure of your pipeline
  * Cluster sizing
  * Plugins that your Cloud Data Fusion pipeline uses



## Pipeline processing terminology in Cloud Data Fusion

The following terminology applies in pipeline processing in Cloud Data Fusion.

Machine type
    Type of virtual machines (VMs) used (CPU, memory).
Cluster
    A group of VMs working together to handle large-scale data processing tasks.
Master and worker nodes
    Physical or virtual machines that can do processing. Master nodes usually coordinate work. Worker nodes run executors that process data. They have machine characteristics (amount of memory and number of vCores available for processes).
vCores, Cores, or CPUs
    A resource that does computing. Usually your nodes provide a certain amount of Cores and your Executors request one or a few CPUs. Balance this along with memory, or you might underutilize your cluster.
Driver
    A single VM that acts as the central coordinator for the entire cluster. It manages tasks, schedules work across worker nodes, and monitors job progress.
Executors
    Multiple VMs performing the actual data processing tasks, as instructed by the driver. Your data is partitioned and distributed across these executors for parallel processing. To utilize all of the executors, you must have enough splits.
Splits or partitions
    A dataset is _split_ into splits (other name partitions) to process data in parallel. If you don't have enough splits, you can't utilize the whole cluster.

## Performance tuning overview

Pipelines are executed on clusters of machines. When you choose to run Cloud Data Fusion pipelines on Managed Service for Apache Spark clusters (which is the recommended provisioner), it uses YARN (Yet Another Resource Negotiator) behind the scenes. Managed Service for Apache Spark utilizes YARN for resource management within the cluster. When you submit a Cloud Data Fusion pipeline to a Managed Service for Apache Spark cluster, the underlying Apache Spark job leverages YARN for resource allocation and task scheduling.

A cluster consists of master and worker nodes. Master nodes are generally responsible for coordinating work, while worker nodes perform the actual work. Clusters will normally have a small number of master nodes (one or three) and a large number of workers. YARN is used as the work coordination system. YARN runs a Resource Manager service on the master node and a Node Manager service on each worker node. Resource Managers coordinate amongst all the Node Managers to determine where to create and execute containers on the cluster.

![YARN Resource Managers and Node Managers](https://docs.cloud.google.com/static/data-fusion/docs/images/concepts/yarn-resource-and-node-managers.svg)

On each worker node, the Node Manager reserves a portion of the available machine memory and CPUs for running YARN containers. For example, on a Managed Service for Apache Spark cluster, if your worker nodes are n1-standard-4 VMs (4 CPU, 15 GB memory), each Node Manager will reserve 4 CPUs and 12 GB memory for running YARN containers. The remaining 3 GB of memory is left for the other Hadoop services running on the node.

When a pipeline is run on YARN, it will launch a pipeline workflow driver, a Spark driver, and many Spark executors in Managed Service for Apache Spark.

![Drivers and Executors](https://docs.cloud.google.com/static/data-fusion/docs/images/concepts/drivers-and-executors.svg)

The workflow driver is responsible for launching the one or more Spark programs that make up a pipeline. The workflow driver usually doesn't do much work. Each Spark program runs a single Spark driver and multiple Spark executors. The driver coordinates work amongst the executors, but usually doesn't perform any actual work. Most of the actual work is performed by the Spark executors.

## What's next

  * Learn about [parallel processing](https://docs.cloud.google.com/data-fusion/docs/concepts/parallel-processing) in Cloud Data Fusion.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
