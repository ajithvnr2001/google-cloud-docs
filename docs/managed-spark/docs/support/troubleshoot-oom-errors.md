---
url: https://docs.cloud.google.com/managed-spark/docs/support/troubleshoot-oom-errors/
title: Troubleshoot VM out-of-memory errors \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:36.899885+00:00
---

# Troubleshoot VM out-of-memory errors  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/support/troubleshoot-oom-errors/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Troubleshoot VM out-of-memory errors Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information on Managed Service for Apache Spark on Compute Engine VM out-of-memory (OOM) errors, and explains steps you can take to troubleshoot and resolve OOM errors.

## OOM error effects

When Managed Service for Apache Spark VMs encounter out-of-memory (OOM) errors, the effects include the following conditions:

  * Master and worker VMs freeze for a period of time.

  * Master VMs OOM errors cause jobs to fail with "task not acquired" errors.

  * Worker VM OOM errors cause a loss of the node on YARN HDFS, which delays Managed Service for Apache Spark job execution.




## YARN memory controls

[Apache YARN](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html) provides the following types of [memory controls](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/NodeManagerCGroupsMemory.html):

  * Polling based (legacy)
  * Strict
  * Elastic



By default, Managed Service for Apache Spark doesn't set `yarn.nodemanager.resource.memory.enabled` to enable YARN memory controls, for the following reasons:

  * Strict memory control can cause the termination of containers when there is sufficient memory if container sizes aren't configured correctly.
  * Elastic memory control requirements can adversely affect job execution.
  * YARN memory controls can fail to prevent OOM errors when processes aggressively consume memory.



## Managed Service for Apache Spark memory protection

When a Managed Service for Apache Spark cluster VM is under memory pressure, Managed Service for Apache Spark memory protection terminates processes or containers until the OOM condition is removed.

Managed Service for Apache Spark provides memory protection for the following cluster nodes in the following [Managed Service for Apache Spark image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters):

Role | 1.5 | 2.0 | 2.1 | 2.2  
---|---|---|---|---  
Master VM | 1.5.74+ | 2.0.48+ | all | all  
Worker VM | Not Available | 2.0.76+ | 2.1.24+ | all  
Driver Pool VM | Not Available | 2.0.76+ | 2.1.24+ | all  
Use Managed Service for Apache Spark image versions with memory protection to help avoid VM OOM errors.

### Identify and confirm memory protection terminations

You can use the following information to identify and confirm job terminations due to memory pressure.

