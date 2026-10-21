---
url: https://docs.cloud.google.com/managed-spark/docs/support/spark-job-tuning/
title: Spark job tuning tips \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:48.728700+00:00
---

# Spark job tuning tips  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/support/spark-job-tuning/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Spark job tuning tips Stay organized with collections  Save and categorize content based on your preferences. 

The following sections provide tips to help you fine tune your Managed Service for Apache Spark Spark applications.

## Use ephemeral clusters

When you use the Managed Service for Apache Spark "ephemeral" cluster model, you create a dedicated cluster for each job, and when the job finishes, you delete the cluster. With the ephemeral model, you can treat storage and compute separately, saving job input and output data in Cloud Storage or BigQuery, using the cluster for compute and temporary data storage only.

### Persistent cluster pitfalls

Using ephemeral one-job clusters avoids the following pitfalls and potential problems associated with using shared and long-running "persistent" clusters:

  * Single points of failure: a shared cluster error state can cause all jobs to fail, blocking an entire data pipeline. Investigating and recovering from an error can take hours. Since ephemeral clusters keep temporary in-cluster states only, when an error occurs, they can be quickly deleted and recreated.
  * Difficulty maintaining and migrating cluster states in HDFS, MySQL or local filesystems
  * Resource contentions among jobs that negatively affect SLOs
  * Unresponsive service daemons caused by memory pressure
  * Buildup of logs and temporary files that can exceed disk capacity
  * Upscaling failure due to cluster zone stockout
  * Lack of support for [outdated cluster image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#unsupported-dataproc-image-versions).



### Ephemeral cluster benefits

On the positive side, ephemeral clusters let you do the following:

  * Configure different IAM permissions for different jobs with different [Managed Service for Apache Spark VM service accounts](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#vm_service_account_data_plane_identity).
  * Optimize a cluster's hardware and software configurations for each job, changing cluster configurations as needed.
  * Upgrade image versions in new clusters to get the latest security patches, bug fixes, and optimizations.
  * Troubleshoot issues more quickly on an isolated, single-job cluster.
  * Save costs by paying for ephemeral cluster running time only, not for idle time between jobs on a shared cluster.



## Use Spark SQL

The [Spark SQL](https://spark.apache.org/docs/latest/sql-programming-guide.html) DataFrame API is a significant optimization of the RDD API. If you interact with code that uses RDDs, consider reading data as a DataFrame before passing an RDD in the code. In Java or Scala code, consider using the [Spark SQL](https://spark.apache.org/docs/latest/sql-programming-guide.html) Dataset API as a superset of RDDs and DataFrames.

## Use Apache Spark 3

[Managed Service for Apache Spark 2.0](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.0) installs Spark 3, which includes the following features and performance improvements:

  * GPU support
  * Ability to read binary files
  * Performance improvements
  * Dynamic Partition Pruning
  * [Adaptive query execution](https://spark.apache.org/docs/latest/sql-performance-tuning.html#adaptive-query-execution), which optimizes Spark jobs in real time

Spark 3 improvements primarily result from under-the-hood changes, and require minimal user code changes. For considerations when migrating from Spark 2 to Spark 3, see the [Apache Spark documentation](https://spark.apache.org/docs/latest/migration-guide.html).

## Use Dynamic Allocation

Apache Spark includes a **Dynamic Allocation** feature that scales the number of Spark executors on workers within a cluster. This feature allows a job to use the full Managed Service for Apache Spark cluster even when the cluster scales up. This feature is enabled by default on Managed Service for Apache Spark (`spark.dynamicAllocation.enabled` is set to `true`). See [Spark Dynamic Allocation](https://spark.apache.org/docs/latest/configuration.html#dynamic-allocation) for more information.

## Use Managed Service for Apache Spark autoscaling

Managed Service for Apache Spark [Autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling) dynamically adds and removes Managed Service for Apache Spark workers from a cluster to help ensure that Spark jobs have the resources needed to complete quickly.

It is a [best practice](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling#avoid_scaling_primary_workers) to configure the autoscaling policy to only scale [secondary workers](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms).

## Use Managed Service for Apache Spark Enhanced Flexibility Mode

Clusters with preemptible VMs or an autoscaling policy may receive FetchFailed exceptions when workers are preempted or removed before they finish serving shuffle data to reducers. This exception can cause task retries and longer job completion times.

Recommendation: Use Managed Service for Apache Spark [Enhanced Flexibility Mode](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flex), which does not store intermediate shuffle data on secondary workers, so that secondary workers can be safely preempted or scaled down.

## Configure partitioning and shuffling

Spark stores data in temporary partitions on the cluster. If your application groups or joins DataFrames, it shuffles the data into new partitions according to the grouping and low-level configuration.

Data partitioning significantly impacts application performance: too few partitions limits job parallelism and cluster resource utilization; too many partitions slows down the job due to additional partition processing and shuffling.

### Configuring partitions

The following properties govern the number and size of your partitions:

  * `spark.sql.files.maxPartitionBytes`: the maximum size of partitions when you read in data from Cloud Storage. The default is 128 MB, which is sufficiently large for most applications that process less than 100 TB.

  * `spark.sql.shuffle.partitions`: the number of partitions after performing a shuffle. The default is `1000` for `2.2` and later image version clusters. Recommendation: Set this to 3x the number of vCPUs in your cluster.

  * `spark.default.parallelism`: the number of partitions returned after performing RDD transformations that require shuffles, such as `join`, `reduceByKey` and `parallelize`. The default is the total number of vCPUs in your cluster. When using RDDs in Spark jobs, you can set this number to 3x your vCPUs When using autoscaling, set these numbers to be 3x the total number of cores of your largest cluster, as defined by the `maxInstances` in the worker configuration of your autoscaling policy.




### Limit the number of files

There is a performance loss when Spark reads a large number small files. Store data in larger file sizes, for example, file sizes in the 256MB–512MB range. Similarly, limit the number of output files (to force a shuffle, see Avoid unnecessary shuffles).

### Configure adaptive query execution (Spark 3)

[Adaptive query execution](https://spark.apache.org/docs/latest/sql-performance-tuning.html#adaptive-query-execution) (enabled by default in Managed Service for Apache Spark image version 2.0) provides Spark job performance improvements, including:

  * [Coalescing partitions after shuffles](https://spark.apache.org/docs/latest/sql-performance-tuning.html#coalescing-post-shuffle-partitions)
  * [Converting sort-merge joins to broadcast joins](https://spark.apache.org/docs/latest/sql-performance-tuning.html#converting-sort-merge-join-to-broadcast-join)
  * [Optimizations for skew joins](https://spark.apache.org/docs/latest/sql-performance-tuning.html#optimizing-skew-join).



Although the default configuration settings are sound for most use cases, setting `spark.sql.adaptive.advisoryPartitionSizeInBytes` to `spark.sql.files.maxPartitionBytes` (default 128 MB) can be beneficial.

### Avoid unnecessary shuffles

Spark allows users to manually trigger a shuffle to re-balance their data with the `repartition` function. Shuffles are expensive, so reshuffling data should be used cautiously. Setting the partition configurations appropriately should be sufficient to allow Spark to automatically partition your data.

**Exception:** When writing column-partitioned data to Cloud Storage, repartitioning on a specific column avoids writing many small files to achieve faster write times. 
    
    
    df.repartition("col_name").write().partitionBy("col_name").save("gs://...")
    

## Store data in Parquet or Avro

Spark SQL defaults to reading and writing data in Snappy compressed [Parquet](https://parquet.apache.org/) files. Parquet is in efficient columnar file format that enables Spark to only read the data it needs to execute an application. This is an important advantage when working with large datasets. Other columnar formats, such as [Apache ORC](https://orc.apache.org/), also perform well.

For non-columnar data, [Apache Avro](https://avro.apache.org/docs/current/) provides an efficient binary-row file format. Although typically slower than Parquet, Avro's performance is better than text based formats, such as CSV or JSON.

## Optimize disk size

Persistent disks throughput scales with disk size, which can affect the Spark job performance since jobs write metadata and shuffle data to disk. When using standard persistent disks, disk size should be at least 1 terabyte per worker (see [Performance by persistent disk size](https://docs.cloud.google.com/compute/docs/disks/performance#performance_by_disk_size)).

To monitor worker disk throughput in the Google Cloud console:

  1. Click the cluster name on the [**Clusters**](https://console.cloud.google.com/dataproc/clusters) page.
  2. Click the VM INSTANCES tab.
  3. Click any worker name.
  4. Click the MONITORING tab, then scroll to Disk Throughput to view worker throughput.

When scaling persistent disk size for optimal performance, disk size can be set significantly larger than the amount of data to be allocated to each worker in order to increase the throughput cap of the workers.

### Disk considerations

Ephemeral Managed Service for Apache Spark clusters, which don't benefit from persistent storage. can use [local SSDs](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/local-ssds). Local SSDs are physically attached to the cluster and provide higher throughput than persistent disks (see the [Performance table](https://docs.cloud.google.com/compute/docs/disks/local-ssd#performance)). Local SSDs are available at a fixed size of 375 gigabytes, but you can add multiple SSDs to increase performance.

Local SSDs don't persist data after a cluster is shut down. If you need persistent storage, you can use SSD persistent disks, which provide [higher throughput](https://docs.cloud.google.com/compute/docs/disks/performance#throughput_limits_zonal_pd) for their size than standard persistent disks. SSD persistent disks are also a good choice if partition size will be smaller than 8 KB (however, avoid small partitions).

## Attach GPUs to your cluster

Spark 3 supports GPUs. Use GPUs with the [RAPIDS initialization action](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/rapids) to speed up Spark jobs using the [RAPIDS SQL Accelerator](https://www.nvidia.com/en-us/deep-learning-ai/solutions/data-science/apache-spark-3/). The [GPU driver initialization action](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/gpu) to configure a cluster with GPUs.

## Common job failures and fixes

The following section discuss common causes of and solutions to job failures.

### Out of Memory

Examples: 

  * "Lost executor"
  * "java.lang.OutOfMemoryError: GC overhead limit exceeded"
  * "Container killed by YARN for exceeding memory limits"



Possible fixes: 

  * If using PySpark, raise `spark.executor.memoryOverhead` and lower `spark.executor.memory`.
  * Use [high memory](https://docs.cloud.google.com/compute/docs/machine-resource#memory-optimized_machine_family_guide) machine types.
  * Use smaller partitions.



### Shuffle Fetch Failures

Examples: 

  * "FetchFailedException" (Spark error)
  * "Failed to connect to..." (Spark error)
  * "Failed to fetch" (MapReduce error)



Typically caused by by premature removal of workers which still have shuffle data to serve.

Possible causes and fixes: 

  * Preemptible worker VMs were reclaimed or non-preemptible worker VMs were removed by the autoscaler. Solution: Use [Enhanced Flexibility Mode](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flex) to make secondary workers safely preemptible or scalable. 
  * Executor or mapper crashed due to OutOfMemory error. Solution: increase the memory of executor or mapper.
  * The Spark shuffle service may be overloaded. Solution: decrease the number of job partitions.



### YARN nodes are UNHEALTHY

Examples (from YARN logs): 
    
    
    ...reported UNHEALTHY with details: 1/1 local-dirs usable space is below
    configured utilization percentage/no more usable space
    [ /hadoop/yarn/nm-local-dir : used space above threshold of 90.0% ]
    

Often related to insufficient disk space for shuffle data. Diagnose by viewing log files: 

  * Open your project's [**Clusters**](https://console.cloud.google.com/dataproc/clusters) page in the Google Cloud console, then click the cluster's name.
  * Click VIEW LOGS.
  * Filter logs by `hadoop-yarn-nodemanager`.
  * Search for "UNHEALTHY".



Possible Fixes:

  * The user cache is stored in the directory specified by the `yarn.nodemanager.local-dirs` property in the `yarn-site.xml file`. This file is located at `/etc/hadoop/conf/yarn-site.xml`. You can check the free space in the `/hadoop/yarn/nm-local-dir` path, and free up space by deleting the `/hadoop/yarn/nm-local-dir/usercache` user cache folder.
  * If the log reports "UNHEALTHY" status, recreate your cluster with larger disk space, which will increase the throughput cap.



### User cache taking up disk space

In Managed Service for Apache Spark, the user cache is stored in the directory specified by the `yarn.nodemanager.local-dirs` property in `yarn-site.xml` (`/etc/hadoop/conf/yarn-site.xml`). In most cases, the location is `/hadoop/yarn/nm-local-dir`.

**Possible Fixes:**

  * **Manual cleanup:** Check the free space in the `/hadoop/yarn/nm-local-dir` path, and then free up space by deleting the `/hadoop/yarn/nm-local-dir/usercache` user cache folder.
  * **Long-term resolution:** Manage the cleanup process by setting the following [cluster properties](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#file-prefixed_properties_table):

    * `yarn.nodemanager.localizer.cache.cleanup.interval-ms`
    * `yarn.nodemanager.localizer.cache.target-size-mb`

If you don't want to recreate the cluster, you can update these properties in `yarn-site.xml` on all nodes and then restart the NodeManager by executing the following command on the worker nodes:
    
    sudo systemctl restart hadoop-yarn-nodemanager.service
    

  * **Resize cluster:** If the log reports an "UNHEALTHY" status, recreate your cluster with larger disk space, which will increase the throughput cap.




### Job fails due to insufficient driver memory

When running jobs in cluster mode, the job fails if the memory size of the worker node memory size.

Example from driver logs: 
    
    
    'Exception in thread "main" java.lang.IllegalArgumentException:
    Required AM memory (32768+3276 MB) is above the max threshold (12288 MB) of this cluster!
    Please check the values of 'yarn.scheduler.maximum -allocation-mb' and/or 'yarn.nodemanager.resource.memory-mb'.'
    

Possible Fixes:

  * Set `spark:spark.driver.memory` less than `yarn:yarn.scheduler.maximum-allocation-mb`.
  * Use the same machine type for master and worker nodes.



## What's next

  * Learn more about [Spark performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
