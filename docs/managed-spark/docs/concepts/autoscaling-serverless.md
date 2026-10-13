---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling-serverless/
title: Autoscale workload resources \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:49.297048+00:00
---

# Autoscale workload resources  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Autoscale workload resources Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about Managed Service for Apache Spark autoscaling. When you submit your Spark workload, Managed Service for Apache Spark can dynamically scale workload resources, such as the number of executors, to run your workload efficiently. Managed Service for Apache Spark autoscaling is the default behavior, and uses [Spark dynamic resource allocation](https://spark.apache.org/docs/latest/job-scheduling.html#dynamic-resource-allocation) to determine whether, how, and when to scale your workload.

## Managed Service for Apache Spark autoscaling V2

Managed Service for Apache Spark autoscaling version 2 (V2) adds features and improvements to default version 1 (V1) to help you manage Managed Service for Apache Spark workloads, improve workload performance, and save costs:

  * **Asynchronous node downscaling** : Autoscaling V2 replaces V1's synchronous downscaling with asynchronous downscaling. Using asynchronous downscaling, Managed Service for Apache Spark downscales workload resources without waiting for all nodes to finish shuffle migration. This means that long-tail nodes that scale down slowly won't block upscaling.
  * **Intelligent scaling down node selection** : Autoscaling V2 replaces V1's random node selection with an intelligent algorithm that identifies the best nodes to scale down first. This algorithm considers factors such as the node's shuffle data size and idle time.
  * **Configurable Spark grace decommission and shuffle migration behavior** : Autoscaling V2 lets you use standard Spark properties to configure Spark graceful decommissioning and shuffle migration. This feature can help you maintain migration compatibility with your customized Spark properties.

