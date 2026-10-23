---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/enhanced-flexibility-mode/
title: Managed Service for Apache Spark Enhanced Flexibility Mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:13.062147+00:00
---

# Managed Service for Apache Spark Enhanced Flexibility Mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/enhanced-flexibility-mode/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark Enhanced Flexibility Mode Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark Enhanced Flexibility Mode (EFM) manages shuffle data to minimize job progress delays caused by the removal of nodes from a running cluster. EFM offloads shuffle data by writing data to primary workers. Workers pull from those remote nodes during the reduce phase. This mode is only available for Spark jobs.

Since EFM doesn't store intermediate shuffle data on secondary workers, EFM is well suited to clusters that use [preemptible VMs](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/preemptible-vms) or only [autoscale](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling) the secondary worker group.

EFM is supported on Managed Service for Apache Spark `2.0.31+`, `2.1.6+`, `2.2+`, and later [image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported_dataproc_versions).

**Limitations:**

  * [Apache Hadoop YARN](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html) jobs that don't support AppMaster relocation can fail in Enhanced Flexibility Mode (see When to wait for AppMasters to finish).
  * Enhanced Flexibility Mode is **not recommended** : 
    * on a cluster that has primary workers only
    * on streaming jobs since it can take up to 30 minutes after job completion to clean up intermediate shuffle data.
    * on a cluster that runs notebooks since shuffle data might not be cleaned up during the life of the session.
    * when Spark jobs run on a cluster with graceful decommissioning enabled. Graceful decommissioning and EFM can work at cross purposes since the YARN graceful decommission mechanism keeps the DECOMMISSIONING nodes until all involved applications complete.
    * on a cluster that runs both Spark and non-Spark jobs.
  * Enhanced Flexibility Mode is **not supported** : 
    * when primary worker autoscaling is enabled. In most cases, primary workers will continue to store shuffle data that is not automatically migrated. Downscaling the primary worker group negates EFM benefits.



## Use Enhanced Flexibility Mode

Enhanced Flexibility is enabled when you create a cluster by setting the `dataproc:efm.spark.shuffle` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties) to `primary-worker`.

**Example:**
    
    
    gcloud dataproc clusters create cluster-name \
        --region=region \
        --properties=dataproc:efm.spark.shuffle=primary-worker \
         other flags ...
    

### Apache Spark example

  1. Run a WordCount job against public Shakespeare text using the Spark examples jar on the EFM cluster. 
         
         gcloud dataproc jobs submit spark \
             --cluster=cluster-name \
             --region=region \
             --jars=file:///usr/lib/spark/examples/jars/spark-examples.jar \
             --class=org.apache.spark.examples.JavaWordCount \
             -- gs://apache-beam-samples/shakespeare/macbeth.txt
         




### Configure local SSDs

Since EFM writes intermediate shuffle data to VM-attached disks, it benefits from the additional throughput and IOPS provided by [local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd). To facilitate resource allocation, target a goal of approximately 1 local SSD partition per 4 vCPUs when configuring primary worker machines.

