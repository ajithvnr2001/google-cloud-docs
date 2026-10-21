---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/metrics-serverless/
title: Spark metrics \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:27.391828+00:00
---

# Spark metrics  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/metrics-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Spark metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about Spark metrics. By default, Managed Service for Apache Spark enables the collection of available Spark metrics, unless you use Spark metrics collection properties to disable or override the collection of one or more Spark metrics.

For additional properties that you can set when you submit a Managed Service for Apache Spark batch workload, see [Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties)

## Spark metrics collection properties

You can use the properties listed in this section to disable or override the collection of one or more available Spark metrics.

Property | Description  
---|---  
`spark.dataproc.driver.metrics` | Use to disable or override Spark driver metrics.  
`spark.dataproc.executor.metrics` | Use to disable or override Spark executor metrics.  
`spark.dataproc.system.metrics` | Use to disable Spark system metrics.  
  
gcloud CLI examples:

  * Disable Spark driver metric collection:
        
        gcloud dataproc batches submit spark \
            --properties spark.dataproc.driver.metrics="" \
            --region=region \
            other args ...
        

  * Override Spark default driver metric collection to collect only `BlockManager:disk.diskSpaceUsed_MB` and `DAGScheduler:stage.failedStages` metrics:
        
        gcloud dataproc batches submit spark \
            --properties=^~^spark.dataproc.driver.metrics="BlockManager:disk.diskSpaceUsed_MB,DAGScheduler:stage.failedStages" \
            --region=region \
            other args ...
        


**Note:** Since a comma (`,`) is used to separate two values associated with the `spark.dataproc.driver.metrics` property in the previous example, the `~` character is specified as the property delimiter character instead of the default comma delimiter. For more information, see [cluster properties formatting ](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#formatting).

## Available Spark metrics

Managed Service for Apache Spark collects the Spark metrics listed in this section unless you use Spark metric collection properties to disable or override their collection.

**Note:** Metrics are collected in the following format:

`custom.googleapis.com/METRIC_EXPLORER_NAME`.

### Spark driver metrics 

Metric | Metrics Explorer name  
---|---  
BlockManager:disk.diskSpaceUsed_MB | spark/driver/BlockManager/disk/diskSpaceUsed_MB  
BlockManager:memory.maxMem_MB | spark/driver/BlockManager/memory/maxMem_MB  
BlockManager:memory.memUsed_MB | spark/driver/BlockManager/memory/memUsed_MB  
DAGScheduler:job.activeJobs | spark/driver/DAGScheduler/job/activeJobs  
DAGScheduler:job.allJobs | spark/driver/DAGScheduler/job/allJobs  
DAGScheduler:messageProcessingTime | spark/driver/DAGScheduler/messageProcessingTime  
DAGScheduler:stage.failedStages | spark/driver/DAGScheduler/stage/failedStages  
DAGScheduler:stage.runningStages | spark/driver/DAGScheduler/stage/runningStages  
DAGScheduler:stage.waitingStages | spark/driver/DAGScheduler/stage/waitingStages  
  
### Spark executor metrics 

Metric | Metrics Explorer name  
---|---  
ExecutorAllocationManager:executors.numberExecutorsDecommissionUnfinished | spark/driver/ExecutorAllocationManager/executors/numberExecutorsDecommissionUnfinished  
ExecutorAllocationManager:executors.numberExecutorsExitedUnexpectedly | spark/driver/ExecutorAllocationManager/executors/numberExecutorsExitedUnexpectedly  
ExecutorAllocationManager:executors.numberExecutorsGracefullyDecommissioned | spark/driver/ExecutorAllocationManager/executors/numberExecutorsGracefullyDecommissioned  
ExecutorAllocationManager:executors.numberExecutorsKilledByDriver | spark/driver/ExecutorAllocationManager/executors/numberExecutorsKilledByDriver  
LiveListenerBus:queue.executorManagement.listenerProcessingTime | spark/driver/LiveListenerBus/queue/executorManagement/listenerProcessingTime  
executor:bytesRead | spark/executor/bytesRead  
executor:bytesWritten | spark/executor/bytesWritten  
executor:cpuTime | spark/executor/cpuTime  
executor:diskBytesSpilled | spark/executor/diskBytesSpilled  
executor:jvmGCTime | spark/executor/jvmGCTime  
executor:memoryBytesSpilled | spark/executor/memoryBytesSpilled  
executor:recordsRead | spark/executor/recordsRead  
executor:recordsWritten | spark/executor/recordsWritten  
executor:runTime | spark/executor/runTime  
executor:shuffleFetchWaitTime | spark/executor/shuffleFetchWaitTime  
executor:shuffleRecordsRead | spark/executor/shuffleRecordsRead  
executor:shuffleRecordsWritten | spark/executor/shuffleRecordsWritten  
executor:shuffleRemoteBytesReadToDisk | spark/executor/shuffleRemoteBytesReadToDisk  
executor:shuffleWriteTime | spark/executor/shuffleWriteTime  
executor:succeededTasks | spark/executor/succeededTasks  
ExecutorMetrics:MajorGCTime | spark/executor/ExecutorMetrics/MajorGCTime  
ExecutorMetrics:MinorGCTime | spark/executor/ExecutorMetrics/MinorGCTime  
  
### System metrics 

Metric | Metric Explorer Name  
---|---  
agent:uptime | agent/uptime  
cpu:utilization | cpu/utilization  
disk:bytes_used | disk/bytes_used  
disk:percent_used | disk/percent_used  
memory:bytes_used | memory/bytes_used  
memory:percent_used | memory/percent_used  
network:tcp_connections | network/tcp_connections  
  
## View Spark metrics

To view Batch metrics, click a batch ID on the Managed Service for Apache Spark [**Batches**](https://console.cloud.google.com/dataproc/batches) page in the Google Cloud console to open the batch **Details** page, which displays a metrics graph for the batch workload under the **Monitoring tab**.

![](https://docs.cloud.google.com/static/managed-spark/images/spark-batch-metrics-graph.png)**Figure 1.** Spark metrics graph for a batch workload. 

See Managed Service for Apache Spark [Cloud Monitoring](https://docs.cloud.google.com/managed-spark/docs/guides/monitoring) for additional information on how to view collected metrics.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