**Note:** Set the `spark.dataproc.scaling.version=2` property to enable Managed Service for Apache Spark autoscaling V2 when you [submit a Spark batch workload](https://docs.cloud.google.com/managed-spark/docs/quickstarts/spark-batch#submit_a_spark_batch_workload).

### Managed Service for Apache Spark autoscaling features

Feature | Managed Service for Apache Spark Autoscaling V1 | Managed Service for Apache Spark Autoscaling V2  
---|---|---  
Node downscaling | Synchronous | Asynchronous  
Node selection for downscaling | Random | Intelligent  
Spark graceful decommissioning and shuffle migration | Not configurable | Configurable  
  
## Spark dynamic allocation properties

The following table lists [Spark Dynamic Allocation](https://spark.apache.org/docs/latest/configuration.html#dynamic-allocation) properties that you can set when you submit a batch workload to control autoscaling (see [how to set Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties)).

**Note:** Also see [Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties), which describes additional properties that you can set when you submit a Managed Service for Apache Spark batch workload.Property | Description | Default  
---|---|---  
`spark.dataproc.scaling.version` | The Managed Service for Apache Spark autoscaling version. Specify version `1` or `2`. | `1`  
`spark.dynamicAllocation.enabled` | Whether to use dynamic resource allocation, which scales up and down the number of executors based on the workload. Setting the value to `false` disables autoscaling for the workload. Default: `true`. | `true`  
`spark.dynamicAllocation.initialExecutors` | The initial number of executors allocated to the workload. After the workload starts, autoscaling may change the number of active executors. Minimum value is `2`; maximum value is `2000`. | `2`  
`spark.dynamicAllocation.minExecutors` | The minimum number of executors to scale the workload down to. Minimum value is `2`. | `2`  
`spark.dynamicAllocation.maxExecutors` | The maximum number of executors to scale the workload up to. Maximum value is `2000`. | `1000`  
`spark.dynamicAllocation.executorAllocationRatio` | Customizes scaling up of the Spark workload. Accepts a value from `0` to `1`. A value of `1.0` provides maximum scale-up capability and helps achieve maximum parallelism. A value of `0.5` sets scale-up capability and parallelism at one-half the max value. | `0.3`  
`spark.dynamicAllocation.diagnosis.enabled` | When `true`, diagnostic information is logged if running executors exceed max-needed executors for the period specified by `spark.dynamicAllocation.diagnosis.interval`. The diagnosis includes an executor summary with idle executor count and idle time percentiles, active task distribution, shuffle data size, and cached RDD size. Use `spark.dynamicAllocation.diagnosis.logLevel` to control the output log level. | `false`  
`spark.dynamicAllocation.profile` | Set to `performance` or `cost` to apply a predefined set of configurations optimized for performance or cost-effectiveness. User-defined properties override the profile's defaults. See Spark dynamic allocation profiles for details. | `none`  
`spark.dynamicAllocation.shuffleTracking.dynamicTimeout.enabled` | When `true`, enables dynamic timeout calculation for executors holding shuffle data. Instead of using the static `spark.dynamicAllocation.shuffleTracking.timeout`, the timeout is calculated based on the amount of shuffle data stored on the executor. This allows executors with small shuffles to be released faster while keeping executors with large shuffles alive longer. | `false`  
`spark.reducer.fetchMigratedShuffle.enabled` | When set to `true`, enables fetching the shuffle output location from the Spark driver after a fetch fails from an executor that was decommissioned due to Spark dynamic allocation. This reduces `ExecutorDeadException` errors caused by shuffle block migration from decommissioned executors to live executors, and reduces stage retries caused by `FetchFailedException` errors (see FetchFailedException caused by ExecutorDeadException). This property is available in Managed Service for Apache Spark [Spark runtime versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-versions) `1.1.12` and later and `2.0.20` and later. | `false`  
`spark.scheduler.excludeShuffleSkewExecutors` | When `true`, avoids scheduling tasks on shuffle-skewed executors, which are executors that have a large amount of shuffle data or a large number of completed map tasks. This can improve performance by mitigating shuffle skew. | `false`  
  
### Spark dynamic allocation profiles

You can set the `spark.dynamicAllocation.profile` property to `performance` or `cost` to apply a predefined set of Spark configurations that are optimized for performance or cost-effectiveness. If you set Spark properties in addition to setting the `spark.dynamicAllocation.profile` property, your settings will override the profile's defaults for those properties.

**performance** : This profile optimizes for minimum execution time by applying the following default settings: 

  * `spark.scheduler.excludeShuffleSkewExecutors`: `true`
  * `spark.dynamicAllocation.executorIdleTimeout`: `300s`
  * `spark.dynamicAllocation.initialExecutors`: `10`



**cost** : This profile optimizes for reduced resource consumption by applying the following default settings: 

  * `spark.dynamicAllocation.executorIdleTimeout`: `120s`
  * `spark.dynamicAllocation.cachedExecutorIdleTimeout`: `120s`
  * `spark.dynamicAllocation.shuffleTracking.dynamicTimeout.enabled`: `true`
  * `spark.dynamicAllocation.diagnosis.enabled`: `true`



## Spark dynamic allocation metrics

Spark batch workloads generate the following metrics related to Spark dynamic resource allocation (for additional information on Spark metrics, see [Monitoring and Instrumentation](https://spark.apache.org/docs/latest/monitoring.html)).

**Note:** See [Spark metrics](https://docs.cloud.google.com/managed-spark/docs/concepts/metrics), which describes properties you can set to control the collection of Spark metrics.Metric | Description  
---|---  
`maximum-needed` | The maximum number of executors needed under the current load to satisfy all running and pending tasks.  
`running` | The number of running executors executing tasks.  
  
## Spark dynamic allocation issues and solutions

  * **FetchFailedException caused by ExecutorDeadException**

Cause: When Spark dynamic allocation scales down an executor, the shuffle file is migrated to live executors. However, since the Spark reducer task on an executor fetches shuffle output from the location set by the Spark driver when the reducer task started, if a shuffle file is migrated, the reducer can continue to attempt to fetch shuffle output from a decommissioned executor, causing `ExecutorDeadException` and `FetchFailedException` errors.

Solution: Enable shuffle location refetching by setting the `spark.reducer.fetchMigratedShuffle.enabled` to `true` when you run your Managed Service for Apache Spark batch workload (see [Set Spark batch workload properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#set_spark_batch_workload_properties)). When this property is enabled, the reducer task refetches the shuffle output location from the driver after a fetch from a decommissioned executor fails.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
