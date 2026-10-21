---
url: https://docs.cloud.google.com/storage-transfer/docs/move-your-cloud-storage-data-to-another-location/
title: Move your Cloud Storage data to another location \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:44.737967+00:00
---

# Move your Cloud Storage data to another location  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/move-your-cloud-storage-data-to-another-location/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Move your Cloud Storage data to another location Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2022-06-20 UTC

When you create a Cloud Storage bucket, you choose its permanent geographic location. As your business needs change, where you store your data might need to change too. For example, your data might be better situated in a highly available dual-region bucket, a lower cost regional bucket, or simply a different region of the world.

This tutorial helps you to select a [location](https://docs.cloud.google.com/storage/docs/locations) that best fits your needs.

## Objectives

  * Choose a new location for the Cloud Storage data.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

There are no prerequisites to this tutorial.

## Choose a new location

When you choose the location for a Cloud Storage bucket, consider the differences in availability, and price, as shown in the following table.

| Zone | Region | Dual-region | Multi-region  
---|---|---|---|---  
[Availability](https://docs.cloud.google.com/storage/docs/availability-durability) | 

  * Data redundancy within one availability zone
  * Zonal outages might affect availability

| 

  * Data redundancy across availability zones (synchronous)
  * RTO(recovery time objective)=0: automated failover and failback on zonal failure (no need to change storage paths)

| 

  * Higher availability than regions for a given storage class
  * Data redundancy across regions (asynchronous)
  * [ Turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) option for replication within 15 minutes
  * RTO(recovery time objective)=0: automated failover and failback on regional failure (no need to change storage paths)

| 

  * Higher availability than regions for a given storage class
  * Data redundancy across regions (asynchronous)
  * RTO(recovery time objective)=0: automated failover and failback on regional failure (no need to change storage paths)

  
[Pricing](https://docs.cloud.google.com/storage/pricing#storage-pricing) | 

  * Offers the highest performance in Cloud Storage for demanding workloads at the highest storage price, out of all location types
  * Zonal bucket-specific data transfer charges apply. For more information, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).

| 

  * Lowest storage price
  * No replication charges
  * No outbound data transfer charges when reading data inside the same region

| 

  * Highest storage price
  * Replication charges apply on write
  * No outbound data transfer charges when reading data within either region

| 

  * Higher storage price than regions, but lower than dual-regions
  * Replication charges apply on write
  * Outbound data transfer charges always apply when reading data

  
  
### Location recommendations

Requirements | Recommended bucket location | Workload examples  
---|---|---  
  
  * Ultra-low latency
  * Ultra-high bandwidth and I/O
  * High performance

| Zone1 | 

  * Artificial Intelligence (AI) and Machine Learning (ML)
  * High-performance computing
  * Data-intensive analytics

  
  
  * Optimized latency and bandwidth
  * Lowest data storage cost
  * Cross-zone redundancy

| Region2 | 

  * Analytics
  * Backup and archive

  
  
  * Optimized latency and bandwidth
  * Cross-region redundancy, with precise control of the locations where copies of data are stored

| Dual-region3 | 

  * Analytics
  * Backup and archive
  * Disaster recovery

  
  
  * Cross-geography data access
  * Cross-region redundancy

| Multi-region | 

  * Content serving

  
  
  1. Zonal locations for buckets are only available through [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket).
  2. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 
  3. If you need a short and predictable [ recovery point objective (RPO)](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning), enable the premium [ turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) feature.



  * To maximize performance and lower the latency between requests and responses, colocate your stored data in the same zone as the compute resources accessing your data. To store data in zones, use [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket).
  * To withstand the risk of losing data within an individual zone, use regions or dual-regions.
  * To avoid data replication charges, store short-lived datasets in regions.
  * For moderate performance and ad hoc analytics workloads, multi-region storage can be a cost-effective choice.

Note that the performance of workloads that use data in a multi-region bucket might vary over time because storage and compute aren't colocated. When a multi-region workload has strict performance requirements, consider enabling [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache).

  * When transferring to a new bucket, consider if the current [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) still suits your needs.




## Plan and start the transfer

After you've decided on a new location, see [Transfer between Cloud Storage buckets](https://docs.cloud.google.com/storage-transfer/docs/cloud-storage-to-cloud-storage) to plan and perform your data move.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2022-06-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2022-06-20 UTC."],[],[]] 
