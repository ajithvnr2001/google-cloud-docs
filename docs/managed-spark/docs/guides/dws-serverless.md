---
url: https://docs.cloud.google.com/managed-spark/docs/guides/dws-serverless/
title: Use Dynamic Workload Scheduler \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:03.525297+00:00
---

# Use Dynamic Workload Scheduler  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/dws-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use Dynamic Workload Scheduler Stay organized with collections  Save and categorize content based on your preferences. 

You can use Dynamic Workload Scheduler (DWS) Flex Start mode to improve the obtainability of scarce GPU resources for your Managed Service for Apache Spark batch workloads.

## Overview

Dynamic Workload Scheduler is a capacity-aware scheduler that manages scarce compute resources globally. In **Flex Start** mode, Managed Service for Apache Spark can queue your request for a configurable duration when GPUs are not immediately available due to regional stockouts. 

Flex Start is the default behavior for all GPU-enabled workloads submitted to Managed Service for Apache Spark Spark runtime version `3.0`+. When resources are unavailable, the request is queued instead of failing with a stockout error. Once capacity is obtained, DWS provisions the entire cluster "all-at-once" before execution begins. For more information, see [Introducing Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler).

## Benefits

  * **Increased availability:** Substantial reduction in job failures caused by transient GPU capacity shortages.
  * **Atomic provisioning:** Provisioning of cluster workers as a single unit, ensuring cluster integrity and preventing scenarios where only a partial set of workers is created.
  * **Default reliability:** Improved resource acquisition without manual parameter configuration.



## Quota requirements

To use DWS Flex Start, your project must have sufficient quota:

  * **Preemptible GPU quota:** DWS Flex Start consumes the **preemptible** version of the GPU quota pool rather than the standard pool (for example, `PREEMPTIBLE_NVIDIA_L4_GPUS`). For more information, see [Managed Service for Apache Spark resource quotas](https://docs.cloud.google.com/managed-spark/quotas-serverless#compute-engine).
  * **Local SSD quota:** When using the `performance` storage class with GPU-accelerated machines, Managed Service for Apache Spark provisions Local SSDs for high-speed shuffle and temporary storage. Your project must have sufficient local SSD quota in the target region.



## Configuration

DWS Flex Start is enabled by default for GPU workloads on runtime version `3.0`+. You can use the following Spark properties to customize the timeout or disable the feature:

Property | Description | Values | Default  
---|---|---|---  
`spark.dataproc.[driver|executor].provisioning.mode` | Specifies the provisioning model. Use `queue` for DWS Flex Start (default for GPUs) or `default` to disable DWS and use on-demand provisioning. | `queue`, `default` | `queue` (for GPUs on `3.0`+)  
`spark.dataproc.[driver|executor].provisioning.allocationTimeout` | The maximum duration for the node pool to wait in the queue for capacity. The **default is 1 hour** (`3600s`) and the **maximum is 2 hours** (`7200s`). **Note: Values must end with an 's' suffix**. | duration in seconds (for example, `1800s`) | `3600s`  
  
## Example: GPU batch workload with DWS Flex Start

The following example submits a PySpark batch job using NVIDIA L4 GPUs. With DWS Flex Start active by default, the command sets a 30-minute (`1800s`) queuing timeout for both the driver and executors:
    
    
    gcloud dataproc batches submit pyspark \
        gs://my-bucket/path/to/your-script.py \
        --project="PROJECT_ID" \
        --region="REGION" \
        --version="3.0" \
        --properties="spark.dataproc.driver.resource.accelerator.type=l4,\
    spark.dataproc.driver.provisioning.allocationTimeout=1800s,\
    spark.dataproc.executor.resource.accelerator.type=l4,\
    spark.dataproc.executor.provisioning.allocationTimeout=1800s,\
    spark.dataproc.executor.compute.tier=premium,\
    spark.dataproc.executor.disk.tier=premium"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
