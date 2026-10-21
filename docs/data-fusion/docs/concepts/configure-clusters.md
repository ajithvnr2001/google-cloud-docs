---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters/
title: Managed Service for Apache Spark cluster configuration \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:31.397417+00:00
---

# Managed Service for Apache Spark cluster configuration  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/configure-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Managed Service for Apache Spark cluster configuration Stay organized with collections  Save and categorize content based on your preferences. 

In Cloud Data Fusion, cluster configuration refers to defining how your data processing pipelines utilize computational resources when running Spark jobs on Managed Service for Apache Spark. This page describes the main approaches to cluster configuration.

## Default ephemeral clusters (recommended)

Using the default clusters is the recommended approach for Cloud Data Fusion pipelines.

  * Cloud Data Fusion automatically provisions and manages ephemeral Managed Service for Apache Spark clusters for each pipeline execution. It creates a cluster at the beginning of the pipeline run, and then deletes it after the pipeline run completes.
  * Benefits of ephemeral clusters: 
    * **Simplicity** : you don't need to manually configure or manage the cluster.
    * **Cost-effectiveness** : you only pay for the resources used during pipeline execution.

**Note:** Cloud Data Fusion, by default, uses Managed Service for Apache Spark Autoscaling compute profile which creates ephemeral clusters as per the default configurations.

