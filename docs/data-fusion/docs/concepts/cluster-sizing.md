---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/cluster-sizing/
title: Cluster sizing \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:02.397683+00:00
---

# Cluster sizing  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/cluster-sizing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Cluster sizing Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Data Fusion by default used Autoscale as the compute profile. Estimating the best number of cluster workers (nodes) for a workload is difficult, and a single cluster size for an entire pipeline is often not ideal. The Managed Service for Apache Spark Autoscaling provides a mechanism for automating cluster resource management and enables cluster worker VM autoscaling. For more information, see [Autoscaling](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling)

On the **Compute config** page, where you can see a list of profiles, there is a **Total cores** column, which has the maximum v CPUs that the profile can scale up to, such as `Up to 84`.

If you want to use the Managed Service for Apache Spark Compute profile , you can manage cluster sizes based on the pipeline size.

## Master node

Master nodes use resources proportional to the number of pipelines or additional applications that are running on the cluster. If you're running pipelines on ephemeral clusters, use 2 CPUs and 8 GB of memory for the master nodes. If you're using persistent clusters, you might need larger master nodes to keep up with the workflow. To understand if you need larger master nodes, you can monitor memory and CPU usage on the node. We recommend sizing your worker nodes with at least 2 CPUs and 8 GB of memory. If you've configured your pipelines to use larger amounts of memory, then you must use larger workers.

To minimize execution time, ensure that your cluster has enough nodes to allow for as much parallel processing as possible.

## Workers

The following sections describe aspects of sizing worker nodes.

### CPU and Memory

We recommend sizing your worker nodes with at least 2 CPU and 8 GB memory. If you configured your pipelines to use larger amounts of memory, use larger workers. For example, with a 4 CPU 15 GB worker node, each worker will have 4 CPU and 12 GB available to run YARN containers. If your pipeline is configured to run 1 CPU, 8 GB executors, YARN is unable to run more than one container per worker node. Each worker node would have an extra 3 CPU and 4 GB that's wasted because it can't be used to run anything. To maximize resource utilization on your cluster, you will want the YARN memory and CPUs to be an exact multiple of the amount needed per Spark executor. You can check how much memory each worker has reserved for YARN by checking the `yarn.nodemanager.resource.memory-mb` property in YARN.

If you're using Managed Service for Apache Spark, the memory available for YARN containers will be roughly 75% of the VM memory. The minimum YARN container size is also adjusted depending on the size of the worker VMs. Some common worker sizes and their corresponding YARN settings are given in the following table.

Worker CPU | Worker memory (GB) | YARN node memory (GB) | YARN min allocation memory (MB)  
---|---|---|---  
1 | 4 | 3 | 256  
2 | 8 | 6 | 512  
4 | 16 | 12 | 1024  
8 | 32 | 24 | 1024  
16 | 64 | 51 | 1024  
  
Keep in mind that Spark requests for more memory than the executor memory set for the pipeline, and that YARN rounds that requested amount up. For example, suppose you have set your executor memory to 2048 MB, and have not given a value for `spark.yarn.executor.memoryOverhead`, which means the default of 384 MB is used. That means Spark requests 2048 MB + 384 MB for each executor, which YARN rounds up to an exact multiple of the YARN minimum allocation. When running on a 8 GB worker node, because the YARN minimum allocation is 512 MB, it gets rounded up to 2.5 GB. This means each worker can run two containers, using up all available CPUs, but leaving 1 GB of YARN memory (6 GB - 2.5 GB - 2.5 GB) unused. This means the worker node can actually be sized a little smaller, or the executors can be given a little bit more memory. When running on a 16 GB worker node, 2048 MB + 1024 MB is rounded up to 3 GB because the YARN minimum allocation is 1024 MB. This means each worker node is able to run four containers, with all CPUs and YARN memory in use.

To help give context, the following table shows recommended worker sizes given some common executor sizes.

**Executor CPU** | **Executor Memory (MB)** | **Worker CPU** | **Worker Memory ( GB)**  
---|---|---|---  
1 | 2048 | 4 | 15  
1 | 3072 | 4 | 21  
1 | 4096 | 4 | 26  
2 | 8192 | 4 | 26  
  
For example, a 26 GB worker node translates to 20 GB of memory usable for running YARN containers. With executor memory set to 4 GB, 1 GB is added as overhead, which means 5 GB YARN containers for each executor. This means the worker can run four containers without any extra resources leftover. You can also multiply the size of the workers. For example, if executor memory is set to 4096 GB, a worker with 8 CPUs and 52 GB memory would also work well. Compute Engine VMs restrict how much memory the VM can have based on the number of cores. For example, a VM with 4 cores must have at least 7.25 GB of memory and at most 26 GB of memory. This means an executor set to use 1 CPU and 8 GB of memory uses 2 CPUs and 26 GB of memory on the VM. If executors are instead configured to use 2 CPUs and 8 GB of memory, all of the CPUs are utilized.

### Disk

Disk is important for some pipelines but not all of them. If your pipeline does not contain any shuffles, disk will only be used when Spark runs out of memory and needs to spill data to disk. For these types of pipelines, disk size and type are generally not going to make a big impact on your performance. If your pipeline is shuffling a lot of data, disk performance will make a difference. If you are using Managed Service for Apache Spark, it is recommended that you use disk sizes of at least 1tb, as disk performance scales up with disk size. For information about disk performance, see [Configure disks to meet performance requirements](https://docs.cloud.google.com/compute/docs/disks/performance).

### Number of workers

In order to minimize execution time, you will want to ensure that your cluster is large enough that it can run as much as it can in parallel. For example, if your pipeline source reads data using 100 splits, you will want to make sure the cluster is large enough to run 100 executors at once.

The easiest way to tell if your cluster is undersized is by looking at the YARN pending memory over time. If you are using Managed Service for Apache Spark, a graph can be found on the cluster detail page.

If pending memory is high for long periods of time, you can increase the number of workers to add that much extra capacity to your cluster. In the preceding example, the cluster should be increased by around 28 GB to ensure that the maximum level of parallelism is achieved.

#### Enhanced Flexibility Mode (EFM)

EFM lets you specify that only primary worker nodes be involved when shuffling data. Since secondary workers are no longer responsible for intermediate shuffle data, when they are removed from a cluster, Spark jobs don't run into delays or errors. Since primary workers are never scaled down, the cluster scales down with more stability and efficiency. If you're running pipelines with shuffles on a static cluster, it is recommended that you use EFM.

For more information on EFM, see [Managed Service for Apache Spark enhanced flexibility mode](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/flex).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
