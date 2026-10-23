---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs/
title: Optimize usage for Coldline and Archive storage data \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:28.459550+00:00
---

# Optimize usage for Coldline and Archive storage data  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Optimize usage for Coldline and Archive storage data Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Storage Intelligence advisor to optimize usage by mitigating a high rate of Class A and B operations on data in Coldline storage and Archive storage.

Coldline storage and Archive storage are intended for infrequently accessed data. These storage classes offer lower storage rates than Standard storage and Nearline storage, but they incur higher fees for data retrieval and [Class A and B operations](https://docs.cloud.google.com/storage/pricing#operations-by-class).

Storage Intelligence advisor displays the finding `Spike in Class A/B operations on Coldline or Archive data` when request volume increases for Coldline storage and Archive storage. A _finding_ is an anomaly detected from your metrics that needs your attention. For an overview of Storage Intelligence advisor, see [About Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview). For a full list of findings, see [Findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog).

## Thresholds that trigger a finding

Storage Intelligence creates a baseline for your project, folder, or organization based on historical trends. Storage Intelligence advisor generates a finding when Class A or Class B operations in Coldline storage or Archive storage increase above the baseline.

Findings reflect the previous day's activity. For example, a spike occurring on Tuesday appears in Storage Intelligence advisor on Wednesday.

## Respond to a finding

  1. [View the finding details](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor#view-finding-details).

  2. Use the following table to select the recommended strategy for your scenario:

Scenario | Recommended action | Details  
---|---|---  
Ongoing or persistent spikes in operations | Enable [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) | If you experience ongoing or persistent spikes in operations, enable Autoclass to automatically move frequently accessed objects to Standard storage. This action helps reduce retrieval fees and stabilize costs. **Note:** Enabling Autoclass incurs charges for Class A operations associated with object transitions. For details, see [Cloud Storage Pricing](https://docs.cloud.google.com/storage/pricing).  
Accidental or unintended data scanning | Use [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders) to narrow permissions | If overly permissive access, such as a misconfigured script, causes unexpected operations across buckets, use managed folders to apply granular access controls. Grant only the necessary permissions for your workloads.  
Spikes in operations on a small subset of objects | Investigate with Storage Insights datasets | If spikes occur on a small subset of objects, export metadata to BigQuery to identify specific objects and operations that are contributing to the spike. For example, you can identify the most frequently accessed objects within a specific prefix. **Note:** Exporting data to BigQuery incurs costs. For details, see [BigQuery Pricing](https://docs.cloud.google.com/bigquery/pricing).  
One-time or historical events causing spikes | Monitor Storage Intelligence advisor | If a one-time event such as a migration or audit causes the spike, no action is necessary. Continue to monitor Storage Intelligence advisor to detect future spikes.  



## What's next

  * **Key tasks** : 
    * [View Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor#view-finding-details)
  * **Explore other findings** : 
    * [Improve performance by mitigating rate limited request errors](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors)
    * [Identify above trend storage consumption](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/identify-storage-consumption)
    * [Manage cross-region egress](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/manage-egress)
    * [Review the findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog)
  * **Related concepts** : 
    * [Storage Intelligence advisor overview](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview)
    * [Storage classes](https://docs.cloud.google.com/storage/docs/storage-classes)
    * [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