To attach local SSDs, pass the `--num-worker-local-ssds` flag to the [gcloud Managed Service for Apache Spark clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command.

Generally, you won't need local SSDs on secondary workers. Adding local SSDs to a cluster's secondary workers (using the `--num-secondary-worker-local-ssds` flag) is often of less importance because secondary workers don't write shuffle data locally. However, since local SSDs improve local disk performance, you may decide to add local SSDs to secondary workers if you expect jobs to be [I/O bound](https://en.wikipedia.org/wiki/I/O_bound) due to local disk use: your job uses significant local disk for scratch space or your partitions are [too large to fit in memory and will spill to disk](https://spark.apache.org/faq.html).

### Secondary worker ratio

Since secondary workers write their shuffle data to primary workers, your cluster must contain a sufficient number of primary workers with sufficient CPU, memory, and disk resources to accommodate your job's shuffle load. For autoscaling clusters, to prevent the primary group from scaling and causing unwanted behavior, set `minInstances` to the `maxInstances` value in the [autoscaling policy](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.autoscalingPolicies#AutoscalingPolicy.InstanceGroupAutoscalingPolicyConfig) for the primary worker group.

Consider starting with a conservative 1:1 ratio of primary to secondary workers (your workflow may be able to tolerate additional secondary workers). 

If you have a high secondary-to-primary workers ratio (for example, 10:1), monitor the CPU utilization, network, and disk usage of primary workers to determine if they are overloaded. To do this:

  1. Go to the [VM instances](https://console.cloud.google.com/compute/instances) page in the Google Cloud console.

  2. Click the checkbox to the left side of primary worker.

  3. Click the MONITORING tab to view the primary worker's CPU Utilization, Disk IOPS, Network Bytes, and other metrics.




If primary workers are overloaded, consider [scaling up primary workers manually](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flex#resizing_the_primary_worker_group).

### Resize the primary worker group

The primary worker group can be safely scaled up, but downscaling the primary worker group can negatively impact job progress. Operations that downscale the primary worker group should use [graceful decommissioning](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scaling-clusters#graceful_decommissioning), which is enabled by setting the `--graceful-decommission-timeout` flag.

**Autoscaled clusters:** Primary worker group scaling is disabled on EFM clusters with autoscaling policies. To resize the primary worker group on an autoscaled cluster:

  1. Disable autoscaling. 
         
         gcloud dataproc clusters update \
             --cluster=cluster-name \
             --region=region \
             --disable-autoscaling
         

  2. Scale the primary group. 
         
         gcloud dataproc clusters update \
             --cluster=cluster-name \
             --region=region \
             --num-workers=num-primary-workers \
             --graceful-decommission-timeout=graceful-decommission-timeout # (if downscaling)
         

  3. Re-enable autoscaling: 
         
         gcloud dataproc clusters update \
             --cluster=cluster-name \
             --region=region \
             --autoscaling-policy=autoscaling-policy
         




### Monitor primary worker disk use

Primary workers must have sufficient disk space for the cluster's shuffle data. You can monitor this indirectly through the `remaining HDFS capacity` metric. As local disk fills up, space becomes unavailable for HDFS, and the remaining capacity decreases.

By default, when a primary worker's local disk use [exceeds 90% of capacity](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/NodeManager.html#Disk_Checker), the node will be marked as UNHEALTHY in the YARN node UI. If you experience disk capacity issues, you can delete unused data from HDFS or scale up the primary worker pool.

## Advanced configuration

### Partitioning and parallelism

When submitting a Spark job, configure an appropriate level of partitioning. Deciding on the number of input and output partitions for a shuffle stage involves a trade off among different performance characteristics. It is best to experiment with values that work for your job shapes.

**Input partitions**

Spark and MapReduce input partitioning are determined by the input dataset. When reading files from Cloud Storage, each task processes approximately one "block size" worth of data.

  * For Spark SQL jobs, the maximum partition size is controlled by `spark.sql.files.maxPartitionBytes`. Consider increasing it to 1GB: `spark.sql.files.maxPartitionBytes=1073741824`.

  * For Spark RDDs, partition size is usually controlled with `fs.gs.block.size`, which defaults to 128MB. Consider increasing it to 1GB. Example: `--properties spark.hadoop.fs.gs.block.size=1073741824`




**Output partitions**

The number of tasks in subsequent stages is controlled by several properties. On larger jobs that process more than 1TB, consider having at least 1GB per partition.

  * For Spark SQL, the number of output partitions is controlled by `spark.sql.shuffle.partitions`.

  * For Spark jobs using the RDD API, you can specify the number of output partitions or set `spark.default.parallelism`.




### Shuffle tuning for primary worker shuffle

The most significant property is `--properties yarn:spark.shuffle.io.serverThreads=<num-threads>`. Note that this is a cluster-level YARN property because the Spark shuffle server runs as part of the Node Manager. It defaults to twice (2x) number of cores on the machine (for example, 16 threads on an n1-highmem-8). If "Shuffle Read Blocked Time" is larger than 1 second, and primary workers have not reached network, CPU or disk limits, consider increasing the number of shuffle server threads.

On larger machine types, consider increasing `spark.shuffle.io.numConnectionsPerPeer`, which defaults to 1. (For example, set it to 5 connections per pair of hosts).

### Increase retries

The maximum number of attempts permitted for app masters, tasks, and stages can be configured by setting the following properties:
    
    
    yarn:yarn.resourcemanager.am.max-attempts
    spark:spark.task.maxFailures
    spark:spark.stage.maxConsecutiveAttempts
    

Since app masters and tasks are more frequently terminated in clusters that use many preemptible VMs or autoscaling without graceful decommissioning, increasing the values of the preceding properties in those clusters can help (note that using EFM with Spark and graceful decommissioning is not supported).

## YARN graceful decommissioning on EFM clusters

[YARN Graceful Decommissioning](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/GracefulDecommission.html) can be used to remove nodes quickly with minimal impact on running applications. For autoscaling clusters, the [graceful decommissioning timeout](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scaling-clusters#using_graceful_decommissioning) can be set in an [AutoscalingPolicy](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling#create_an_autoscaling_policy) that is attached to the EFM cluster.

### EFM enhancements to graceful decommissioning

  1. Since intermediate data is stored in a distributed file system, nodes can be removed from an EFM cluster as soon as all containers running on those nodes have finished. By comparison, nodes are not removed on standard Managed Service for Apache Spark clusters until the application has finished.

  2. Node removal does not wait for app masters running on a node to finish. When the app master container is terminated, it is rescheduled on another node that is not being decommissioned. Job progress is not lost: the new app master quickly recovers state from the previous app master by reading job history.


**When to wait for AppMasters to finish**. If you run applications that don't support AppMaster recovery, your application can wait for AppMasters to finish by setting the following [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties) to **`true`** when you create the Enhanced Flexibility Mode cluster. 
    
    
    yarn:yarn.resourcemanager.decommissioning-nodes-watcher.wait-for-app-masters=true
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
