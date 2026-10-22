---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/resource-management/
title: Resource management \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:58.698177+00:00
---

# Resource management  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/resource-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Resource management Stay organized with collections  Save and categorize content based on your preferences. 

Pipelines let you specify the CPUs and memory to give to the driver and each executor. You can configure resources in the Cloud Data Fusion Studio pipeline configurations. For more information, see [Manage pipeline configurations](https://docs.cloud.google.com/data-fusion/docs/concepts/manage-pipeline-configurations).

This page provides the guidelines on how much driver and executor resources to configure for your use case.

## Driver

Since the driver doesn't do much work, the default of 1 CPU and 2 GB memory is enough to run most pipelines. You might need to increase the memory for pipelines that contain many stages or large schemas. As mentioned in [Parallel processing of JOINs](https://docs.cloud.google.com/data-fusion/docs/concepts/parallel-processing-join-operations), if the pipeline is performing in-memory joins, the in-memory datasets also need to fit in the driver's memory.

## Executor

Consider the following guidelines on CPU and memory resources.

### CPU

The number of CPUs assigned to an executor determines the number of tasks the executor can run in parallel. Each partition of data requires one task to process. In most cases, it's simplest to set the number of CPUs to one, and instead focus on adjusting memory.

### Memory

For most pipelines, 4 GB of executor memory is enough to successfully run the pipeline. Heavily skewed, multi-terabyte joins have been completed with 4 GB of executor memory. It's possible to improve execution speed by increasing the amount of memory, but this requires a strong understanding of both your data and your pipeline.

Spark divides memory into several sections. A section is reserved for Spark internal usage, and another is for execution and storage.

By default, the storage and execution section is roughly 60% of the total memory. Spark's `spark.memory.fraction configuration` property (defaults to 0.6) controls this percentage. This amount performs well for most workloads and normally doesn't need to be adjusted.

The storage and execution section is further divided into separate spaces for storage and execution. By default, those spaces are the same size, but you can adjust them by setting `spark.memory.storageFraction` (defaults to 0.5) to control what percentage of the space is reserved for storage.

The storage space stores cached data. The execution space stores shuffle, join, sort, and aggregation data. If there's extra space in the execution section, Spark can use some of it for storage data. However, execution data will never use any of the storage space.

If you know your pipeline isn't caching any data, you can reduce the storage fraction to leave more room for execution requirements.

#### Point to consider: YARN container memory

The executor memory setting controls the amount of heap memory given to the executors. Spark adds an additional amount of memory for off-heap memory, which is controlled by the `spark.executor.memoryOverhead` setting, which defaults to 384m. That means that the amount of memory YARN reserves for each executor is higher than the number set in the pipeline resources configuration. For example, if you set executor memory to 2048m, Spark adds 384m to that number and requests YARN for a 2432m container. On top of that, YARN rounds the request number up to a multiple of `yarn.scheduler.increment-allocation-mb`, which defaults to the value of `yarn.scheduler.minimum-allocation-mb`. If it is set to 512, YARN rounds the 2432m up to 2560m. If the value is set to 1024, YARN rounds up the 2432m to 3072m. This point is useful to keep in mind when determining the size of each worker node in your cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
