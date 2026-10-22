---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/manage-egress/
title: Manage cross-region egress \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:37.299029+00:00
---

# Manage cross-region egress  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/manage-egress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Manage cross-region egress Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Storage Intelligence advisor to manage cross-region egress.

Cross-region egress occurs when applications transfer data from Cloud Storage buckets in one region to Google Cloud services in another region. Colocating your Google Cloud services and storage resources helps manage cross-region egress.

Storage Intelligence advisor displays the **Spike in cross-region egress** finding when cross-region egress increases above historical trends in your project, folder, or organization. A _finding_ is an anomaly detected from your metrics that needs your attention. For an overview of Storage Intelligence advisor, see [About Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview). For a full list of findings, see [Findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog).

## Thresholds that trigger a finding

Storage Intelligence analyzes historical data to establish a baseline for cross-region egress across your project, folder, or organization. Storage Intelligence advisor generates a finding when cross-region egress increases above this baseline over the last 24 hours.

Findings reflect the previous day's activity. For example, a spike occurring on Tuesday appears in Storage Intelligence advisor on Wednesday.

## Respond to a finding

  1. [View the finding details](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor#view-finding-details).

  2. Use the following table to select the recommended strategy for your scenario:

Scenario | Recommended action | Details  
---|---|---  
Data is frequently accessed from another region | Colocate resources using [bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview) | Colocate storage with Google Cloud services to optimize performance and reduce cross-region egress costs. Bucket relocation helps you move an existing Cloud Storage bucket from one geographic location to another.  
Need to understand which data or access patterns are driving egress | Investigate with Storage Insights datasets | If you need more granular information about what is driving cross-region egress, use Storage Insights to export metadata to BigQuery to identify specific prefixes, objects, and access patterns. **Note:** Exporting data to BigQuery incurs costs. For details, see [BigQuery Pricing](https://cloud.google.com/bigquery/pricing).  



## What's next

  * **Key tasks** : 
    * [View Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor#view-finding-details)
  * **Explore other findings** : 
    * [Improve performance by mitigating rate limited request errors](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors)
    * [Optimize usage for Coldline and Archive storage data](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs)
    * [Identify above trend storage consumption](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/identify-storage-consumption)
    * [Review the findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog)
  * **Related concepts** : 
    * [Storage Intelligence advisor overview](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview)
    * [Bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
