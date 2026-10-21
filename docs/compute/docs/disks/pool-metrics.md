---
url: https://docs.cloud.google.com/compute/docs/disks/pool-metrics/
title: Available metrics for Hyperdisk pools \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:11:32.174892+00:00
---

# Available metrics for Hyperdisk pools  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/pool-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Available metrics for Hyperdisk pools Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the metrics for Hyperdisk pools, including Hyperdisk Storage Pools and Hyperdisk Exapools.

Metrics help you answer questions about a pool, like its provisioned performance and capacity, the number of disks in the pool, and its overprovisioning rate.

For instructions on how to view the metrics listed on this page, see [Monitor pool usage and performance](https://docs.cloud.google.com/compute/docs/disks/monitor-pool-performance). 

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Hyperdisk pool metrics

The following table lists metrics that are available for both Hyperdisk Storage Pools and Hyperdisk Exapools.

For metrics specific to Storage Pools and Exapools, see Storage Pool metrics and Exapool metrics, respectively.

To refer to the metric programmatically, for example, with PromQL, prefix the **Metric name** with `compute.googleapis.com/`, which has been omitted from the table for readability. For example, the fully qualified name for the capacity overprovisioning metric is `compute.googleapis.com/storage_pool/capacity_overprovisioning`.

Questions | Metric | Description  
---|---|---  
pool properties  
How many disks are in the pool? | **Metric display name** : Disks  
  
**Metric name** : (`storage_pool/disks`)  | The number of disks that are in the pool.   
How much capacity was provisioned for the storage pool? | **Metric display name** : Provisioned Capacity  
  
**Metric name** : (`storage_pool/provisioned_capacity`)  | The size, in TiB, of the pool.   
Capacity-related metrics  
What percentage of the pool's total capacity has been provisioned to the disks in the pool?  
If the pool's capacity is overprovisioned, what is the overprovisioning rate?  | **Metric display name** : Capacity Overprovisioning (%)  
  
**Metric name:** (`storage_pool/capacity_overprovisioning`)  
|  The ratio of the total provisioned capacity of disks in the pool to its provisioned capacity, as a percentage.   
For **Advanced capacity pools** , a value greater than 100% means capacity is overprovisioned. The overprovisioning rate is the percentage of total provisioned disk capacity relative to the pool's total capacity.   
How much data has been written to the disks in the pool, relative to the pool's provisioned capacity (the utilization rate)? |   
**Metric display name** : Capacity Utilization (%)  
  
**Metric name** : (`storage_pool/capacity_utilization`)  | The used capacity of the pool, represented as a percentage of the overall pool capacity. This value is calculated using the following formula:   
`Utilization = (used_capacity/provisioned_capacity) * 100`  
How much capacity has been provisioned to the disks created in the pool? | **Metric display name** : Total Disk Provisioned Capacity  
  
**Metric name** : (`storage_pool/total_disk_provisioned_capacity`)  | The sum of the capacity that is provisioned across all the disks in the pool. For example, a pool with 10 disks, each 5 TiB in size, would return 50 TiB for the Total Disk Provisioned Capacity metric.   
How much data, in bytes, has been written to the pool, including any data reduction? | **Metric display name** : Used Capacity  
  
**Metric name** : (`storage_pool/used_capacity`)  
| For **Standard capacity pools** : This is the sum of the provisioned capacity for all the disks in the storage pool. This is equivalent to the _Total Disk Provisioned Capacity_.   
For **Advanced capacity pools** : This is the number of bytes written to the disks in the storage pool. The value is aggregated for all the disks in the storage pool, after data reduction, if supported.   
Performance-related metrics  
How much throughput has been allocated, or provisioned, to the disks created in the storage pool? | **Metric display name** : Total Disk Provisioned Throughput **Metric name** : (`storage_pool/total_disk_provisioned_throughput`)  | Sum of the provisioned throughput for all the disks in the pool, in MiB/s.   
How much IOPS has been allocated to the disks created in the storage pool? | **Metric display name** : Total Disk Provisioned IOPS  **Metric name** : (`storage_pool/total_disk_provisioned_iops`)  | Sum of the provisioned IOPS for all the disks in the pool.   
  
### Hyperdisk Storage Pool metrics

The following table lists the metrics available for only Hyperdisk Storage Pools.

Questions | Metric | Description  
---|---|---  
Hyperdisk Storage Pool properties  
How much IOPS were provisioned for the Storage Pool? | **Metric display name** : Provisioned IOPS  
**Metric name** : (`storage_pool/provisioned_iops`)  | Provisioned IOPS of the Storage Pool. This metric is only valid for Hyperdisk Balanced Storage Pools.   
How much throughput was provisioned for the Storage Pool? | **Metric display name** : Provisioned Throughput  
**Metric name** : (`storage_pool/provisioned_throughput`)  | Provisioned throughput of the Storage Pool.   
Performance usage metrics  
What percentage of the Storage Pool's provisioned IOPS has been provisioned to disks in the pool?   
If the pool's IOPS are overprovisioned, what is the overprovisioning rate?  | **Metric display name** : IOPS Overprovisioning (%)  
**Metric name** : (`storage_pool/iops_overprovisioning`)  
| The ratio of the total provisioned IOPS of disks in the Storage Pool to its provisioned IOPS, as a percentage.   
For **Advanced performance pools** , a value greater than 100% means that the pool's IOPS are overprovisioned. The overprovisioning rate is a percentage of the total disk provisioned IOPS to the pool's provisioned IOPS.  
What percentage of the Storage Pool's provisioned throughput has been provisioned to disks in the pool?   
If the pool's throughput is overprovisioned, what is the overprovisioning rate?  | **Metric display name** : Throughput Overprovisioning(%)  
**Metric name** : (`storage_pool/throughput_overprovisioning`)  
| The ratio of the total provisioned throughput of disks in the Storage Pool to its provisioned throughput, as a percentage.   
For **Advanced performance pools** , a value greater than 100% means throughput is overprovisioned. The overprovisioning rate is the percentage of total provisioned disk throughput relative to the pool's total throughput.  
What percentage of the Storage Pool's provisioned IOPS has been used, or consumed, by the disks in the pool? | **Metric display name** : IOPS Utilization (%)  
**Metric name** : (`storage_pool/iops_utilization`)  
| Ratio of the total IOPS provisioned to the disks in the Storage Pool to the Storage Pool's provisioned IOPS, as a percentage. This value is calculated using the following formula:   
`Utilization = (used_iops/provisioned_iops) * 100`  
What percentage of the Storage Pool's total throughput has been used, or consumed, by disks? | **Metric display name** : Throughput Utilization (%)  
**Metric name** : (`storage_pool/throughput_utilization`)  
| The used throughput of the Storage Pool, represented as a percentage of its provisioned throughput. This value is calculated using the following formula:   
` Utilization = (used_throughput/provisioned_throughput) * 100`  
How much of the provisioned IOPS of the Storage Pool has been used, or consumed, by the disks in the pool? | **Metric display name** : Used IOPS  
**Metric name** : (`storage_pool/used_iops`)  
| For **Standard performance pools** , this is equal to the _Total Disk Provisioned IOPS_ , and the first 3,000 IOPS provisioned per disk are not counted towards this value.   
For **Advanced performance pools** , this is the sum of the IOPS consumed by all the disks in the Storage Pool for the specified period of time. This metric differs from the total IOPS provisioned to the disks in the Storage Pool.  
How much of the provisioned throughput of the Storage Pool has been used, or consumed, by the disks in the Storage Pool? | **Metric display name** : Used throughput  
**Metric name** : (`storage_pool/used_throughput`)  
| For **Standard performance pools** , this is equal to the _Total Disk Provisioned Throughput_ , and the first 140 MiB/s of provisioned throughput per disk are not counted towards this value.   
For **Advanced performance pools** , this is the sum of the throughput consumed by all the disks in the Storage Pool for the specified period of time. This metric differs from the total throughput provisioned to the disks in the Storage Pool.   
  
### Hyperdisk Exapool metrics

The following table lists the metrics available for only Hyperdisk Exapools.

Questions | Metric | Description  
---|---|---  
Exapool properties  
How many read IOPS were purchased for the Exapool? | **Metric display name** : Pool Maximum Read IOPS | The total read IOPS purchased for the Exapool based on the blend of capacity units. This metric is only valid for Hyperdisk Balanced Exapools.   
How much read throughput was purchased for the Exapool? | **Metric display name** : Pool Maximum Read Throughput  
| The total read throughput purchased for the Exapool based on the blend of capacity units.   
How many write IOPS were purchased for the Exapool? | **Metric display name** : Pool Maximum Write IOPS  
| The total write IOPS purchased for the Exapool, based on the blend of capacity units. This metric is only valid for Hyperdisk Balanced Exapools.   
How much write throughput was purchased for the Exapool? | **Metric display name** : Pool Maximum Write Throughput  
| The total write throughput purchased for the Exapool based on the blend of capacity units   
Performance-related metrics  
How much read IOPS have the disks in the Exapool consumed? | **Metric display name** : Pool Used Read IOPS  
  
**Metric name** : (`storage_pool/used_read_iops`)  | Used read IOPS aggregated for all the disks in the Exapool. You can compare this to the provisioned read IOPS to determine if you need to adjust the blend of capacity units.   
How much read throughput have the disks in the Exapool consumed?  | **Metric display name** : Pool Used Read Throughput  
  
**Metric name** : (`storage_pool/used_read_throughput`)  | Used read throughput aggregated for all the disks in the Exapool. You can compare this to the provisioned read throughput to determine if you need to adjust the blend of capacity units.   
How much write IOPS have the disks in the Exapool consumed? | **Metric display name** : Pool Used Write IOPS  
  
**Metric name** : (`storage_pool/used_write_iops`)   
| Used write IOPS aggregated for all the disks in the Exapool. You can compare this to the provisioned write IOPS to determine if you need to adjust the blend of capacity units.   
How much write throughput have the disks in the Exapool consumed? | **Metric display name** : Pool Used Write Throughput  
  
**Metric name** : (`storage_pool/used_write_throughput`)  | Used write throughput aggregated for all the disks in the Exapool. You can compare this to the provisioned write throughput to determine if you need to adjust the blend of capacity units.   
Capacity-related metrics  
How much data are workloads writing to the disks in the pool? | **Metric display name** : Pool User Written Bytes  
| The sum of the bytes written by applications that are using the disks in the Exapool. This field is used to calculate the Data Reduction Ratio metric.  You can view this metric only using the Cloud Monitoring; You can't view this metric by using the Google Cloud CLI.   
How effective are the data reduction strategies? | **Metric display name** : Pool Data Reduction Ratio | How much data was written by applications on the disks in the pool compared to how much was saved to block storage. It's calculated as:   
`Pool user written bytes / Pool used capacity`.   
For example, a value of "2:1" would mean that every 2 bytes of data that applications write to the disks in the pool is reduced to 1 byte before it's saved to block storage.   
  
## What's next

  * To learn how to review a pool's metrics, see [Monitor pool usage and performance](https://docs.cloud.google.com/compute/docs/disks/monitor-pool-performance).

  * For a full list of all disk metrics, see [Compute Engine metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