#### Process terminations

  * Processes that Managed Service for Apache Spark memory protection terminates exit with code `137` or `143`.

  * When Managed Service for Apache Spark terminates a process due to memory pressure, the following actions or conditions can occur:

    * Managed Service for Apache Spark increments the `dataproc.googleapis.com/node/problem_count` cumulative metric, and sets the `reason` to `ProcessKilledDueToMemoryPressure`. See [Managed Service for Apache Spark resource metric collection](https://docs.cloud.google.com/managed-spark/docs/guides/metrics#dataproc_resource_metric_collection).
    * Managed Service for Apache Spark writes a `google.dataproc.oom-killer` log with the message: `"A process is killed due to memory pressure: process name`. To view these messages, enable Logging, then use the following log filter: 
          
          resource.type="cloud_dataproc_cluster"
          resource.labels.cluster_name="CLUSTER_NAME"
          resource.labels.cluster_uuid="CLUSTER_UUID"
          jsonPayload.message:"A process is killed due to memory pressure:"
          




#### Master node or driver node pool job terminations

  * When a Managed Service for Apache Spark master node or driver node pool job terminates due to memory pressure, the job fails with error `Driver received SIGTERM/SIGKILL signal and exited with INT` code. To view these messages, enable Logging, then use the following log filter: 
        
        resource.type="cloud_dataproc_cluster"
        resource.labels.cluster_name="CLUSTER_NAME"
        resource.labels.cluster_uuid="CLUSTER_UUID"
        jsonPayload.message:"Driver received SIGTERM/SIGKILL signal and exited with"
            

    * Check the `google.dataproc.oom-killer` log or the `dataproc.googleapis.com/node/problem_count` to confirm that Managed Service for Apache Spark Memory Protection terminated the job (see Process terminations).

**Solutions:**

    * If the cluster has a [driver pool](https://docs.cloud.google.com/managed-spark/docs/guides/node-groups/driver-node-groups), increase `driver-required-memory-mb` to actual job memory usage.
    * If the cluster does not have a driver pool, recreate the cluster, lowering the [maximum number of concurrent jobs](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/life-of-a-job#job_concurrency) running on the cluster.
    * Use a master node machine type with increased memory.



#### Worker node YARN container terminations

  * Managed Service for Apache Spark writes the following message in the YARN resource manager: `container id exited with code EXIT_CODE`. To view these messages, enable Logging, then use the following log filter:
        
        resource.type="cloud_dataproc_cluster"
        resource.labels.cluster_name="CLUSTER_NAME"
        resource.labels.cluster_uuid="CLUSTER_UUID"
        jsonPayload.message:"container" AND "exited with code" AND "which potentially signifies memory pressure on NODE
        

  * If a container exited with `code INT`, check the `google.dataproc.oom-killer` log or the `dataproc.googleapis.com/node/problem_count` to confirm that Managed Service for Apache Spark Memory Protection terminated the job (see Process terminations).

**Solutions:**

    * Check that container sizes are configured correctly.
    * Consider lowering `yarn.nodemanager.resource.memory-mb`. This property controls the amount of memory used for scheduling YARN containers.
    * If job containers consistently fail, check if data skew is causing increased usage of specific containers. If so, repartition the job or increase worker size to accommodate additional memory requirements.



## Fine-tune Linux memory protection on the master node (advanced)

Managed Service for Apache Spark master nodes use the `earlyoom` utility to prevent system hangs by freeing memory when available memory is critically low. The default configuration is suitable for many workloads. However, you might need to adjust the configuration if your master node has a large amount of memory and experiences rapid memory consumption.

In scenarios with high memory pressure, the system can enter a state of "thrashing," where it spends most of its time on memory management and becomes unresponsive. This can happen so quickly that `earlyoom` fails to take action based on its default settings or fails to act before the kernel OOM response is invoked.

### Before you begin

  * This is an advanced tuning option. Before you adjust `earlyoom` settings, prioritize other solutions, such as using a master VM with more memory, reducing job concurrency, or optimizing job memory usage.



### Customize `earlyoom` settings

The default `earlyoom` configuration uses a fixed amount of free memory as a trigger. On virtual machines with a large amount of RAM, for example `32GB` or more, this fixed amount might represent a small fraction of the total memory. This makes the system susceptible to sudden spikes in memory usage.

To customize the `earlyoom` settings, connect to the master node and modify the configuration file.

  1. [Connect to your master node using SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh).

  2. Open the configuration file for editing:
         
         sudo nano /etc/default/earlyoom
         

  3. Adjust the minimum memory threshold. Locate the `EARLYOOM_ARGS` line. The `-M <kbytes>` option sets the minimum amount of free memory in KiB that `earlyoom` tries to maintain. The default value is `-M 65536`, which is `64 MiB`. 

**Tuning considerations** : Setting the `-M` value too high can cause `earlyoom` to terminate processes more aggressively. This can impact applications even when sufficient memory might still be available for them. Monitor system behavior after making changes. Adjust the `-M` value based on your instance size and workload. A general guideline is to set `-M` to a value that represents `1-5%` of total system memory.

For a master node with substantial memory, increase this value. For example, to set the threshold to `1 GiB` (`1048576 KiB`), modify the line as follows:
         
         EARLYOOM_ARGS="-r 15 -M 1048576 -s 1"
         

Notes:

     * `-r`: Memory report interval in seconds
     * `-s`: The swap space threshold to trigger `earlyoom`
  4. Restart the `earlyoom` service to apply the changes:
         
         sudo systemctl restart earlyoom
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
