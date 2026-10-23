---
url: https://docs.cloud.google.com/managed-spark/quotas-serverless/
title: Managed Service for Apache Spark serverless quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:08.037557+00:00
---

# Managed Service for Apache Spark serverless quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/quotas-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Resources ](https://docs.cloud.google.com/managed-spark/docs/resources)



Send feedback 

#  Managed Service for Apache Spark serverless quotas Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark has API quota limits that are enforced at the project and region level. The quotas reset every 60 seconds (1 minute).

**Handling Managed Service for Apache Spark Quota Errors** : If you exceed a Managed Service for Apache Spark quota limit, a [RESOURCE_EXHAUSTED](https://docs.cloud.google.com/apis/design/errors#handling_errors) (HTTP code 429) is generated, and the corresponding Managed Service for Apache Spark API request fails. However, since your project's Managed Service for Apache Spark quota is refreshed every 60 seconds, you can retry your request after 1 minute has elapsed following the failure.

The following table lists the specific and default per-project Managed Service for Apache Spark API quota types, quota limits, and the methods to which they apply.

Quota Type | Limit | API Methods or Description  
---|---|---  
ClusterOperationRequestsPerMinutePerProjectPerRegion | 200 | CancelOperation (cancelling batch operation quota is shared with cancelling cluster operation quota).  
BatchOperationRequestsPerMinutePerProjectPerRegion | 200 | CreateBatch, DeleteBatch  
SessionOperationRequestsPerMinutePerProjectPerRegion | 200 | CreateSession, DeleteSession, TerminateSession  
DefaultRequestsPerMinutePerProjectPerRegion | 7,500 | GetBatch, ListBatches, GetSession, ListSessions  
ActiveOperationsPerProjectPerRegion | 5,000 | Limit on the total number of concurrent active operations of all types in a project in a region.  
**Increasing Resource Quota Limits** : Open the Google Cloud [IAM & Admin Quotas](https://console.cloud.google.com/iam-admin/quotas) page, and select the resources you want to modify. Then click **Edit Quotas** at the top of the page to start the quota increase process. If the resources you are trying to increase aren't displayed on the page and the current filtering is "Quotas with usage," change the filtering to "All quotas" by toggling the "Quota type" dropdown.

## Other Google Cloud quotas

Managed Service for Apache Spark batches use other Google Cloud products. These products have project-level quotas, which include quotas that apply to Managed Service for Apache Spark use. Some services are required to use Managed Service for Apache Spark, such as [Compute Engine](https://docs.cloud.google.com/compute "Compute Engine") and [Cloud Storage](https://docs.cloud.google.com/storage "gcs_name"). Other services, such as [BigQuery](https://docs.cloud.google.com/bigquery "bigquery_name") and [Bigtable](https://docs.cloud.google.com/bigtable "Bigtable"), can optionally be used with Managed Service for Apache Spark.

### Required services

The following services, which enforce quota limits, are required to create Managed Service for Apache Spark batches.

#### Compute Engine

Managed Service for Apache Spark batch workloads can select a variety of Compute Engine resources:

  * To mitigate obtainability issues with CPUs and disks, Managed Service for Apache Spark supports fallback across multiple machine families and disk types. For example, in the Premium tier, a batch workload can fall back to `N2` with persistent SSD, `N2D` with local SSD, `N2D` with persistent disk, `N4` with hyperdisk balanced, or `N4D` with hyperdisk balanced.

  * A batch workload fails if it has insufficient quota to consume the fallback selection resources.




The following table lists [Compute Engine resource quotas](https://docs.cloud.google.com/compute/resource-usage) that apply to Managed Service for Apache Spark batch workloads.

Compute Tier | Quota  
---|---  
Standard | `CPUS`  
Premium | 

  * `N2_CPUS`
  * `N2D_CPUS`
  * `CPUS_PER_VM_FAMILY` with N4 VM Family
  * `CPUS_PER_VM_FAMILY` with N4D VM Family

  
Disk Tier | Quota  
Standard | `DISKS_TOTAL_GB`  
Premium | 

  * `DISKS_TOTAL_GB`
  * `LOCAL_SSD_TOTAL_GB_PER_VM_FAMILY` with N2 and N2D VM Families
  * `SSD-TOTAL-GB` or `Persistent Disk SSD (GB)`
  * `HDB-TOTAL-GB` or `Hyperdisk Balanced Capacity (GB)`

  
GPU accelerator | Quota  
L4 | `NVIDIA_L4_GPUS`  
A100 40GB | `NVIDIA_A100_GPUS`  
A100 80GB | `NVIDIA_A100_80GB_GPUS`  
  
The [Compute Engine quotas](https://docs.cloud.google.com/compute/resource-usage "Compute Engine Quotas") are split into regional and global limits. These limits apply to batches you create. For example, to run a Spark batch with 4 driver cores (`spark.driver.cores=4`) and two executors with 4 cores each (`spark.executor.cores=4`), you use 12 virtual CPUs (`4 * 3`). This batch usage counts against the regional quota limit of 24 virtual CPUs.

**Free trial quotas:** If you use the Compute Engine free trial, your project will have a limit of 8 CPUs. To increase this limit, you must enable billing on the project. 

#### Default batch resources

When you create a batch with default settings, the following Compute Engine resources are used:

**Item** | **Resources used**  
---|---  
Virtual CPUs | 12  
Virtual Machine (VM) Instances | 3  
Persistent disk | 1,200 GiB  
  
#### Cloud Logging

Managed Service for Apache Spark saves batch output and logs in [Cloud Logging](https://docs.cloud.google.com/logging "Cloud Logging"). The [Cloud Logging quota](https://docs.cloud.google.com/logging/quota-policy "Cloud Logging quota") applies to your Managed Service for Apache Spark batches.

### Optional services

The following services, which have quota limits, can optionally be used with Managed Service for Apache Spark batches.

#### BigQuery

When reading or writing data into BigQuery, the [BigQuery quota](https://docs.cloud.google.com/bigquery/quota-policy "BigQuery quota") applies.

#### Bigtable

When reading or writing data into Bigtable, the [Bigtable quota](https://docs.cloud.google.com/bigtable/quota "Bigtable quota") applies.

## Identify workloads with quota or IP address limitations

You can use the following [Cloud Logging](https://console.cloud.google.com/logs/query) queries to identify Managed Service for Apache Spark workloads that reached your quota or were unable to scale due to IP address exhaustion.

Quota query:
    
    
    jsonPayload.@type="type.googleapis.com/google.cloud.dataproc.logging.AutoscalerLog"
    jsonPayload.recommendation.outputs.constraintsReached="SCALING_CAPPED_DUE_TO_LACK_OF_QUOTA"
    

IP address exhaustion query:
    
    
    jsonPayload.@type="type.googleapis.com/google.cloud.dataproc.logging.AutoscalerLog"
    jsonPayload.status.details =~".*Insufficient free IP addresses.*"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