To adjust clusters and tune performance, see [Cluster sizing](https://docs.cloud.google.com/data-fusion/docs/concepts/cluster-sizing).

## Static clusters (for specific scenarios)

In the following scenarios, you can use static clusters:

  * **Long-running pipelines** : for pipelines that run continuously or for extended periods, a static cluster can be more cost-effective than repeatedly creating and tearing down ephemeral clusters.
  * **Centralized cluster management** : if your organization requires centralized control over cluster creation and management policies, static clusters can be used alongside tools like Terraform.
  * **Cluster creation time** : when the time it takes to create a new cluster for every pipeline is prohibitive for your use case.



However, static clusters require more manual configuration and involve managing the cluster lifecycle yourself.

To use a static cluster, you must set the following [properties](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/cluster-properties) on the Managed Service for Apache Spark cluster:
    
    
    dataproc:dataproc.conscrypt.provider.enable=false
    capacity-scheduler:yarn.scheduler.capacity.resource-calculator="org.apache.hadoop.yarn.util.resource.DefaultResourceCalculator"
    

### Cluster configuration options for static clusters

If you choose to use static clusters, Cloud Data Fusion offers configuration options for the following aspects:

  * **Worker machine type** : specify the virtual machine type for the worker nodes in your cluster. This determines the vCPUs and memory available for each worker.
  * **Number of workers** : define the initial number of worker nodes in your cluster. Managed Service for Apache Spark might still autoscale this number, based on workload.
  * **Zone** : select your cluster's Google Cloud zone. Location can affect data locality and network performance.
  * **Additional configurations** : you can configure advanced options for your static cluster, such as preemption settings, network settings, and initialization actions.



## Best practices

When creating a static cluster for your pipelines, use the following configurations.

Parameters | Description  
---|---  
`yarn.nodemanager.delete.debug-delay-sec` | Retains YARN logs.  
Recommended value: `86400` (equivalent to one day)  
`yarn.nodemanager.pmem-check-enabled` | Enables YARN to check for physical memory limits and kill containers if they go beyond physical memory.  
Recommended value: `false`  
`yarn.nodemanager.vmem-check-enabled` | Enables YARN to check for virtual memory limits and kill containers if they go beyond physical memory.  
Recommended value: `false`  
`dataproc.scheduler.driver-size-mb` | The average memory footprint of the driver makes Managed Service for Apache Spark queue the job if the master node lacks sufficient memory to run the driver process. This can impact [job concurrency](https://docs.cloud.google.com/dataproc/docs/concepts/jobs/life-of-a-job#job_concurrency) but can be mitigated by using a master node with more memory.  
Recommended value: `2048`  
  
For more information, see [Run a pipeline against an existing Managed Service for Apache Spark cluster](https://docs.cloud.google.com/data-fusion/docs/how-to/running-against-existing-dataproc).

## Reusing clusters

You can reuse Managed Service for Apache Spark clusters between runs to improve processing time. Cluster reuse is implemented in a model similar to connection pooling or thread pooling. Any cluster is kept up and running for a specified time after the run is finished. When a new run is started, it will try to find an idle cluster available that matches the configuration of the compute profile. If one is present, it will be used, otherwise a new cluster will be started.

### Considerations for reusing clusters

  * Clusters are not shared. Similar to the regular ephemeral cluster provisioning model, a cluster runs a single pipeline run at a time. A cluster is reused only if it is idle**.**
  * If you enable cluster reuse for all your runs, the necessary number of clusters to process all your runs will be created as needed. Similar to the ephemeral Managed Service for Apache Spark provisioner, there is no direct control on the number of clusters created. You can still use Google Cloud quotes to manage resources. For example, if you run 100 runs with 7 maximum parallel runs, you will have up to 7 clusters at a given point of time.
  * Clusters are reused between different pipelines as soon as those pipelines are using the same profile and share the same profile settings. If profile customization is used, clusters will still be reused, but only if customizations are exactly the same, including all cluster settings like cluster labeling.

  * When cluster reuse is enabled, there are two main cost considerations:

    * Less resources are used for cluster startup and initialization.
    * More resources are used for clusters to sit idle between the pipeline runs and after the last pipeline run.



While it's hard to predict the cost effect of cluster reuse, you can employ a strategy to get maximum savings. The strategy is to identify a critical path for chained pipelines and enable cluster reuse for this critical path. This would ensure the cluster is immediately reused, no idle time is wasted and maximum performance benefits are achieved.

### Enable Cluster Reuse

In the Compute Config section of deployed pipeline configuration or when creating new compute profile:

  * Enable **Skip Cluster Delete**.
  * Max Idle Time is the time up to which a cluster waits for the next pipeline to reuse it. The default Max Idle Time is 30 minutes. For Max Idle Time, consider the cost versus cluster availability for reuse. The higher the value of Max Idle Time, the more clusters sit idle, ready for a run. 



## Troubleshoot: Version compatibility

**Problem** : The version of your Cloud Data Fusion environment might not be compatible with the version of your Managed Service for Apache Spark cluster.

**Recommended** : Upgrade to the latest Cloud Data Fusion version and use one of the [supported Managed Service for Apache Spark versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_dataproc_versions).

Earlier versions of Cloud Data Fusion are only compatible with [unsupported versions of Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#unsupported_dataproc_versions). Managed Service for Apache Spark does not provide updates and support for clusters created with these versions. Although you can continue running a cluster that was created with an unsupported version, we recommend replacing it with one created with a [supported version](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_dataproc_versions).

Cloud Data Fusion version | Managed Service for Apache Spark version  
---|---  
6.11.1 | 2.3, 2.2***, 2.1  
6.10.1.1 | 2.2***, 2.1, 2.0 *  
6.10 | 2.1, 2.0 *  
6.9 | 2.1, 2.0, 1.5 *  
6.7-6.8 | 2.0, 1.5 *  
6.4-6.6 | 2.0 *, 1.3 **  
6.1-6.3 | 1.3**  
  
* Cloud Data Fusion versions 6.4 and later are compatible with [ supported versions of Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_dataproc_versions). Unless specific OS features are needed, the recommended practice is to specify the [ `major.minor` image version](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/overview#how_versioning_works).  
To specify the OS version used in your Managed Service for Apache Spark cluster, the OS version must be compatible with one of the supported Managed Service for Apache Spark versions for your Cloud Data Fusion in the preceding table. 

** Cloud Data Fusion versions 6.1 to 6.6 are compatible with [ unsupported Managed Service for Apache Spark version 1.3](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#unsupported_dataproc_versions). 

*** Certain [ issues](https://docs.cloud.google.com/data-fusion/docs/release-notes#October_24_2024) are detected with this image version. This Managed Service for Apache Spark image version is not recommended for production use. 

## Troubleshoot: Container exited with a non-zero exit code 3

**Problem** : An autoscaling policy isn't used, and the static Managed Service for Apache Spark clusters are encountering memory pressure, causing an out of memory exception to appear in the logs: `Container exited with a non-zero exit code 3`.

**Recommended** : Increase the executor memory.

Increase the memory by adding a `task.executor.system.resources.memory` runtime argument to the pipeline. The following example runtime argument sets the memory to 4096 MB:
    
    
    "task.executor.system.resources.memory": 4096
    

For more information, see [Cluster sizing](https://docs.cloud.google.com/data-fusion/docs/concepts/cluster-sizing).

## What's next

  * Refer to the [How to change Managed Service for Apache Spark image version](https://docs.cloud.google.com/data-fusion/docs/how-to/change-dataproc-image).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
