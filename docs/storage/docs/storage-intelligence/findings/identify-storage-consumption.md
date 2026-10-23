---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/identify-storage-consumption/
title: Identify above trend storage consumption \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:29.031566+00:00
---

# Identify above trend storage consumption  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/identify-storage-consumption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Identify above trend storage consumption Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Storage Intelligence advisor to identify above-trend storage consumption. Identifying growth trends helps you determine whether you are storing data unnecessarily and optimize your storage usage.

When total bytes stored increases above trend, Storage Intelligence advisor displays a `Total bytes stored increased above trend over the last 30 days` finding. A _finding_ is an anomaly detected from your metrics that needs your attention. For an overview of Storage Intelligence advisor, see [About Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview). For a full list of findings, see [Findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog).

## Thresholds that trigger a finding

To identify above-trend growth, Storage Intelligence analyzes historical data over a 30-day period to establish a baseline for storage consumption across your project, folder, or organization. Storage Intelligence advisor generates a finding when storage consumption increases above this baseline.

Findings reflect the previous day's activity. For example, a spike occurring on Tuesday appears in Storage Intelligence advisor on Wednesday.

## Respond to a finding

To respond to the finding, identify which data is causing the growth and determine the best management strategy.

  1. [View the finding details](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor#view-finding-details).

  2. On the **Finding details** page, use the **Buckets with largest increases** table and the bucket-specific **Prefixes with largest increases** to identify which datasets are growing.

  3. Once you know which data is growing, decide if that data needs to be managed differently based on its access patterns or retention needs. Use the following table to select the recommended strategy for your scenario:

Scenario | Recommended action | Details  
---|---|---  
Data is not needed after a specific period | Apply [lifecycle rules](https://docs.cloud.google.com/storage/docs/lifecycle) | If you no longer need data after a specific period or want to move data to a colder storage class, use Object Lifecycle Management rules to manage your storage consumption.  
Data with changing access patterns | Enable [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) | Autoclass automatically transitions objects in your bucket to appropriate storage classes based on access patterns. It moves less frequently accessed data to colder storage classes and more frequently accessed data to warmer storage classes, which helps manage costs automatically. **Note:** Enabling Autoclass incurs charges for Class A operations associated with object transitions. For details, see [Cloud Storage Pricing](https://docs.cloud.google.com/storage/pricing).  
Need object-level details to understand storage growth | Investigate with Storage Insights datasets | If you need granular information about storage growth, use Storage Insights datasets to export metadata to BigQuery. You can then query the dataset to identify the specific prefixes and objects that contribute to the growth. **Note:** Exporting data to BigQuery incurs costs. For details, see [BigQuery Pricing](https://docs.cloud.google.com/bigquery/pricing).  



## What's next

  * **Key tasks** : 
    * [View Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor#view-finding-details)
  * **Explore other findings** : 
    * [Improve performance by mitigating rate limited request errors](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors)
    * [Optimize usage for Coldline and Archive storage data](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs)
    * [Manage cross-region egress](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/manage-egress)
    * [Review the findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog)
  * **Related concepts** : 
    * [Storage Intelligence advisor overview](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview)
    * [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle)
    * [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
